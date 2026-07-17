# Audit Notes

## Entry 1 — pytest import path issue
- Symptom: `ModuleNotFoundError: No module named 'src'` even though src/main.py existed and had correct content.
- Root cause: pytest wasn't adding the project root to sys.path automatically on this setup.
- Fix: added pytest.ini with `pythonpath = .` so pytest always resolves imports from the project root.
- Lesson: don't assume code is broken just because a test fails — check the environment/tooling first. 
## Entry 2 — missing endpoint implementation
- Symptom: GET /bookings/{id} and DELETE /bookings/{id} both returned 404 even for valid, just-created bookings.
- Root cause: the two route functions were never actually saved into src/main.py — a copy-paste step was missed, so the routes didn't exist at all.
- Fix: re-added get_booking and cancel_booking functions to src/main.py.
- Lesson: a 404 doesn't always mean "not found in data" — first confirm the route/function exists at all before debugging data logic.

## Entry 3 — race condition in booking creation
- Symptom: under concurrent requests, two users could both book the last available seat on a flight, causing seats_available to go negative and creating an invalid double-booking.
- Root cause: the "check seats available" and "decrement seat count" steps were not atomic — two simultaneous requests could both pass the check before either updated the count.
- Fix: wrapped the check-and-decrement logic in a threading.Lock() so only one request can execute that critical section at a time.
- Lesson: sequential tests won't catch concurrency bugs. Race conditions need to be reasoned about explicitly, not just tested with normal one-at-a-time requests.