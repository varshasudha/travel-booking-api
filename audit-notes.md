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