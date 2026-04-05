from bs4 import BeautifulSoup
import requests
import os
from urllib.parse import urljoin

# 🔥 USER INPUT: Change this URL anytime
url = input("Enter website URL to scrape images: ")

# Send request
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all images
images = soup.find_all('img')

# Make images folder if not exists
os.makedirs('images', exist_ok=True)

print(f"Total images found: {len(images)}")

# Scrape max 3 images
for i, img in enumerate(images):
    if i == 3:  # Limit to 3 images
        break
    src = img.get('src')
    if not src:
        continue
    full_url = urljoin(url, src)
    try:
        img_data = requests.get(full_url).content
        with open(f'images/image_{i}.jpg', 'wb') as f:
            f.write(img_data)
        print(f"Image {i} saved successfully: {full_url}")
    except Exception as e:
        print(f"Failed to download image {i}: {e}")

print("✅ Scraping completed!")