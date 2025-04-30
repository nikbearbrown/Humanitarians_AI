import os
import requests
import random
import time
import argparse
from datetime import datetime
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright
import pandas as pd

load_dotenv()

# Configuration
INSTA_USERNAME = os.getenv('INSTAGRAM_USERNAME')
INSTA_PASSWORD = os.getenv('INSTAGRAM_PASSWORD')
SESSION_FILE = 'instagram_session.json'
BASE_URL = 'https://www.instagram.com/'
IMAGES_DIR = 'images'
SCREENSHOTS_DIR = '{}_post_screenshots'
OUTPUT_EXCEL = 'instagram_data_{}_{}.xlsx'

def setup_directories(username):
    """Create required directories"""
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
    """Perform fresh login and save session"""
    print("Starting login process...")
    page.goto(f'{BASE_URL}accounts/login/')
    
    # Fill credentials with human-like delays
    page.fill('input[name="username"]', INSTA_USERNAME)
    human_like_delay(0.5, 1.2)
    page.fill('input[name="password"]', INSTA_PASSWORD)
    human_like_delay(0.8, 1.5)
    
    # Click submit
    page.click('button[type="submit"]')
    
    try:
        # Handle post-login dialogs
        page.wait_for_url('**/accounts/onetap/**', timeout=15000)
        human_like_delay(2, 3)
        
        for _ in range(2):
            if page.get_by_text('Not Now').count():
                page.get_by_text('Not Now').first.click()
                human_like_delay(1, 2)
    except Exception as e:
        print(f"Login dialog handling failed: {e}")
    
    # Save session cookies
    page.context.storage_state(path=SESSION_FILE)
    print("Login successful and session saved")

def check_session_validity(page, profile_url):
    """Verify if the loaded session is still valid"""
    page.goto(profile_url)
    human_like_delay(2, 3)
    
    # Check for either successful profile load or login redirect
    if 'accounts/login' in page.url:
        print("Session expired/invalid, requires fresh login")
        return False
    return True

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
        return ''

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
    if caption_container.count() > 0:
        return caption_container.first.inner_text()
    return ''

def scrape_profile(userhandle, num_posts):
    screenshot_dir = setup_directories(userhandle)
    data = []
    profile_url = f'{BASE_URL}{userhandle}/'

    with sync_playwright() as p:
        # Launch browser with session if available
        browser = p.chromium.launch(headless=False)
        
        # Load existing session if available
        context_args = {
            "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "viewport": {"width": 1366, "height": 768}
        }
        if os.path.exists(SESSION_FILE):
            context_args["storage_state"] = SESSION_FILE

        context = browser.new_context(**context_args)
        page = context.new_page()

        # Verify session validity
        if not check_session_validity(page, profile_url):
            login(page)
            page.goto(profile_url)

        # Wait for profile content
        page.wait_for_selector('._aagv', timeout=15000)
        print("Session validated successfully")
        
        # Scroll to load posts
        posts = []
        scroll_attempts = 0
        while len(posts) < num_posts and scroll_attempts < 15:
            random_scroll(page)
            human_like_delay(1.5, 2.5)
            posts = page.query_selector_all('._aagv')
            scroll_attempts += 1
        
        posts = posts[:num_posts]
        print(f"Found {len(posts)} posts to process")
        
        for idx, post in enumerate(posts):
            post_data = {
                'userhandle': userhandle,
                'scraped_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            
            # Get main image details
            img = post.query_selector('img')
            alt_text = img.get_attribute('alt')
            img_url = img.get_attribute('src')
            
            # Process date
            try:
                post_data['date'] = alt_text.split('on ')[1].split('.')[0].strip()
            except:
                post_data['date'] = datetime.now().strftime("%Y-%m-%d")
            
            # Download image
            img_filename = f"{userhandle}_post_{idx+1}"
            post_data['image_path'] = download_image(img_url, img_filename)
            
            # Open post modal
            human_like_delay(1, 2)
            post.click()
            page.wait_for_selector('div[role="dialog"]', timeout=10000)
            human_like_delay(1, 1.5)
            
            # Capture screenshot
            screenshot_path = os.path.join(
                screenshot_dir,
                f"{userhandle}_post_{idx+1}_{datetime.now().strftime('%Y%m%d%H%M%S')}.png"
            )
            capture_modal_screenshot(page, screenshot_path)
            post_data['screenshot_path'] = screenshot_path
            
            # Extract post data
            post_data['caption'] = get_caption(page)
            post_data['likes'] = get_likes(page)
            
            # Close modal
            human_like_delay(0.5, 1.2)
            page.keyboard.press('Escape')
            human_like_delay(0.5, 1.0)
            
            data.append(post_data)
            print(f"Processed post {idx+1}/{len(posts)} - {post_data['likes']} likes")
        
        browser.close()
    
    # Save to Excel
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = OUTPUT_EXCEL.format(userhandle, timestamp)
    df = pd.DataFrame(data)
    df.to_excel(output_file, index=False)
    print(f"Data saved to {output_file}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Instagram Scraper')
    parser.add_argument('userhandle', type=str, help='Instagram username to scrape')
    parser.add_argument('-n', '--num_posts', type=int, default=12,
                      help='Number of posts to scrape (default: 12)')
    args = parser.parse_args()
    
    scrape_profile(args.userhandle, args.num_posts)