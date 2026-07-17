
# Travel Booking API

A test-first, spec-driven build of a flight booking microservice — built as a demonstration of an agentic SDLC workflow: spec → failing tests → AI-assisted implementation → code audit.

## Workflow

1. `spec/spec.md` — requirements and endpoint contracts defined before any code
2. `docs/schema.sql` and `docs/nosql_schema.md` — data layer designed before implementation
3. `tests/` — written and committed failing, before implementation existed
4. `prompt-log.md` — how implementation was directed
5. `audit-notes.md` — real bugs found while reviewing generated code, including a concurrency race condition
6. `src/main.py` — final implementation

## Endpoints

- `GET /flights/search?origin=&destination=&date=`
- `POST /bookings` — create a booking
- `GET /bookings/{id}` — get booking details
- `DELETE /bookings/{id}` — cancel a booking

## Stack

FastAPI, PyTest, Python

## Running locally

\`\`\`
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
pytest tests/
\`\`\`

## Notable finding

During implementation review, a race condition was discovered in booking creation: concurrent requests could both pass the seat-availability check before either updated the seat count, allowing overbooking. Fixed with a threading lock to make the check atomic. Full details in `audit-notes.md`.