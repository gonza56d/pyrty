"""Profile views."""

# Python
# import pdb

# Django
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView

# Pyrty
from comments.models import Comment
from posts.models import Post
from privatemessages.forms import PrivateMessageForm
from profiles.models import Profile
from users.models import User


class ProfileDetailView(DetailView):
	"""Display third users' profile info."""

	model = Profile

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
		context = super().get_context_data(**kwargs)
		context['private_message_form'] = PrivateMessageForm(
			target_user=User.objects.get(username=self.kwargs['slug'])
		)
		context['profile_posts'] = Post.objects.filter(user=context['object'].user)[:10]
		context['profile_comments'] = Comment.objects.filter(user=context['object'].user)[:10]
		return context


class ProfileUpdateView(UpdateView):
	"""Display own user's profile info and handle edit."""

	model = Profile
	fields = ['first_name', 'last_name']

	def get_success_url(self):
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
		context = super().get_context_data(**kwargs)
		context['profile_posts'] = Post.objects.filter(user=self.object.user)
		context['profile_comments'] = Comment.objects.filter(user=self.object.user)
		return context
