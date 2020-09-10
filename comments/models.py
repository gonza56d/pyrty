"""Comment model definition."""

# Django
from django.db import models

# Pyrty
from users.models import User
from utils.models import PyrtyModel


class Comment(PyrtyModel):
	"""A comment is a content shared by a user in some post.""" 

	user = models.ForeignKey('users.User', on_delete=models.CASCADE, null=False)
	post = models.ForeignKey('posts.Post', on_delete=models.CASCADE, null=False)

	content = models.TextField(max_length=1000, null=False, blank=False)

	positive_votes = models.ManyToManyField('users.User', related_name='c_positive_vote_set')
	negative_votes = models.ManyToManyField('users.User', related_name='c_negative_vote_set')

	score = 0

	def __init__(self, *args, **kwargs):
		# init with the score (positive votes - negative votes) if the comment is persisted
		super(Comment, self).__init__(*args, **kwargs)
		if self.id is not None:
			self.score = (
				self.positive_votes.all().count() -
				self.negative_votes.all().count()
			)

	def __str__(self):
		"""Return the comment str."""
		return "'{}'".format(self.content)

	class Meta(PyrtyModel.Meta):
		ordering = ['created', 'modified']
