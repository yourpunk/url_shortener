from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, func
from backend.database import Base

class ShortenedURL(Base):
    __tablename__ = "shortened_urls"

    id = Column(Integer, primary_key=True, index=True)
    short_code = Column(String(10), unique=True, index=True, nullable=False)
    original_url = Column(String(2048), nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    click_count = Column(Integer, default=0)

    def __repr__(self):
        return f"<Shortened {self.short_code} -> {self.original_url}"