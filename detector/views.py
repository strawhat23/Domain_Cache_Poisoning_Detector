# -*- coding: utf-8 -*-
# @Author: MAYUR / GPT
# @Date:   2025-10-22
# @Description: Handles dashboard, API, and PDF report generation.

import os
import json
import datetime
from django.http import JsonResponse, FileResponse, Http404
from django.shortcuts import render
from django.conf import settings

# ================= PATHS =================
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = os.path.join(BASE_DIR, "data", "detections.json")
REPORTS_DIR = os.path.join(BASE_DIR, "reports")

os.makedirs(REPORTS_DIR, exist_ok=True)


# ================= INDEX PAGE =================
def index(request):
    """
    Loads the latest detection events and renders the dashboard.
    """
    detections = []
    try:
        with open(DATA_FILE, 'r') as f:
            detections = json.load(f)
    except Exception:
        detections = []

    context = {
        'detections': list(reversed(detections))[:100],  # Show latest 100 only
    }
    return render(request, 'detector/index.html', context)


# ================= LIVE API (AJAX/POLLING) =================
def api_latest(request):
    """
    Returns the latest detections in JSON for live chart updates.
    """
    try:
        with open(DATA_FILE, 'r') as f:
            detections = json.load(f)
    except Exception:
        detections = []

    latest = detections[-50:]  # Limit for frontend speed
    return JsonResponse({
        'status': 'ok',
        'count': len(latest),
        'detections': latest
    })


# ================= REPORT DOWNLOAD =================
def download_report(request, filename):
    """
    Lets the user download a generated PDF report.
    """
    path = os.path.join(REPORTS_DIR, filename)
    if not os.path.exists(path):
        raise Http404("Report not found")
    return FileResponse(open(path, 'rb'), as_attachment=True, filename=filename)


# ================= REPORT GENERATION =================
def generate_report(request):
    """
    Generates a summary PDF report of recent detections.
    """
    try:
        from reportlab.lib.pagesizes import letter
        from reportlab.pdfgen import canvas
    except ImportError:
        return JsonResponse({'status': 'error', 'message': 'reportlab not installed'})

    # Load detections
    try:
        with open(DATA_FILE, 'r') as f:
            detections = json.load(f)
    except Exception:
        detections = []

    timestamp = datetime.datetime.utcnow().strftime('%Y%m%d_%H%M%S')
    filename = f'report_{timestamp}.pdf'
    path = os.path.join(REPORTS_DIR, filename)

    c = canvas.Canvas(path, pagesize=letter)
    c.setFont('Helvetica-Bold', 14)
    c.drawString(40, 750, 'Domain Cache Poisoning Detector Report')
    c.setFont('Helvetica', 10)
    c.drawString(40, 735, f"Generated on: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    c.line(40, 730, 570, 730)

    y = 710
    if not detections:
        c.drawString(40, y, 'No detections found.')
    else:
        for det in detections[-30:][::-1]:  # last 30 records
            entry = f"[{det.get('time','')}] {det.get('domain')} | DNSSEC={det.get('dnssec_score')} | Level={det.get('alert_level')}"
            c.drawString(40, y, entry)
            y -= 14
            if y < 60:
                c.showPage()
                y = 750

    c.save()
    return JsonResponse({'status': 'ok', 'filename': filename})
