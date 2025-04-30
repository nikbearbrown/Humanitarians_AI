import instaloader
import sys
import time
import random
import requests
import pandas as pd
import os
import shutil
from imageTag import query


def load_proxies(file_path="proxies_list"):
    """Load proxies from a file."""
    try:
        with open(file_path, "r") as file:
            proxies = [line.strip() for line in file if line.strip()]
        if not proxies:
            print("No proxies found in the file.")
        return proxies
    except FileNotFoundError:
        print("Proxies list file not found.")
        return []


def set_random_proxy(proxies):
    """Set and return a random proxy from the list."""
    if not proxies:
        return None

    proxy = random.choice(proxies)
    proxy_dict = {
        "http": proxy,
        "https": proxy,
    }
    print(f"Using proxy: {proxy}")
    return proxy_dict


def download_instagram_images(username, max_posts=5, proxy_list_path="Proxies/proxy_list.txt"):
    # Load proxies from file
    proxies = load_proxies(proxy_list_path)
    
    # Ensure scraping only proceeds if a valid proxy exists
    if not proxies:
        print("No proxies available. Exiting...")
        return

    L = instaloader.Instaloader(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36")

    try:
        # Set initial proxy
        proxy = set_random_proxy(proxies)
        if proxy:
            L.context._session.proxies.update(proxy)
        else:
            print("No valid proxy selected. Exiting...")
            return

        profile = instaloader.Profile.from_username(L.context, username)
        post_data = []  # Collect data for the Excel file

        post_count = 0
        folder_path = f"{username}_images"
        os.makedirs(folder_path, exist_ok=True)  # Create folder for images

        for post in profile.get_posts():
            if post_count >= max_posts:
                break

            # Random delay to mimic human-like behavior
            time.sleep(random.uniform(5, 15))

            # Rotate proxy after every few posts
            if post_count % 2 == 0:
                proxy = set_random_proxy(proxies)
                L.context._session.proxies.update(proxy)

            # Download only one image from the post if available
            image_url = post.url
            image_file_path = os.path.join(folder_path, f"{post.shortcode}.jpg")
            imgage_context = ""
            try:
                img_data = requests.get(image_url).content
                with open(image_file_path, 'wb') as handler:
                    handler.write(img_data)
                imgage_context = query(image_file_path)
            except Exception as e:
                print(f"Failed to download image for post {post.shortcode}: {e}")
                continue

            # Append post data to list
            post_data.append({
                "Post URL": f"https://www.instagram.com/p/{post.shortcode}/",
                "Image Context": imgage_context[0]["generated_text"],
                "Caption": post.caption[:1000] if post.caption else "",  # Limit caption to 50 characters
                "Likes": post.likes,
                "Comments": post.comments,
                "Date": post.date.strftime("%Y-%m-%d %H:%M:%S"),
                "Image Url": post.url
            })

            post_count += 1

        # Save data to Excel
        df = pd.DataFrame(post_data)
        os.makedirs("tabular_data", exist_ok=True)
        excel_file = os.path.join("tabular_data", f"{username}_instagram_posts.xlsx")
        df.to_excel(excel_file, index=False)

        print(f"Downloaded {post_count} post data from {username}'s profile and saved data to '{excel_file}'")

        # Delete the image directory after saving Excel file
        try:
            shutil.rmtree(folder_path)
            print(f"Successfully deleted image directory: {folder_path}")
        except Exception as e:
            print(f"Error deleting image directory: {e}")

    except instaloader.exceptions.ProfileNotExistsException:
        print(f"Profile with username '{username}' does not exist on Instagram.")
    except instaloader.exceptions.ConnectionException:
        print("Network error. Please check your connection or Instagram server status.")
    except requests.exceptions.ProxyError:
        print("Failed to connect using the proxy. Exiting...")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <Instagram_username>")
    else:
        username = sys.argv[1]
        download_instagram_images(username)