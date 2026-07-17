from fastapi import FastAPI, HTTPException
from datetime import date as date_type

app = FastAPI()

# Temporary in-memory data (we'll replace with real DB later)
flights_db = [
    {"id": 1, "origin": "DEL", "destination": "BOM", "date": "2026-08-01", "seats_available": 5, "price": 4500},
    {"id": 2, "origin": "DEL", "destination": "BOM", "date": "2026-08-01", "seats_available": 0, "price": 4200},
]

bookings_db = []
next_booking_id = 1

@app.get("/flights/search")
def search_flights(origin: str, destination: str, date: str):
    try:
        date_type.fromisoformat(date)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format")

    results = [
        f for f in flights_db
        if f["origin"] == origin and f["destination"] == destination and f["date"] == date
    ]
    return results
from pydantic import BaseModel

class BookingRequest(BaseModel):
    flight_id: int
    user_id: int

@app.post("/bookings", status_code=201)
def create_booking(booking: BookingRequest):
    global next_booking_id

    flight = next((f for f in flights_db if f["id"] == booking.flight_id), None)
    if flight is None:
        raise HTTPException(status_code=404, detail="Flight not found")

    if flight["seats_available"] <= 0:
        raise HTTPException(status_code=409, detail="No seats available")

    flight["seats_available"] -= 1

    new_booking = {
        "id": next_booking_id,
        "flight_id": booking.flight_id,
        "user_id": booking.user_id,
        "status": "CONFIRMED",
    }
    bookings_db.append(new_booking)
    next_booking_id += 1

    return new_booking
@app.get("/bookings/{booking_id}")
def get_booking(booking_id: int):
    booking = next((b for b in bookings_db if b["id"] == booking_id), None)
    if booking is None:
        raise HTTPException(status_code=404, detail="Booking not found")
    return booking

@app.delete("/bookings/{booking_id}")
def cancel_booking(booking_id: int):
    booking = next((b for b in bookings_db if b["id"] == booking_id), None)
    if booking is None:
        raise HTTPException(status_code=404, detail="Booking not found")
    if booking["status"] == "CANCELLED":
        raise HTTPException(status_code=409, detail="Booking already cancelled")

    booking["status"] = "CANCELLED"
    return booking
