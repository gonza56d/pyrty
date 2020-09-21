"""Profile views."""

# Python
# import pdb

# Django
from django import forms
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView

# Pyrty
from comments.models import Comment
from posts.models import Post
from privatemessages.forms import PrivateMessageForm
from profiles.models import Profile
from users.forms import UserConfigurationsForm
from users.models import User


class ProfileDetailView(DetailView):
	"""Display third users' profile info."""

	model = Profile

	def get_object(self, queryset=None):
		"""Override to select related user."""

		return Profile.objects.select_related('user').get(
			slug=self.kwargs.get(self.slug_url_kwarg)
		)

	def get(self, request, *args, **kwargs):
		"""Redirect to ProfileUpdateView if the requested profile is the same than request.user."""
		user = None
		try:
			user = User.objects.get(username=self.kwargs['slug'])
		finally:
			if request.user == user:
				return redirect('self_profile', slug=self.kwargs['slug'])
			self.object = self.get_object()
			context = self.get_context_data(object=self.object)
			return self.render_to_response(context)

	def get_context_data(self, **kwargs):
		"""Load private message form, and profile's last posts and comments."""

		context = super().get_context_data(**kwargs)
		context['private_message_form'] = PrivateMessageForm(
			target_user=User.objects.get(username=self.kwargs['slug'])
		)
		context['profile_posts'] = Post.objects.select_related('subforum__forum').filter(
			user=context['object'].user
		)[:10]
		context['profile_comments'] = Comment.objects.select_related('post').filter(
			user=context['object'].user
		)[:10]
		return context


class ProfileUpdateView(UpdateView):
	"""Display own user's profile info and handle update."""

	model = Profile
	fields = ['first_name', 'last_name', 'birthday', 'bio']

	def get_object(self, queryset=None):
		"""Override to select related user."""

		return Profile.objects.select_related('user').get(
			slug=self.kwargs.get(self.slug_url_kwarg)
		)

	def get_form(self, form_class=None):
		"""Set widgets for form and initialy disable each field."""
		
		form = super(UpdateView, self).get_form(form_class)

		form.fields['first_name'].widget = forms.TextInput(
			attrs={'class': 'form-control', 'disabled': ''}
		)
		form.fields['last_name'].widget = forms.TextInput(
			attrs={'class': 'form-control', 'disabled': ''}
		)
		form.fields['birthday'].widget = forms.DateInput(
			attrs={'class': 'form-control', 'disabled': '', 'type': 'date'}
		)
		form.fields['bio'].widget = forms.Textarea(
			attrs={'class': 'form-control', 'disabled': '', 'rows': '5'}
		)
		return form

	def get_success_url(self):
		"""Redirect to own profile on update success."""
		return reverse('self_profile', args=[self.request.user])

	def get(self, request, *args, **kwargs):
		"""Redirect to ProfileDetailView if the requested profile is not request.user."""
		user = None
		try:
			user = User.objects.get(username=self.kwargs['slug'])
		finally:
			if request.user != user:
				return redirect('profile', slug=self.kwargs['slug'])
			self.object = self.get_object()
			return super().get(request, *args, **kwargs)

	def get_context_data(self, **kwargs):
		"""Load profile's last posts and comments."""
		context = super().get_context_data(**kwargs)

		user = self.object.user

		context['user_configurations_form'] = UserConfigurationsForm(
			initial={'summary_reports': user.summary_reports}
		)
		context['profile_posts'] = Post.objects.select_related('subforum__forum')\
			.filter(user=user)[:10]

		context['profile_comments'] = Comment.objects.filter(user=user)[:10]
		return context
