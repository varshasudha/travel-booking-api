# Prompt Log

This log documents how AI assistance was used to build this project, following a test-first, spec-driven workflow.

## Session 1 — Spec and schema design
- Defined entities and endpoints in spec/spec.md before any code was written
- Designed SQL schema (flights, bookings) and NoSQL document shape (search_preferences)

## Session 2 — Test-first flight search
- Wrote failing tests for GET /flights/search before implementation existed
- Prompted implementation of the endpoint to satisfy the tests
- Verified tests passed after implementation

## Session 3 — Test-first booking creation
- Wrote failing tests for POST /bookings (success, 404, 409 cases)
- Implemented booking creation logic
- Audited the implementation and found a race condition: concurrent requests could double-book the last seat on a flight
- Fixed using a threading lock to make the check-and-decrement atomic
- Documented the bug and fix in audit-notes.md

## Session 4 — Test-first get/cancel booking
- Wrote failing tests for GET /bookings/{id} and DELETE /bookings/{id}
- Found that the implementation was missing entirely on first pass, causing false 404s despite valid data
- Re-implemented both endpoints and confirmed all 10 tests passed