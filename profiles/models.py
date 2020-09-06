"""Profile model definition."""

# Python
# import pdb
from datetime import datetime

# Django
from django.core.exceptions import ValidationError
from django.db import models

# Django extensions
from django_extensions.db.fields import AutoSlugField

# Utils
from utils.models import PyrtyModel


def slugify(content):
	return str(content)


def validate_birthday(value):
	if value > datetime.date(datetime.now()):
		raise ValidationError(
			'Birthday cannot be later than today', code='invalid_birthday'
		)


class Profile(PyrtyModel):
	"""Profile model.

	Hold the public data of a user like bio, stats, picture.
	"""

	user = models.OneToOneField('users.User', on_delete=models.CASCADE)

	picture = models.ImageField(
		'profile picture',
		upload_to='users/pictures/profiles',
		blank=True,
		null=True
	)

	first_name = models.CharField(
		max_length=50,
		null=False,
		blank=True,
		default=''
	)

	last_name = models.CharField(
		max_length=50,
		null=False,
		blank=True,
		default=''
	)

	slug = AutoSlugField(populate_from='user', slugify_function=slugify)

	bio = models.TextField(max_length=1000, blank=True)

	birthday = models.DateField(null=True, validators=[validate_birthday])

	is_moderator = models.BooleanField(default=False)

	# Stats
	posts = models.PositiveIntegerField(
		'posts made',
		default=0
	)
	comments = models.PositiveIntegerField(
		'comments made',
		default=0
	)
	reputation = models.PositiveIntegerField(
		'user reputation',
		default=0,
		help_text='Score obtained from comments and votes received.'
	)

	def get_rank_by_reputation(self):
		"""Return rank name based on reputation score."""
		if self.reputation < 100:
			return "Initiate"
		elif self.reputation >= 100 and self.reputation < 200:
			return "Junior"
		elif self.reputation >= 200 and self.reputation < 300:
			return "Enthusiast"
		elif self.reputation >= 300 and self.reputation < 500:
			return "Experienced"
		elif self.reputation >= 500 and self.reputation < 1000:
			return "Community Contributor"
		elif self.reputation >= 1000 and self.reputation < 2000:
			return "Great Contributor"
		elif self.reputation >= 2000 and self.reputation < 3000:
			return "Community Warrior"
		elif self.reputation >= 3000:
			return "Community Veteran"

	def __str__(self):
		"""Return user's username."""
		return str(self.user)
