"""Summary report detail views."""

# Django
from django.views.generic.detail import DetailView

# Pyrty
from summaryreports.models import SummaryReport


class SummaryReportDetail(DetailView):
    """Detail view of the latest summary report for a user."""
    
    model = SummaryReport

    def get_object(self, queryset=None):
        return SummaryReport.objects.filter(user=self.request.user).latest()
