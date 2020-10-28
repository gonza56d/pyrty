"""Notification views."""

# Python
# import pdb

# Django
from django.http import JsonResponse

# Pyrty
from notifications.models import Notification



def update_notifications(request):
	"""Set notifications to seen=True."""

	if request.method == 'POST':
		n = Notification.objects.filter(target_user=request.user).update(seen=True)
		return JsonResponse({'status': 200, 'message': str(n)+' notifications updated'})
