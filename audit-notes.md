# Audit Notes

## Entry 1 — pytest import path issue
- Symptom: `ModuleNotFoundError: No module named 'src'` even though src/main.py existed and had correct content.
- Root cause: pytest wasn't adding the project root to sys.path automatically on this setup.
- Fix: added pytest.ini with `pythonpath = .` so pytest always resolves imports from the project root.
- Lesson: don't assume code is broken just because a test fails — check the environment/tooling first. 