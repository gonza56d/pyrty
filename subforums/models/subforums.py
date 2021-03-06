"""Subforums model definition."""

# Django
from django.db import models

# Pyrty
from utils.models import PyrtyModel


class Subforum(PyrtyModel):
	"""A subforum is the model which has a single Forum as parent. It can
	contain posts in it that are its childrens.
	"""

	forum = models.ForeignKey('forums.Forum', on_delete=models.CASCADE, null=False)
	name = models.CharField(
		'subforum title',
		max_length=50,
		null=False,
		blank=False
	)

	posts = 0
	new_posts = 0
	url_name = ''

	def __init__(self, *args, **kwargs):
		super(Subforum, self).__init__(*args, **kwargs)
		self.url_name = str(self.name).replace(' ', '_')

	def __str__(self):
		"""Return subforum name."""
		return self.name

	class Meta(PyrtyModel.Meta):
		ordering = ['created', 'modified']
		unique_together = ['forum', 'name']
