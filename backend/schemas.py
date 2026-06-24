from pydantic import BaseModel, HttpUrl
from datetime import datetime

class URLShortenRequest(BaseModel):
    url: HttpUrl

class URLShortenResponse(BaseModel):
    short_code: str
    short_url: str
    original_url: str

class URLInfoResponse(BaseModel):
    short_code: str
    original_url: str
    created_at: datetime
    click_count: int

    class Config:
        from_attributes = True
        