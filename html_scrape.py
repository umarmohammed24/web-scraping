import requests
from bs4 import BeautifulSoup

print("HTML scraping started")

url="https://www.realme.com"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    with open("scraped_page.html", "w", encoding="utf-8") as f:
        f.write(str(soup))

    print("HTML saved successfully")
else:
    print("Failed to fetch website", response.status_code)