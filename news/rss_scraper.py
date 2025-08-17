import feedparser

def fetch_articles(feeds, max_per_feed=3):
    articles = []
    for url in feeds:
        feed = feedparser.parse(url)
        for entry in feed.entries[:max_per_feed]:
            articles.append({
                "title": entry.title,
                "link": entry.link,
                "summary": entry.get("summary", ""),
                "published": entry.get("published", "")
            })
    return articles
