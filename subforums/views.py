"""Subforum views."""

# Python
# import pdb

# Django
from django.views.generic import ListView

# Pyrty
from posts.models import Post
from subforums.models import Subforum


class PostList(ListView):
	"""List all the posts children of the subforum passed in the GET request."""
	model = Post
	forum = None
	subforum = None

	def get_context_data(self, **kwargs):
		context = super(PostList, self).get_context_data(**kwargs)
		context['current_forum'] = self.forum
		context['current_forum_url'] = self.forum.url_name
		context['current_subforum'] = self.subforum
		context['current_subforum_url'] = self.subforum.url_name
		return context

	def get_queryset(self, queryset=None):
		self.subforum = Subforum.objects.get(name=self.kwargs['subforum'].replace('_', ' '))
		self.forum = self.subforum.forum
		return Post.objects.filter(subforum=self.subforum)
