"""Notification tasks."""

# Python
from datetime import datetime, timedelta

# Celery
from celery.decorators import periodic_task

# Pyrty
from notifications.models import Notification


@periodic_task(run_every=timedelta(hours=1))
def clean_seen_notifications():
	"""
	Every hour, delete seen notifications that are equal or older than 7 days.
	"""
	interval = datetime.now() - timedelta(days=7)
	Notification.objects.filter(created__lte=interval, seen=True).delete()
