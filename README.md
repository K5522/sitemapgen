# 🗺️ Sitemap Generator

A simple Python tool to automatically generate XML sitemaps for your website by crawling all internal links.

## ✨ Features

- 🔍 **Automatic crawling** - Discovers all internal pages on your website
- 🌐 **Dual interface** - Use via command-line (CLI) or web browser
- 📄 **XML sitemap generation** - Creates standard sitemap.xml files
- ⚡ **Easy to use** - Simple installation and straightforward commands
- 🔒 **Domain restriction** - Only crawls links within your domain

## 📋 Requirements

- Python 3.6 or higher
- Internet connection (to crawl websites)

## 🚀 Installation

### Option 1: Install from source (recommended)

```bash
# Clone the repository
git clone https://github.com/K5522/sitemapgen.git
cd sitemapgen

# Install the package
pip install -e .
```

### Option 2: Install dependencies only

```bash
pip install -r requirements.txt
```

## 💻 Usage

### Command Line Interface (CLI)

The CLI mode is perfect for quick sitemap generation and automation.

**Basic usage:**

```bash
sitemapgen https://example.com
```

This will:
1. Crawl all pages starting from `https://example.com`
2. Follow all internal links within the same domain
3. Generate a `sitemap.xml` file in your current directory

**Example:**

```bash
# Generate sitemap for your website
sitemapgen https://yourdomain.com

# Output will show crawling progress:
# Crawling: https://yourdomain.com
# Crawling: https://yourdomain.com/about
# Crawling: https://yourdomain.com/contact
# ✅ Sitemap saved as sitemap.xml
```

### Web Interface

The web interface provides a user-friendly GUI in your browser.

**Start the web server:**

```bash
sitemapgen-web
```

This will start a Flask development server (default: http://127.0.0.1:5000)

**Using the web interface:**

1. Open your browser and navigate to `http://127.0.0.1:5000`
2. Enter your website URL in the input field (e.g., `example.com` or `https://example.com`)
3. Click "Generate Sitemap"
4. The sitemap.xml file will be automatically downloaded to your computer

## 📝 Understanding the Sitemap

The generated `sitemap.xml` file follows the standard sitemap protocol and looks like this:

```xml
<?xml version='1.0' encoding='utf-8'?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://yourdomain.com</loc>
  </url>
  <url>
    <loc>https://yourdomain.com/about</loc>
  </url>
  <!-- More URLs... -->
</urlset>
```

## 📤 Using Your Sitemap

Once generated, you can:

1. **Upload to your website** - Place `sitemap.xml` in your website's root directory
2. **Submit to search engines:**
   - Google Search Console: https://search.google.com/search-console
   - Bing Webmaster Tools: https://www.bing.com/webmasters
3. **Add to robots.txt** - Include the line:
   ```
   Sitemap: https://yourdomain.com/sitemap.xml
   ```

## 🔧 Troubleshooting

### "Usage: sitemapgen https://example.com" error
- Make sure to provide a URL as an argument
- URL should start with `http://` or `https://`

### No pages found or empty sitemap
- Check if the website is accessible
- Ensure the website has proper HTML links (`<a href="...">`)
- Some pages might be blocked by robots.txt or login walls

### Installation issues
- Ensure Python 3.6+ is installed: `python --version`
- Try upgrading pip: `pip install --upgrade pip`
- Install dependencies manually: `pip install requests beautifulsoup4 flask`

## 🛠️ Development

### Run from source without installing

**CLI mode:**
```bash
cd sitemapgen
python -m sitemapgen.cli https://example.com
```

**Web mode:**
```bash
cd sitemapgen
python -m sitemapgen.web
```

### Project Structure

```
sitemapgen/
├── sitemapgen/
│   ├── __init__.py
│   ├── cli.py          # Command-line interface
│   └── web.py          # Web interface (Flask)
├── setup.py            # Package configuration
├── requirements.txt    # Dependencies
├── LICENSE            # MIT License
└── README.md          # This file
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Frez Key**

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## ⚠️ Disclaimer

- This tool is for generating sitemaps for websites you own or have permission to crawl
- Be respectful of server resources and avoid aggressive crawling
- Some websites may block automated crawlers
- The tool respects HTTP timeouts but doesn't check robots.txt

## 📚 Additional Resources

- [Sitemap Protocol](https://www.sitemaps.org/protocol.html)
- [Google Search Console](https://search.google.com/search-console)
- [XML Sitemaps Guide](https://developers.google.com/search/docs/crawling-indexing/sitemaps/overview)

---

**Need help?** Open an issue on GitHub or check the troubleshooting section above.
