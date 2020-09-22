"""User tasks."""

# Python
from datetime import datetime, timedelta

# Django
from django.db.models import Exists, OuterRef, Q

# Celery
from celery.decorators import periodic_task
from celery.schedules import crontab

# Pyrty
from comments.models import Comment
from notifications.models import Notification
from privatemessages.models import PrivateMessage
from posts.models import Post
from summaryreports.models import SummaryReport
from users.models import User


def create_summary_report(user, interval):
	sr = SummaryReport()
	sr.user = user

	sr.posts_made = Post.objects.filter(user=user, created__gte=interval).count()
	sr.comments_made = Comment.objects.filter(user=user, created__gte=interval).count()
	sr.comments_received = Comment.objects.filter(
		~Q(user=user),
		Exists(Post.objects.filter(id=OuterRef('post_id'), user=user)),
		created__gte=interval
	).count()
	sr.messages_sent = PrivateMessage.objects.filter(origin_user=user, created__gte=interval).count()
	sr.messages_received = PrivateMessage.objects.filter(target_user=user, created__gte=interval).count()
	sr.notifications = Notification.objects.filter(target_user=user, created__gte=interval).count()
	sr.save()


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
