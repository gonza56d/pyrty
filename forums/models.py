"""Forums model definition."""

# Django
from django.db import models

# Pyrty
from utils.models import PyrtyModel


class Forum(PyrtyModel):
	"""
	Object that contains subforums.
	"""

	name = models.CharField(
		'forum title',
		unique=True,
		error_messages={
			'unique': 'Duplicated forum name.'
		},
		max_length=50,
		null=False,
		blank=False
	)

	url_name = ''
	subforums = 0
	posts = 0
	new_posts = 0

	def __init__(self, *args, **kwargs):
		super(Forum, self).__init__(*args, **kwargs)
		self.url_name = str(self.name).replace(' ', '_')

	def __str__(self):
		"""Return forum name."""
		return self.name
