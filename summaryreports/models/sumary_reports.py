"""Summary report models."""

# Django
from django.db import models

# Pyrty
from utils.models import PyrtyModel


class SummaryReport(PyrtyModel):
	"""Summary report for each user.

	Contains a mix of data resulting from the time interval
	chosen by the user.
	"""

	user = models.ForeignKey('users.User', on_delete=models.CASCADE, null=False)

	posts_made = models.PositiveIntegerField(default=0)
	comments_made = models.PositiveIntegerField(default=0)
	comments_received = models.PositiveIntegerField(default=0)
	messages_sent = models.PositiveIntegerField(default=0)
	messages_received = models.PositiveIntegerField(default=0)
	notifications = models.PositiveIntegerField(default=0)
