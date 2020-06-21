"""Posts views."""

# Python
# import pdb

# Django
from django.views.generic.detail import DetailView

# Pyrty
from comments.forms import CommentForm
from comments.models import Comment
from posts.models import Post


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
		context['comment_form'] = CommentForm()
		return context
