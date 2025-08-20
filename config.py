import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
RSS_FEEDS = [
    "https://feeds.bbci.co.uk/news/technology/rss.xml",
    "https://www.cnet.com/rss/news/",
    "https://www.engadget.com/rss.xml",
    "https://www.techradar.com/rss",
    "https://www.npr.org/rss/rss.php?id=1019"
]