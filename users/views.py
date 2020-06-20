"""Users view."""

# Python
# import pdb

# Django
from django.contrib import auth
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

# Pyrty
from pyrty.views import ForumList
from users.forms import LoginForm, SignUpForm


def login_view(request):
	"""Handle login request."""
	if request.method == "POST":
		form = LoginForm(data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = auth.authenticate(username=username, password=password)
			if user is not None:
				auth.login(request, user)
			return redirect('forums')


def logout_view(request):
	"""Handle logout request."""
	auth.logout(request)
	return redirect('forums')


class SignUp(FormView):
	"""Common users sign up view."""

	template_name = 'users/signup.html'
	form_class = SignUpForm
	success_url = reverse_lazy('forums')

	def forum_valid(self, form):
		#  form.save() TODO
		return super().form_valid(form)
