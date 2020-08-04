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

	def get_context_data(self, **kwargs):
		context = super(NotificationList, self).get_context_data(**kwargs)
		count = Notification.objects.filter(target_user=self.request.user).count()
		page = self.kwargs['page']
		if page < 1:
			page = 1
		context['page'] = page
		context['count'] = count
		context['offset'] = page * 10
		context['previous_offset'] = page * 10 - 10
		context['next_offset'] = page * 10 + 10
		return context

	def get_queryset(self, queryset=None):
		offset = self.kwargs['page'] - 1
		if offset < 0:
			offset = 0
		return Notification.objects.filter(target_user=self.request.user)[offset:10]


def update_notifications(request):
	if request.method == 'POST':
		n = Notification.objects.filter(target_user=request.user).update(seen=True)
		return JsonResponse({'status': 200, 'message': str(n)+' notifications updated'})
