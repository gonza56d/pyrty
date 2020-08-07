"""Post views."""

# Python
import pdb

# Django
from django import forms
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

# Pyrty
from comments.forms import CommentForm
from comments.models import Comment
from posts.models import Post
from subforums.models import Subforum


class PostDetailView(DetailView):
	"""Display a post with its children comments."""

	model = Post
	forum = None
	subforum = None

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['comments'] = Comment.objects.filter(post=self.object)
		context['current_subforum'] = self.object.subforum
		context['current_subforum_url'] = self.object.subforum.url_name
		context['current_forum'] = self.object.subforum.forum
		context['current_forum_url'] = self.object.subforum.forum.url_name
		context['comment_form'] = CommentForm(context['object'])
		return context


class CreatePostView(CreateView):
	"""Create a new post view."""

	model = Post
	subforum = None

	fields = ['subforum', 'title', 'content']

	#  TODO

	def get(self, request, *args, **kwargs):
		self.subforum = Subforum.objects.get(pk=self.kwargs['subforum_id'])
		return super().get(request, *args, **kwargs)
