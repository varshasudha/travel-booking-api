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