import os

from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, RedirectResponse
from sqlalchemy.orm import Session
from pathlib import Path

from backend.database import engine, get_db, Base
from backend.schemas import URLShortenResponse, URLShortenRequest, URLInfoResponse
from backend.crud import create_shortened_url, get_url_by_code, get_url_info

Base.metadata.create_all(bind=engine)

app = FastAPI(title="URL Shortener", description="Simple URL shortening service", version="1.0.0")

BASE_URL = os.getenv("BASE_URL", "http://localhost:8000")

static_dir = Path(__file__).parent.parent / "frontend"
if static_dir.exists():
    app.mount("/static", StaticFiles(directory=static_dir), name="static")

@app.get("/", include_in_schema=False)
async def root():
    return FileResponse(static_dir / "index.html", media_type="text/html")

@app.post("/api/shorten", response_model=URLShortenResponse)
def shorten_url(
    request: URLShortenRequest,
    db: Session = Depends(get_db),
):
    original_url = str(request.url)
    
    db_url = create_shortened_url(db, original_url)

    return URLShortenResponse(
        short_code=db_url.short_code,
        short_url=f"{BASE_URL}/{db_url.short_code}",
        original_url=original_url,
    )




@app.get("/api/info/{short_code}", response_model=URLInfoResponse)
def get_info(short_code: str, db: Session = Depends(get_db)):
    url_record = get_url_info(db, short_code)

    if not url_record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Short code '{short_code}' not found",
        )

    return URLInfoResponse.model_validate(url_record)


@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/{short_code}", include_in_schema=False)
def redirect_to_original(short_code: str, db: Session = Depends(get_db)):
    url_record = get_url_by_code(db, short_code)

    if not url_record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Short code '{short_code}' not found",
        )

    return RedirectResponse(url=url_record.original_url, status_code=301)
