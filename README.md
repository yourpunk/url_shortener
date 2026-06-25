# URL Shortener

[![Tests](https://github.com/yourpunk/url_shortener/actions/workflows/tests.yml/badge.svg)](https://github.com/yourpunk/url_shortener/actions/workflows/tests.yml)

Fast and simple URL shortening service built with FastAPI. Live demo: [your-app.onrender.com](https://url-shortener-5aqz.onrender.com)

## Preview

![URL Shortener preview](docs/preview.png)

## Features

- Shorten long URLs into short, shareable codes
- Redirect to original URL via short link
- Click statistics for each shortened link
- Simple web interface, no sign-up required
- Deployed and live on Render

## Tech Stack

- **Backend:** FastAPI, SQLAlchemy, Pydantic
- **Database:** SQLite
- **Frontend:** HTML, CSS, vanilla JavaScript
- **Testing:** Pytest
- **CI/CD:** GitHub Actions
- **Deployment:** Render

## Project Structure

```
url_shortener/
├── backend/
│   ├── app/ (или прямо в backend/, уточни свою структуру)
│   │   ├── crud.py       
│   │   ├── database.py   
│   │   ├── main.py       
│   │   ├── models.py     
│   │   └── schemas.py    
│   └── requirements.txt
├── frontend/
│   └── index.html
├── tests/
│   ├── test_api.py
│   └── test_crud.py
├── .github/workflows/tests.yml
├── .gitignore
└── README.md
```

## Installation

```bash
git clone https://github.com/yourpunk/url_shortener.git
cd url_shortener

python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS/Linux

pip install -r backend/requirements.txt
```

## Running Locally

```bash
uvicorn backend.main:app --reload
```

Visit `http://localhost:8000`

## Testing

```bash
pytest -v
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/shorten` | Shorten a URL |
| `GET` | `/{short_code}` | Redirect to original URL |
| `GET` | `/api/info/{short_code}` | Get stats (clicks, created date) |
| `GET` | `/health` | Health check |

### Example

```bash
curl -X POST https://your-app.onrender.com/api/shorten \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com/very/long/path"}'
```

## Deployment

Deployed on [Render](https://render.com) using:
- **Build Command:** `pip install -r backend/requirements.txt`
- **Start Command:** `uvicorn backend.main:app --host 0.0.0.0 --port $PORT`
- **Environment Variable:** `BASE_URL=https://your-app.onrender.com`

> **Note:** This runs on Render's free tier, which spins down after inactivity. The first request after idle time may take 30-60 seconds to respond.