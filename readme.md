# AI Daily Digest

A Python-based project that automatically fetches the latest AI and tech news, summarizes it using **Gemini AI**, and sends daily updates directly to Telegram. The project is fully automated with **GitHub Actions**, ensuring you receive digests without manual effort.

---

## 🚀 Features

- Fetch latest articles from multiple RSS feeds
- Summarize each article using **Gemini AI**
- Store article metadata in **SQLite** to avoid duplicates
- Send each article as a Telegram message
- Fully automated daily runs using **GitHub Actions**
- Easily extendable with more RSS feeds or Telegram groups

---

## 📦 Tech Stack

- **Python 3.11**
- **feedparser** – Parse RSS feeds
- **requests** – Send messages to Telegram
- **SQLite** – Store articles
- **Gemini AI API** – Summarization
- **GitHub Actions** – Automation
- **dotenv** – Environment variable management

---

## 📋 Project Structure

```plaintext
ai-daily-digest/
│
├─ news/
│  ├─ rss_scraper.py        # Fetch articles from RSS feeds
│  └─ summarizer.py         # Summarize text using Gemini
│
├─ store/
│  └─ db.py                 # SQLite DB setup and article storage
│
├─ notifier/
│  └─ telegram_bot.py       # Send messages to Telegram
│
├─ main.py                  # Main entry point
├─ config.py                # RSS feed URLs and settings
├─ requirements.txt
└─ .github/workflows/
   └─ daily-digest.yml      # GitHub Actions workflow
```

---

## ⚡ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/ai-daily-digest.git
cd ai-daily-digest
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up environment variables

Create a `.env` file:

```env
TELEGRAM_BOT_TOKEN=your_bot_token
TELEGRAM_CHAT_ID=your_chat_id
GEMINI_API_KEY=your_gemini_api_key
```

### 4. Run locally (optional)

```bash
python main.py
```

### 5. GitHub Actions

- Daily automation is handled via `daily-digest.yml`
- You can also manually trigger the workflow from the GitHub Actions tab

---

## 🛠 Configuration

- **RSS Feeds** → Edit `config.py`
- **Telegram** → Ensure bot is started in chat or group, use numeric `chat_id`
- **Gemini AI** → Provide valid API key

---

## ✅ Project Status

- Phase 1: RSS Scraper – ✅ Complete
- Phase 2: Summarizer – ✅ Complete
- Phase 3: Database & Scheduler – ✅ Complete
- Phase 4: Telegram Integration – ✅ Complete
- Phase 5: UI – ⏸ Skipped
- Phase 6: Deployment via GitHub Actions – ✅ Complete

---

## 📌 Future Improvements

- Add web-based UI for browsing summaries
- Migrate to Render or VPS for persistent storage
- Batch multiple articles into single digest message
- Add filtering by topic or keyword

---

## 📄 License

This project is open source under the MIT License.

