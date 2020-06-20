"""Middleware utils."""

# Pyrty
from users.forms import LoginForm


class LoginFormMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
    	login_form = LoginForm()
    	request.login_form = login_form
    	return self.get_response(request)