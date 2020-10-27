"""Comment notification views."""

# Django
from django.urls import reverse

# Pyrty
from notifications.models import Notification
from users.models import User


def create_notification(request, form):
	"""Create a new notification for the post's author about new comment."""
	# validate comment user is not the same than post user
	post = form.cleaned_data.get('post')
	if request.user != User.objects.get(pk=post.user.id):
		notification = Notification()
		notification.origin_user = request.user
		notification.target_user = User.objects.get(pk=post.user.id)
		notification.message = "{} commented in your post: '{}'".format(request.user, post.title)
		notification.url = reverse('post', args=[post.id])
		notification.save()
