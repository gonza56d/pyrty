"""Summary report periodic tasks."""

# Python
from datetime import datetime, timedelta

# Celery
from celery.decorators import periodic_task
from celery.schedules import crontab

# Pyrty
from summaryreports.views import create_summary_report
from users.models import User


@periodic_task(run_every=crontab(hour=17, minute=0))
def send_daily_summary_report():
	"""
	Run every day.
	"""
	interval = datetime.now() - timedelta(hours=24)
	users = User.objects.filter(summary_reports='D')
	for user in users:
		create_summary_report(user, interval)


@periodic_task(run_every=crontab(hour=17, minute=0, day_of_week=5))
def send_weekly_summary_report():
	"""
	Run every friday.
	"""
	interval = datetime.now() - timedelta(hours=168)
	users = User.objects.filter(summary_reports='W')
	for user in users:
		create_summary_report(user, interval)


@periodic_task(run_every=crontab(hour=17, minute=0, day_of_month=1))
def send_monthly_summary_report():
	"""
	Run every 1st of each month.
	"""
	today = datetime.now()
	interval = datetime.now() - today.replace(month=today.month-1)
	users = User.objects.filter(summary_reports='M')
	for user in users:
		create_summary_report(user, interval)
