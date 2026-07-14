# 🌐🔗 URL Shortener

[![Tests](https://github.com/yourpunk/url_shortener/actions/workflows/tests.yml/badge.svg)](https://github.com/yourpunk/url_shortener/actions/workflows/tests.yml)

Fast and simple **URL** shortening service built with FastAPI. *Live demo*: [url-shortener.onrender.com](https://url-shortener-5aqz.onrender.com)

> **Note:** This runs on Render's free tier, which spins down after inactivity. The first request after idle time may take 30-60 seconds to respond.

## Preview

<img width="410" height="283" alt="Screenshot_2" src="https://github.com/user-attachments/assets/9c29add5-3949-403c-b1cd-dc9e364c05cb" />
<br>
<img width="410" height="567" alt="Screenshot_3" src="https://github.com/user-attachments/assets/ddea1d9a-16b6-4baf-bd3e-8d5adb6ff0d5" />


## Features

- Shorten long URLs into short, shareable codes
- Redirect to original URL via short link
- Simple web interface, no sign-up required
- Deployed and live on **Render**

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
│   ├── __init__.py
│   ├── crud.py       
│   ├── database.py   
│   ├── main.py       
│   ├── models.py     
│   ├── schemas.py    
├── frontend/
│   └── index.html
├── tests/
│   ├── __init__.py
│   ├── test_api.py
│   └── test_crud.py
├── .github/workflows/tests.yml
├── .gitignore
├── requirements.txt
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

*Visit `http://localhost:8000`*

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

## 👤 Author
🦾 Crafted by Aleksandra Kenig (aka [yourpunk](https://github.com/yourpunk)).<br>
💌 Wanna collab or throw some feedback? You know where to find me.
