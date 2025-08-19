#from apscheduler.schedulers.blocking import BlockingScheduler
from news.rss_scraper import fetch_articles
from news.summarizer import summarize_text
from config import RSS_FEEDS
from store.db import init_db, save_article, is_article_saved, print_all_articles
from notifier.telegram_bot import send_to_telegram

def job():
    print("Running daily AI digest job...")
    init_db()
    articles = fetch_articles(RSS_FEEDS, max_per_feed=1)

    for article in articles:
        if is_article_saved(article['link']):
            continue  # skip duplicates
        print(f"📰 {article['title']}")
        print(f"🔗 {article['link']}")
        print("🧠 Summary:")
        summary = summarize_text(article['summary'] or article['title'])
        print(summary)
        print("-" * 60)

        article['summary'] = summary
        save_article(article)
        msg = f"📰 {article['title']}\n🔗 {article['link']}\n🧠 {summary}"
        send_to_telegram(msg)

if __name__ == "__main__":
    #print_all_articles()
    job()  
    # scheduler = BlockingScheduler()
    # Run every day at 9 AM
    # scheduler.add_job(job, 'cron', hour=9, minute=0)

    # For testing: uncomment below to run every 1 minute
    # scheduler.add_job(job, 'interval', minutes=1)

    # print("Scheduler started. Waiting for the next run...")
    # scheduler.start()