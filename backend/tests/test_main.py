from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_mock_flights():
    response = client.get("/api/flights/mock")

    assert response.status_code == 200

    data = response.json()

    assert "timestamp" in data
    assert "flights" in data
    assert len(data["flights"]) > 0
