"""Notification views."""

# Python
# import pdb

# Django
from django.http import JsonResponse
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


def update_notifications(request):
	"""Set notifications to seen=True."""

	if request.method == 'POST':
		n = Notification.objects.filter(target_user=request.user).update(seen=True)
		return JsonResponse({'status': 200, 'message': str(n)+' notifications updated'})
