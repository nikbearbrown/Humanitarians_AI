import os
import requests
import random
import time
import argparse
import torch
from datetime import datetime
from dotenv import load_dotenv
from PIL import Image
from transformers import (
    VisionEncoderDecoderModel,
    ViTImageProcessor,
    AutoTokenizer,
    pipeline
)
from playwright.sync_api import sync_playwright
import pandas as pd
from typing import List

load_dotenv()

INSTA_USERNAME = os.getenv('INSTAGRAM_USERNAME')
INSTA_PASSWORD = os.getenv('INSTAGRAM_PASSWORD')
SESSION_FILE = 'instagram_session.json'
BASE_URL = 'https://www.instagram.com/'
IMAGES_DIR = 'images'
SCREENSHOTS_DIR = 'post_screenshots'
OUTPUT_EXCEL = 'instagram_data_{}_{}.xlsx'

class ScraperModels:
    def __init__(self):
        if torch.backends.mps.is_available():
            self.device = torch.device("mps")
        elif torch.cuda.is_available():
            self.device = torch.device("cuda")
        else:
            self.device = torch.device("cpu")

        self.image_model = VisionEncoderDecoderModel.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
        self.image_processor = ViTImageProcessor.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
        self.tokenizer = AutoTokenizer.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
        self.image_model.to(self.device)

        self.summarizer = pipeline("summarization", model="facebook/bart-large-cnn", device=self.device)

    def analyze_image(self, image_path: str) -> str:
        try:
            image = Image.open(image_path)
            if image.mode != "RGB":
                image = image.convert("RGB")
            
            pixel_values = self.image_processor(images=image, return_tensors="pt").pixel_values.to(self.device)
            output_ids = self.image_model.generate(pixel_values, max_length=16, num_beams=4)
            return self.tokenizer.batch_decode(output_ids, skip_special_tokens=True)[0]
        except Exception as e:
            print(f"Image analysis failed: {e}")
            return ""

    def summarize_caption(self, caption: str) -> str:
        try:
            if len(caption.split()) < 10:
                return caption
            return self.summarizer(caption, max_length=100, min_length=10, do_sample=False)[0]['summary_text']
        except Exception as e:
            print(f"Caption summarization failed: {e}")
            return ""

    def extract_keywords(self, text: str) -> List[str]:
        try:
            stop_words = {"a", "an", "the", "in", "on", "at", "and", "or"}
            words = [word.lower() for word in text.split() if word.isalnum()]
            word_counts = {}
            
            for word in words:
                if word not in stop_words and len(word) > 2:
                    word_counts[word] = word_counts.get(word, 0) + 1
            
            return sorted(word_counts, key=lambda x: word_counts[x], reverse=True)[:5]
        except Exception as e:
            print(f"Keyword extraction failed: {e}")
            return []

def setup_directories(username):
    os.makedirs(IMAGES_DIR, exist_ok=True)
    screenshot_dir = SCREENSHOTS_DIR.format(username)
    os.makedirs(screenshot_dir, exist_ok=True)
    return screenshot_dir

def human_like_delay(min=1, max=3):
    time.sleep(random.uniform(min, max))

def random_scroll(page):
    page.mouse.wheel(0, random.randint(300, 700))
    human_like_delay(0.5, 1.5)

def login(page):
    page.goto(f'{BASE_URL}accounts/login/')
    
    if os.path.exists(SESSION_FILE):
        page.context.storage_state(path=SESSION_FILE)
        return
    
    page.fill('input[name="username"]', INSTA_USERNAME)
    human_like_delay(0.5, 1.2)
    page.fill('input[name="password"]', INSTA_PASSWORD)
    human_like_delay(0.8, 1.5)
    page.click('button[type="submit"]')
    
    try:
        page.wait_for_url('**/accounts/onetap/**', timeout=15000)
        human_like_delay(2, 3)
        for _ in range(2):
            if page.get_by_text('Not Now').count():
                page.get_by_text('Not Now').first.click()
                human_like_delay(1, 2)
    except Exception as e:
        print(f"Login dialog handling failed: {e}")
    
    page.context.storage_state(path=SESSION_FILE)

def check_session_validity(page, profile_url):
    page.goto(profile_url)
    human_like_delay(2, 3)
    return 'accounts/login' not in page.url

