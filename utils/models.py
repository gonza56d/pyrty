"""Project's abstract utility model."""

from django.db import models


class PyrtyModel(models.Model):
	"""An abstract base model which any other project's model can extend from
	in order to inherit some utility fields such as created and modified
	and also ordering utilities by these fields.
	"""

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
