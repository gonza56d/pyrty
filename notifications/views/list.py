"""Notification list views."""

# Django
from django.views.generic import ListView

# Pyrty
from notifications.models import Notification


class NotificationList(ListView):
	"""List notifications where target user is request.user."""

	model = Notification
	paginate_by = 10

	def get_queryset(self, queryset=None):
		"""Get list of notifications with pagination."""
		return Notification.objects.filter(target_user=self.request.user)
