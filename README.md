# Odibets Scraper (Docker + Supabase)

## 📦 Features
- Scrapes Odibets match odds, results, standings
- Schedules tasks (match: hourly, results: every 2 min)
- Retries failed jobs up to 4 times
- Sends email alerts on repeated failure
- Saves data to Supabase PostgreSQL
- Docker-ready, deployable via Render

## 🚀 Setup

### 1. Clone and Install
```bash
git clone https://github.com/youruser/odibets_scraper.git
cd odibets_scraper
pip install -r requirements.txt
```

### 2. Create `.env`
```bash
cp .env.example .env
# Fill your Supabase + Email credentials
```

### 3. Run Locally
```bash
python main.py
```

### 4. Run with Docker
```bash
docker build -t odibets-scraper .
docker run -d --env-file .env odibets-scraper
```

### 5. Deploy on Render
- Push to GitHub
- Create new Web Service on [Render](https://render.com/)
- Use Docker tab and link repo
- Add environment variables in Settings

✅ Done!