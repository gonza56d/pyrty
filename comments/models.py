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

	def __str__(self):
		"""Return the comment str."""
		return "'{}'".format(self.content)
