"""Posts model definition."""

# Django
from django.db import models

# Pyrty
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

	answers = 0

	def __str__(self):
		"""Return post's title and autor."""
		return "'{}'' by {}".format(self.title, self.user)
