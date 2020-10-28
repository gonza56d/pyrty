"""Periodic notification tasks."""

# Python
from datetime import datetime, timedelta

# Celery
from celery.decorators import periodic_task

# Pyrty
from notifications.models import Notification


@periodic_task(run_every=timedelta(hours=1))
def clean_seen_notifications():
	""" Every hour, delete seen notifications that are older 31 days.

	Added one more day than a month in order to save the data for
	users that have monthly summary report.
	"""
	interval = datetime.now() - timedelta(days=31)
	Notification.objects.filter(created__lt=interval, seen=True).delete()
