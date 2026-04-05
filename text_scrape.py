import requests
from bs4 import BeautifulSoup

print("Program started")
url="https://www.realme.com"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    text = soup.get_text(separator="\n", strip=True)

    with open("webpage_text.txt", "w", encoding="utf-8") as f:
        f.write(text)

    print("Text scraped successfully")
else:
    print("Website access failed")