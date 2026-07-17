from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_search_returns_matching_flights():
    response = client.get("/flights/search?origin=DEL&destination=BOM&date=2026-08-01")
    assert response.status_code == 200

def test_search_invalid_date_returns_400():
    response = client.get("/flights/search?origin=DEL&destination=BOM&date=notadate")
    assert response.status_code == 400