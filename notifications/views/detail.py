"""Notification detail views."""

# Django
from django.shortcuts import redirect

# Pyrty
from notifications.models import Notification


def get_notification(request, pk):
    """Get notification by pk, update to seen=True and redirect to notification url."""
    n = Notification.objects.filter(pk=pk)
    n.update(seen=True)
    return redirect(n[0].url)