def download_image(url, filename):
    try:
        response = requests.get(url, stream=True)
        filepath = os.path.join(IMAGES_DIR, f"{filename}.jpeg")
        with open(filepath, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        return filepath
    except Exception as e:
        print(f"Image download failed: {e}")
        return ""

def capture_modal_screenshot(page, path):
    modal = page.locator('div[role="dialog"]')
    modal.wait_for()
    human_like_delay(0.5, 1.0)
    modal.screenshot(path=path)
    return path

def get_likes(page):
    likes_selector = [
        '//div[@class="x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh xr1yuqi xkrivgy x4ii5y1 x1gryazu x1n2onr6 x1plvlek xryxfnj x1iyjqo2 x2lwn1j xeuugli xdt5ytf x1a02dak xqjyukv x1cy8zhl x1oa3qoh x1nhvcw1"]/span/a/span/span[contains(., "likes")]',
        '//span[contains(text(), "likes")]'
    ]
    for selector in likes_selector:
        try:
            element = page.locator(selector).first
            if element.count() > 0:
                likes_text = element.inner_text()
                return ''.join(filter(str.isdigit, likes_text)) or '0'
        except:
            continue
    return '0'

def get_caption(page):
    caption_container = page.locator('div.xt0psk2 h1')
    return caption_container.first.inner_text() if caption_container.count() > 0 else ""

def scrape_profile(userhandle, num_posts):
    models = ScraperModels()
    screenshot_dir = setup_directories(userhandle)
    data = []
    profile_url = f'{BASE_URL}{userhandle}/'

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context_args = {
            "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "viewport": {"width": 1366, "height": 768}
        }
        if os.path.exists(SESSION_FILE):
            context_args["storage_state"] = SESSION_FILE

        context = browser.new_context(**context_args)
        page = context.new_page()

        if not check_session_validity(page, profile_url):
            login(page)
            page.goto(profile_url)

        page.wait_for_selector('._aagv', timeout=15000)
        
        posts = []
        scroll_attempts = 0
        while len(posts) < num_posts and scroll_attempts < 15:
            random_scroll(page)
            human_like_delay(1.5, 2.5)
            posts = page.query_selector_all('._aagv')
            scroll_attempts += 1
        
        posts = posts[:num_posts]
        
        for idx, post in enumerate(posts):
            post_data = {'userhandle': userhandle, 'scraped_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
            
            img = post.query_selector('img')
            alt_text = img.get_attribute('alt')
            img_url = img.get_attribute('src')
            
            try:
                post_data['date'] = alt_text.split('on ')[1].split('.')[0].strip()
            except:
                post_data['date'] = datetime.now().strftime("%Y-%m-%d")
            
            img_filename = f"{userhandle}_post_{idx+1}"
            post_data['image_path'] = download_image(img_url, img_filename)
            
            human_like_delay(1, 2)
            post.click()
            page.wait_for_selector('div[role="dialog"]', timeout=10000)
            human_like_delay(1, 1.5)
            
            screenshot_path = os.path.join(screenshot_dir, f"{userhandle}_post_{idx+1}_{datetime.now().strftime('%Y%m%d%H%M%S')}.png")
            post_data['screenshot_path'] = capture_modal_screenshot(page, screenshot_path)
            
            original_caption = get_caption(page)
            post_data['likes'] = get_likes(page)
            
            image_context = models.analyze_image(post_data['image_path']) if post_data['image_path'] else ""
            caption_summary = models.summarize_caption(original_caption)
            keywords = models.extract_keywords(f"{image_context} {original_caption}")
            
            post_data.update({
                'original_caption': original_caption,
                'image_context': image_context,
                'caption_summary': caption_summary,
                'keywords': ", ".join(keywords)
            })
            
            human_like_delay(0.5, 1.2)
            page.keyboard.press('Escape')
            human_like_delay(0.5, 1.0)
            
            data.append(post_data)
            print(f"Processed post {idx+1}/{len(posts)} - {post_data['likes']} likes")
        
        browser.close()
    
    columns = ['userhandle', 'date', 'image_path', 'screenshot_path', 
              'likes', 'original_caption', 'image_context', 'caption_summary', 'keywords']
    df = pd.DataFrame(data, columns=columns)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = OUTPUT_EXCEL.format(userhandle, timestamp)
    df.to_excel(output_file, index=False)
    print(f"Data saved to {output_file}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Instagram Scraper')
    parser.add_argument('userhandle', type=str, help='Instagram username to scrape')
    parser.add_argument('-n', '--num_posts', type=int, default=12, help='Number of posts to scrape')
    args = parser.parse_args()
    scrape_profile(args.userhandle, args.num_posts)