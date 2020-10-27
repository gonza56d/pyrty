"""Comment models."""

# Django
from django.db import models

# Pyrty
from utils.models import PyrtyModel


class Notification(PyrtyModel):
	"""Notification model.

	Notify some user about something."""

	origin_user = models.ForeignKey(
		'users.User', 
		on_delete=models.CASCADE, 
		null=True,
		related_name='notification_origin'
	)

	target_user = models.ForeignKey(
		'users.User', 
		on_delete=models.CASCADE, 
		null=False,
		related_name='notification_target'
	)

	message = models.CharField(max_length=128, null=False)
	url = models.CharField('Url path', max_length=256, null=True)
	seen = models.BooleanField(default=False)
