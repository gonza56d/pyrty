"""User authentication views."""

# Python
# import pdb

# Django
from django.contrib import auth, messages
from django.db import transaction
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic.edit import FormView

# Pyrty
from profiles.models import Profile
from pyrty.views import ForumList
from users.forms import LoginForm, SignUpForm, UserConfigurationsForm
from users.models import User


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
    
    def form_valid(self, form):
        user = form.save(commit=False)
        User.objects.create_user(username=user.username, email=user.email, password=user.password)
        user = User.objects.get(username=user.username)
        profile = Profile()
        profile.user = user
        profile.save()
        messages.add_message(self.request, messages.INFO, _('Account registered successfully.'))
        return super().form_valid(form)
