"""Summary report create views."""

# Django
from django.db.models import Exists, OuterRef, Q

# Pyrty
from comments.models import Comment
from notifications.models import Notification
from privatemessages.models import PrivateMessage
from posts.models import Post
from summaryreports.models import SummaryReport


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
