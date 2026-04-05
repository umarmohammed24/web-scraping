import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def scrape_website(url):
    """
    Scrapes the given URL for title, text content, and images.
    """
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
        response = requests.get(url, headers=headers, timeout=10,verify=False)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract Title
        title = soup.title.string.strip() if soup.title else "No Title Found"

        # Extract Text (First 500 characters to avoid clutter)
        text = soup.get_text(separator=' ', strip=True)
        text_snippet = text[:1000] + "..." if len(text) > 1000 else text

        # Extract Images (Limit to 5)
        images = []
        img_tags = soup.find_all('img')
        for img in img_tags:
            if len(images) >= 6:
                break
            src = img.get('src')
            if src:
                full_url = urljoin(url, src)
                if full_url.startswith('http'):
                    images.append(full_url)

        return {
            'url': url,
            'title': title,
            'text': text_snippet,
            'images': images,
            'html': soup.prettify()
        }

    except requests.exceptions.RequestException as e:
        raise Exception(f"Failed to fetch URL: {str(e)}")
    except Exception as e:
        raise Exception(f"Scraping error: {str(e)}")
