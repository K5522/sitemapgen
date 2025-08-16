from flask import Flask, request, render_template_string, send_file
import requests
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import io

app = Flask(__name__)

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

    soup = BeautifulSoup(response.text, "html.parser")
    sitemap_links.append(url)

    for link in soup.find_all("a", href=True):
        href = link.get("href")
        full_url = urljoin(url, href)
        if urlparse(full_url).netloc == domain and full_url.startswith("http"):
            if full_url not in visited:
                crawl(full_url, domain)

def generate_sitemap(start_url):
    global visited, sitemap_links
    visited, sitemap_links = set(), []

    domain = urlparse(start_url).netloc
    crawl(start_url, domain)

    urlset = ET.Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
    for link in sitemap_links:
        url_elem = ET.SubElement(urlset, "url")
        loc = ET.SubElement(url_elem, "loc")
        loc.text = link

    tree = ET.ElementTree(urlset)
    xml_bytes = io.BytesIO()
    tree.write(xml_bytes, encoding="utf-8", xml_declaration=True)
    xml_bytes.seek(0)
    return xml_bytes

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form.get("url")
        if not url.startswith("http"):
            url = "http://" + url
        sitemap_file = generate_sitemap(url)
        return send_file(
            sitemap_file,
            mimetype="application/xml",
            as_attachment=True,
            download_name="sitemap.xml"
        )
    return render_template_string("""
        <h2>Sitemap Generator</h2>
        <form method="post">
            <input type="text" name="url" placeholder="Enter website URL" size="40">
            <button type="submit">Generate Sitemap</button>
        </form>
    """)

def run():
    app.run(debug=True)
