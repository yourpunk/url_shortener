from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from backend.main import app, get_db
from backend.database import Base

SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


def test_health_check():
    
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_shorten_url():
    
    response = client.post(
        "/api/shorten",
        json={"url": "https://example.com/very/long/path"},
    )
    assert response.status_code == 200
    data = response.json()
    assert "short_code" in data
    assert "short_url" in data
    assert len(data["short_code"]) == 6


def test_shorten_url_invalid():
    
    response = client.post(
        "/api/shorten",
        json={"url": "not a valid url"},
    )
    assert response.status_code == 422


def test_redirect():
    
    shorten_response = client.post(
        "/api/shorten",
        json={"url": "https://example.com/test"},
    )
    short_code = shorten_response.json()["short_code"]

    response = client.get(f"/{short_code}", follow_redirects=False)
    assert response.status_code == 301
    assert response.headers["location"] == "https://example.com/test"


def test_redirect_not_found():
    
    response = client.get("/nonexistent", follow_redirects=False)
    assert response.status_code == 404


def test_get_info():
    
    shorten_response = client.post(
        "/api/shorten",
        json={"url": "https://example.com/info-test"},
    )
    short_code = shorten_response.json()["short_code"]

    
    client.get(f"/{short_code}", follow_redirects=False)
    client.get(f"/{short_code}", follow_redirects=False)

    info_response = client.get(f"/api/info/{short_code}")
    assert info_response.status_code == 200
    data = info_response.json()
    assert data["short_code"] == short_code
    assert data["click_count"] == 2
