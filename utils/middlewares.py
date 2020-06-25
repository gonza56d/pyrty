"""Middleware utils."""

# Pyrty
from users.forms import LoginForm


class LoginFormMiddleware:
	"""Set LoginForm available in all the requests to save from have to manually call it."""

	def __init__(self, get_response):
		self.get_response = get_response

	def __call__(self, request):
		request.login_form = LoginForm()
		return self.get_response(request)
