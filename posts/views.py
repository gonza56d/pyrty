"""Post views."""

# Python
# import pdb

# Django
from django import forms
from django.db.models import Prefetch
from django.shortcuts import redirect
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

# Pyrty
from comments.forms import CommentForm
from comments.models import Comment
from posts.forms import PostVoteForm
from posts.models import Post
from subforums.models import Subforum
from users.models import User


class PostDetailView(DetailView):
	"""Display a post with its comments."""

	model = Post

	def get_object(self, queryset=None):
		"""Override to select related Subforum, forum and user vote."""

		user_queryset = User.objects.filter(username=self.request.user.username)
		positive_vote_prefetch = Prefetch('positive_votes', queryset=user_queryset, to_attr='user_positive_vote')
		negative_vote_prefetch = Prefetch('negative_votes', queryset=user_queryset, to_attr='user_negative_vote')

		return Post.objects.select_related('subforum__forum').select_related('user')\
			.prefetch_related(positive_vote_prefetch).prefetch_related(negative_vote_prefetch)\
			.get(pk=self.kwargs.get(self.pk_url_kwarg))

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['comments'] = Comment.objects.filter(post=self.object)
		context['current_subforum'] = self.object.subforum
		context['current_subforum_url'] = self.object.subforum.url_name
		context['current_forum'] = self.object.subforum.forum
		context['current_forum_url'] = self.object.subforum.forum.url_name
		context['comment_form'] = CommentForm(context['object'])
		context['positive_vote_form'] = PostVoteForm(post_id=self.object.id, positive=True)
		context['negative_vote_form'] = PostVoteForm(post_id=self.object.id, positive=False)
		return context


class CreatePostView(CreateView):
	"""Create a new post view."""

	model = Post
	subforum = None  # used to set post's subforum

	fields = ['subforum', 'title', 'content']

	def get_success_url(self):
		return reverse('subforum', args=[self.kwargs['subforum_id']])

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['subforum'] = self.subforum  # used as url parameter
		return context

	def get_form(self, form_class=None):
		"""Init form by hiding subforum option and leaving current subforum as the only choice."""

		form = super(CreatePostView, self).get_form(form_class)

		form.fields['subforum'] = forms.ModelChoiceField(
			queryset=Subforum.objects.filter(pk=self.subforum.id),
			empty_label=None,
			label = '',
			widget = forms.Select(attrs={'class': 'form-control', 'style': 'display:none;'})
		)
		form.fields['title'].widget = forms.TextInput(
			attrs={'class': 'form-control my-2', 'placeholder': 'Title'}
		)
		form.fields['content'].widget = forms.Textarea(
			attrs={'class': 'form-control my-2', 'placeholder': 'Content'}
		)
		return form

	def get(self, request, *args, **kwargs):
		"""
		Handle get method and populate Subforum object.
		"""
		self.subforum = Subforum.objects.get(pk=self.kwargs['subforum_id'])
		return super().get(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		"""
		Handle post method and create a new Post object.
		"""
		self.subforum = Subforum.objects.get(pk=self.kwargs['subforum_id'])
		form = self.get_form()
		if form.is_valid():
			post = form.save(commit=False)
			post.user = request.user
			post.save()
			return redirect('post', pk=post.id)
		return super().post(request, *args, **kwargs)


def submit_vote(request):
	"""Handle vote submit.

	Create if not exists, delete if exists.
	On create, delete contrary vote of the same user and post if exists."""

	if not request.user.is_authenticated:
		return redirect('signup')

	if request.method == 'POST':
		form = PostVoteForm(
			post_id=request.POST['post'], data=request.POST, user=request.user
		)
		if form.is_valid():
			form.submit_vote(request.user)
		return redirect('post', pk=request.POST['post'])
