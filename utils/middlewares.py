"""Middleware utils."""

# Python
# import pdb

# Pyrty
from notifications.models import Notification
from privatemessages.models import PrivateMessage
from users.forms import LoginForm


class LoginFormMiddleware:
	"""Set LoginForm available in all the requests to save from have to manually call it."""

	def __init__(self, get_response):
		self.get_response = get_response

	def __call__(self, request):
		request.login_form = LoginForm()
		return self.get_response(request)


class NotificationMiddleware:
	"""Perform a query for notifications for the user."""

	def __init__(self, get_response):
		self.get_response = get_response

	def __call__(self, request):
		if request.user.is_authenticated:  # AnnonymousUser is not iterable therefore we need to check if it is authenticated.
			request.non_seen_notifs = Notification.objects.filter(target_user=request.user, seen=False).exists()
			request.notifications = Notification.objects.filter(target_user=request.user)
		return self.get_response(request)


class PrivateMessageMiddleware:
	"""Perform a query for notifications for the user."""

	def __init__(self, get_response):
		self.get_response = get_response

	def __call__(self, request):
		if request.user.is_authenticated:
			request.non_read_msgs = PrivateMessage.objects.filter(target_user=request.user, seen=False).exists()
			request.messages = PrivateMessage.objects.filter(target_user=request.user)
		return self.get_response(request)
