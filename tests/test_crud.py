

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from backend.database import Base
from backend.crud import generate_short_code, find_available_code, create_shortened_url
from backend.models import ShortenedURL

SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


def test_generate_short_code_length():
   
    code = generate_short_code()
    assert len(code) == 6


def test_generate_short_code_alphanumeric():
   
    code = generate_short_code()
    assert code.isalnum()


def test_find_available_code_unique():
    
    db = TestingSessionLocal()
    
    code1 = find_available_code(db)
    code2 = find_available_code(db)
    
    assert code1 != code2
    db.close()


def test_create_shortened_url():
    
    db = TestingSessionLocal()
    
    url = create_shortened_url(db, "https://example.com/long/path")
    
    assert url.short_code is not None
    assert url.original_url == "https://example.com/long/path"
    assert url.click_count == 0
    
    db.close()


def test_create_shortened_url_duplicate():
    
    db = TestingSessionLocal()
    
    url1 = create_shortened_url(db, "https://example.com/test")
    url2 = create_shortened_url(db, "https://example.com/test")
    
    assert url1.short_code == url2.short_code
    
    db.close()
