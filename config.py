import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
RSS_FEEDS = [
    # "https://www.theverge.com/rss/index.xml",
    # "https://www.technologyreview.com/feed/",
    # "https://spectrum.ieee.org/rss/fulltext",
    "https://feeds.bbci.co.uk/news/technology/rss.xml",
    "https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml",
    "https://feeds.arstechnica.com/arstechnica/technology",
    "https://www.zdnet.com/news/rss.xml",
    "https://www.cnet.com/rss/news/"
]