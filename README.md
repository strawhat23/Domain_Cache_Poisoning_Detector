Domain Cache Detector - Django Edition
=====================================

Features added:
- Django-based dashboard (no database required).
- Live updates on dashboard via AJAX polling (/api/detections/latest).
- Detection simulation improved using dnspython-style checks (realistic heuristics).
- Generated reports are displayed on the dashboard and downloadable as PDF.
- Attractive UI using Bootstrap and Chart.js.
- All detections stored in `data/detections.json` and reports in `reports/`.

Quick start (Linux / macOS / WSL / Windows with Python 3.10+):
1. Create and activate a virtualenv:
   python -m venv venv
   source venv/bin/activate   # or venv\Scripts\activate on Windows
2. Install requirements:
   pip install -r requirements.txt
3. Run the background detector (in a separate terminal):
   python detector_worker.py
4. Start Django dev server:
   python manage.py runserver
5. Open http://127.0.0.1:8000 in your browser.

Notes:
- The detector_worker simulates/queries DNS using dnspython. If you prefer full offline simulation, the worker will still generate realistic events.
- Reports are saved under reports/ and can be downloaded from the dashboard.
