"""Detail post views."""

# Django
from django.db.models import Prefetch
from django.views.generic.detail import DetailView

# Pyrty
from comments.forms import CommentForm, CommentVoteForm
from comments.models import Comment
from posts.forms import PostVoteForm
from posts.models import Post
from users.models import User


class PostDetail(DetailView):
	"""Display a post with its comments."""

	model = Post
	user_queryset = None
	positive_vote_prefetch = None
	negative_vote_prefetch = None

	def get_object(self, queryset=None):
		"""Override to select related Subforum, forum and user vote."""

		self.user_queryset = User.objects.filter(username=self.request.user.username)
		self.positive_vote_prefetch = Prefetch(
			'positive_votes', queryset=self.user_queryset, to_attr='user_positive_vote'
		)
		self.negative_vote_prefetch = Prefetch(
			'negative_votes', queryset=self.user_queryset, to_attr='user_negative_vote'
		)
		return Post.objects.select_related('subforum__forum')\
			.select_related('user').prefetch_related(self.positive_vote_prefetch)\
			.prefetch_related(self.negative_vote_prefetch)\
			.get(pk=self.kwargs.get(self.pk_url_kwarg))

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		context['comments'] = Comment.objects.prefetch_related(self.positive_vote_prefetch)\
			.prefetch_related(self.negative_vote_prefetch).filter(post=self.object)

		context['current_subforum'] = self.object.subforum
		context['current_subforum_url'] = self.object.subforum.url_name
		context['current_forum'] = self.object.subforum.forum
		context['current_forum_url'] = self.object.subforum.forum.url_name
		context['comment_form'] = CommentForm(context['object'])
		context['positive_post_vote_form'] = PostVoteForm(post_id=self.object.id, positive=True)
		context['negative_post_vote_form'] = PostVoteForm(post_id=self.object.id, positive=False)
		context['positive_comment_vote_form'] = CommentVoteForm(positive=True)
		context['negative_comment_vote_form'] = CommentVoteForm(positive=False)
		return context
