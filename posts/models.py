"""Posts model definition."""

# Python
# import pdb

# Django
from django.db import models

# Pyrty
from comments.models import Comment
from utils.models import PyrtyModel


class Post(PyrtyModel):
	"""A post is the content that a user is sharing. It has a Subforum as parent,
	and can contain comments as childrens.
	"""

	user = models.ForeignKey('users.User', on_delete=models.CASCADE, null=False)
	subforum = models.ForeignKey('subforums.Subforum', on_delete=models.CASCADE, null=False)

	title = models.CharField(
		'post title',
		max_length=80, 
		null=False, 
		blank=False
	)
	content = models.TextField(
		'post content',
		max_length=5000,
		null=False,
		blank=False
	)

	positive_votes = models.ManyToManyField('users.User', related_name='p_positive_vote_set')
	negative_votes = models.ManyToManyField('users.User', related_name='p_negative_vote_set')

	comments = 0
	score = 0

	def __init__(self, *args, **kwargs):
		# init with the ammount of comments and score (positive votes - negative votes)
		# if the post is persisted
		super(Post, self).__init__(*args, **kwargs)
		if self.id is not None:
			self.comments = Comment.objects.filter(post=self).count()
			self.score = (
				self.positive_votes.all().count() -
				self.negative_votes.all().count()
			)

	def __str__(self):
		"""Return post's title and autor."""
		return "'{}'".format(self.title)
