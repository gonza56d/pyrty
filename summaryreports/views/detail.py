"""Summary report detail views."""

# Django
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
from django.views.generic.detail import DetailView

# Pyrty
from summaryreports.models import SummaryReport


class SummaryReportDetail(DetailView):
    """Detail view of the latest summary report for a user."""
    
    model = SummaryReport

    def get_object(self, queryset=None):
        return SummaryReport.objects.filter(user=self.request.user).latest()

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except ObjectDoesNotExist:
            return redirect('forums')
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)
