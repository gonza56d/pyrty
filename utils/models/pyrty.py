"""Project's abstract utility model."""

# Django
from django.db import models


class PyrtyModel(models.Model):
	"""Project's base model. Inherit to get modified and created fields, and
    ordering logic."""

	created = models.DateTimeField(
		'created at',
		auto_now_add=True,
		help_text='Date time on which the object was created.'
	)

	modified = models.DateTimeField(
		'modified at',
		auto_now=True,
		help_text='Date time on which the object was last modified.'
	)

	class Meta:
		abstract = True

		get_latest_by = 'created'
		ordering = ['-created', '-modified']
