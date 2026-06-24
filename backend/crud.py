import random
import string
from typing import Optional
from sqlalchemy.orm import Session

from backend.models import ShortenedURL

def generate_short_code(length: int = 6) -> str:
    chars = string.ascii_letters + string.digits
    return "".join(random.choice(chars) for _ in range(length))

def find_available_code(db: Session, length: int = 6) -> str:
    max_attempts = 10
    for _ in range(max_attempts):
        code = generate_short_code(length)
        existing = db.query(ShortenedURL).filter(ShortenedURL.short_code == code).first()
        if not existing:
            return code

    return find_available_code(db, length + 1)

def create_shortened_url(db: Session, original_url: str) -> ShortenedURL:
    existing = db.query(ShortenedURL).filter(ShortenedURL.original_url == original_url).first()
    if existing:
        return existing

    short_code = find_available_code(db)
    db_url = ShortenedURL(short_code=short_code, original_url=original_url)
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    return db_url

def get_url_by_code(db: Session, short_code: str) -> Optional[ShortenedURL]:
    url_record = db.query(ShortenedURL).filter(ShortenedURL.short_code == short_code).first()
    if url_record:
        url_record.click_count += 1
        db.commit()
    return url_record

def get_url_info(db: Session, short_code: str) -> Optional[ShortenedURL]:
    return db.query(ShortenedURL).filter(ShortenedURL.short_code == short_code).first()
