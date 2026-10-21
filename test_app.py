import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    """Test the root endpoint status code and response body."""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello, World!" in response.data

def test_health_check(client):
    """Test the /health endpoint returns HTTP 200 and JSON with status healthy."""
    response = client.get("/health")
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data["status"] == "healthy"
    assert "running smoothly" in json_data["message"]
