"""Summary report create views."""

# Django
from django.db.models import Exists, OuterRef, Q
from django.shortcuts import reverse

# Pyrty
from comments.models import Comment
from notifications.models import Notification
from privatemessages.models import PrivateMessage
from posts.models import Post
from summaryreports.models import SummaryReport


def create_summary_report(user, interval):
    """Create a report with statistics for a user regarding the period
    of time received as interval."""
    
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
    create_notification(user)


def create_notification(user):
    """Notify a user about its new summary report."""

    notification = Notification()
    notification.target_user = user
    sr = ''
    if user.summary_reports == 'D':
        sr = 'Your daily summary report is here.'
    elif user.summary_reports == 'W':
        sr = 'Your weekly summary report is here.'
    elif user.summary_reports == 'M':
        sr = 'Your monthly summary report is here.'
    notification.message = sr
    notification.url = reverse('summary_report')
    notification.save()
