# Travel Booking API — Spec

## Entities

### Flight
- id
- origin
- destination
- date
- seats_available
- price

### Booking
- id
- flight_id
- user_id
- status (CONFIRMED / CANCELLED)
- created_at

### SearchPreference (NoSQL)
- user_id
- preferred_time
- seat_type
- max_budget

## Endpoints

### GET /flights/search?origin=&destination=&date=
- 200 -> list of matching flights
- 400 -> invalid date format

### POST /bookings
Body: { flight_id, user_id }
- 201 -> booking created
- 404 -> flight not found
- 409 -> no seats available

### GET /bookings/{id}
- 200 -> booking details
- 404 -> booking not found

### DELETE /bookings/{id}
- 200 -> booking cancelled
- 404 -> booking not found
- 409 -> booking already cancelled