import sqlite3
from store.db import init_db, save_article, is_article_saved

def test_db_insert_and_check(tmp_path):
    db_file = tmp_path / "test.db"
    init_db(db_file)

    article = {"title": "Test", "link": "http://test.com", "summary": "Summary", "published": "Today"}
    save_article(article, db_file)

    assert is_article_saved("http://test.com", db_file) is True

    # Also verify it exists in raw DB
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("SELECT title, link FROM articles WHERE link = ?", ("http://test.com",))
    row = cursor.fetchone()
    conn.close()

    assert row is not None
    assert row[0] == "Test"
    assert row[1] == "http://test.com"
