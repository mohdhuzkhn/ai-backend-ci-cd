from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "online", "service": "AI Backend"}


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert "postgres_configured" in response.json()
