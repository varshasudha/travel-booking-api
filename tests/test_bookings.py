from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_create_booking_success():
    response = client.post("/bookings", json={"flight_id": 1, "user_id": 1})
    assert response.status_code == 201

def test_booking_nonexistent_flight_returns_404():
    response = client.post("/bookings", json={"flight_id": 9999, "user_id": 1})
    assert response.status_code == 404

def test_booking_fully_booked_flight_returns_409():
    response = client.post("/bookings", json={"flight_id": 2, "user_id": 1})
    assert response.status_code == 409
    