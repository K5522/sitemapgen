from setuptools import setup, find_packages

setup(
    name="sitemapgen",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "requests",
        "beautifulsoup4",
        "flask"
    ],
    entry_points={
        "console_scripts": [
            "sitemapgen=sitemapgen.cli:main",
            "sitemapgen-web=sitemapgen.web:run"
        ]
    },
    author="Frez Key",
    description="A simple Python Sitemap Generator (CLI + Web)",
    url="https://github.com/yourusername/sitemapgen",
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
)
