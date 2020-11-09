"""Summary report urls."""

# Django
from django.urls import path

# Pyrty
from summaryreports.views import SummaryReportDetail


urlpatterns = [
    path('detail/', SummaryReportDetail.as_view(), name='summary_report'),
]
