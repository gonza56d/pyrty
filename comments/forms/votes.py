"""Comment vote forms."""

# Django
from django import forms
from django.core.exceptions import ValidationError
from django.db.models import Prefetch

# Pyrty
from comments.models import Comment
from profiles.views import run_reputation_update
from users.models import User
from utils import vote_manager


class CommentVoteForm(forms.Form):
	"""Form for comment vote submit."""

	comment_id = None
	positive = forms.BooleanField()
	user = None

	def __init__(self, comment_id=None, positive=None, user=None, *args, **kwargs):
		"""Init with comment's id to vote, and positive=True/False for voting value."""

		super(CommentVoteForm, self).__init__(*args, **kwargs)

		self.fields['positive'] = forms.BooleanField(
			initial=positive,
			required=False
		)
		self.comment_id = comment_id
		self.user = user

	def clean(self):
		comment = Comment.objects.get(pk=self.comment_id)
		if comment.user == self.user:
			raise ValidationError("Voting your own comment is not allowed")

	def submit_vote(self, user):
		"""Submit user vote for a comment."""

		# get variables
		comment_id, positive = self.comment_id, self.cleaned_data.get('positive')
		user_queryset = User.objects.filter(username=user.username)
		prefetch_positive = Prefetch('positive_votes', queryset=user_queryset, to_attr='user_positive_vote')
		prefetch_negative = Prefetch('negative_votes', queryset=user_queryset, to_attr='user_negative_vote')
		instance = Comment.objects.prefetch_related(prefetch_positive).prefetch_related(prefetch_negative).get(pk=comment_id)

		# vote submit
		vote_manager.handle(positive, instance, user)

		# profile score update
		run_reputation_update(instance.user)
