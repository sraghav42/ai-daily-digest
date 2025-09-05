import feedparser
from news.rss_scraper import fetch_articles

class FakeEntry:
    def __init__(self):
        self.title = "Test Article"
        self.link = "http://test.com"
        self.summary = "Summary here"
        self.published = "Today"

    def get(self, key, default=None):
        return getattr(self, key, default)

class FakeFeed:
    def __init__(self):
        self.entries = [FakeEntry()]

def test_fetch_articles(monkeypatch):
    monkeypatch.setattr(feedparser, "parse", lambda url: FakeFeed())
    articles = fetch_articles(["http://fake-url.com"])
    
    assert len(articles) == 1
    assert articles[0]["title"] == "Test Article"
    assert articles[0]["link"] == "http://test.com"
    assert "Summary" in articles[0]["summary"]
