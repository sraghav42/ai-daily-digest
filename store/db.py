import sqlite3
from datetime import datetime

DB_PATH = "digest.db"

def init_db(db_file=DB_PATH):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS articles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            link TEXT UNIQUE,
            summary TEXT,
            published TEXT,
            created_at TEXT
        );
    """)
    conn.commit()
    conn.close()

def save_article(article,db_file=DB_PATH):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO articles (title, link, summary, published, created_at)
            VALUES (?, ?, ?, ?, ?)
        """, (
            article['title'],
            article['link'],
            article['summary'],
            article['published'],
            datetime.now().isoformat()
        ))
        conn.commit()
    except sqlite3.IntegrityError:
        # Article already saved
        pass
    finally:
        conn.close()

def is_article_saved(link,db_file=DB_PATH):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("SELECT 1 FROM articles WHERE link = ?", (link,))
    result = cursor.fetchone()
    conn.close()
    return result is not None

def print_all_articles():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT title, link, published, created_at FROM articles ORDER BY created_at DESC")
    rows = cursor.fetchall()
    conn.close()

    for row in rows:
        print(f"📰 {row[0]}\n🔗 {row[1]}\n📅 Published: {row[2]} | Saved: {row[3]}\n---")