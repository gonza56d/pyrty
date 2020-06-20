"""Private messages model definition."""

# Django
from django.db import models

# Pyrty
from utils.models import PyrtyModel


class PrivateMessage(PyrtyModel):
	"""A private message sent by a user to another user."""

	from_user = models.ForeignKey(
		'users.User',
		related_name='from_user',
		on_delete=models.CASCADE,
		null=False
	)
	to_user = models.ForeignKey(
		'users.User',
		related_name='to_user',
		on_delete=models.CASCADE,
		null=False
	)

	subject = models.CharField(
		'message subject',
		max_length=50,
		null=False,
		blank=False
	)

	message = models.TextField(
		'message content',
		max_length=3000,
		null=False,
		blank=False
	)
