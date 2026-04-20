# -*- coding: utf-8 -*-
# @Author: Your name
# @Date:   2025-10-22 09:55:40
# @Last Modified by:   Your name
# @Last Modified time: 2025-10-22 21:16:49
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('api/detections/latest', views.api_latest, name='api_latest'),
    path('report/download/<str:filename>', views.download_report, name='download_report'),
    path('report/generate', views.generate_report, name='generate_report'),
]
