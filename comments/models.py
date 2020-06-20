"""Comments model definition."""

# Django
from django.db import models

# Pyrty
from users.models import User
from utils.models import PyrtyModel


class Comment(PyrtyModel):
	"""A comment is a content shared by a user in some other user's or own post.
	It can receive positive and negative votes by any user reading the post
	(one vote by user), and also can be marked as favourite by the post autor
	if the comment is not shared by the post autor itself.
	""" 

	user = models.ForeignKey('users.User', on_delete=models.CASCADE, null=False)
	post = models.ForeignKey('posts.Post', on_delete=models.CASCADE, null=False)

	users_positive_votes = models.ManyToManyField(
		User,
		related_name='users_positive_votes'
	)
	users_negative_votes = models.ManyToManyField(
		User,
		related_name='users_negative_votes'
	)

	positive_votes = models.PositiveIntegerField(default=0)
	negative_votes = models.PositiveIntegerField(default=0)

	content = models.TextField(max_length=1000, null=False, blank=False)
