"""Private messages model definition."""

# Django
from django.db import models

# Pyrty
from utils.models import PyrtyModel


class PrivateMessage(PyrtyModel):
	"""A private message sent by a user to another user."""

	origin_user = models.ForeignKey(
		'users.User',
		on_delete=models.CASCADE,
		null=False,
		related_name='message_origin'
	)

	target_user = models.ForeignKey(
		'users.User',
		on_delete=models.CASCADE,
		null=False,
		related_name='message_target'
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

	seen = models.BooleanField(default=False)
