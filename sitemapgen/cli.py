import requests
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import sys

visited = set()
sitemap_links = []

def crawl(url, domain):
    if url in visited:
        return
    visited.add(url)

    try:
        response = requests.get(url, timeout=5)
        if response.status_code != 200:
            return
    except Exception:
        return

    print(f"Crawling: {url}")
    soup = BeautifulSoup(response.text, "html.parser")
    sitemap_links.append(url)

    for link in soup.find_all("a", href=True):
        href = link.get("href")
        full_url = urljoin(url, href)
        if urlparse(full_url).netloc == domain and full_url.startswith("http"):
            if full_url not in visited:
                crawl(full_url, domain)

def generate_sitemap(domain, start_url):
    crawl(start_url, domain)

    urlset = ET.Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
    for link in sitemap_links:
        url_elem = ET.SubElement(urlset, "url")
        loc = ET.SubElement(url_elem, "loc")
        loc.text = link

    tree = ET.ElementTree(urlset)
    tree.write("sitemap.xml", encoding="utf-8", xml_declaration=True)
    print("✅ Sitemap saved as sitemap.xml")

def main():
    if len(sys.argv) != 2:
        print("Usage: sitemapgen https://example.com")
        sys.exit(1)

    start_url = sys.argv[1]
    domain = urlparse(start_url).netloc
    generate_sitemap(domain, start_url)
