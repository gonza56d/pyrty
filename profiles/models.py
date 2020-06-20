"""Profile model definition."""

# Django
from django.db import models

# Utils
from utils.models import PyrtyModel


def get_rank_by_reputation(reputation):
	"""Return rank name based on reputation score."""
	if reputation < 100:
		return "Initiate"
	elif reputation >= 100 and reputation < 200:
		return "Junior"
	elif reputation >= 200 and reputation < 300:
		return "Enthusiast"
	elif reputation >= 300 and reputation < 500:
		return "Experienced"
	elif reputation >= 500 and reputation < 1000:
		return "Community Contributor"
	elif reputation >= 1000 and reputation < 2000:
		return "Great Contributor"
	elif reputation >= 2000 and reputation < 3000:
		return "Community Warrior"
	elif reputation >= 3000:
		return "Community Veteran"


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

	bio = models.TextField(max_length=1000, blank=True)

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

	is_moderator = models.BooleanField('moderator', default=False)

	rank = ""

	def __init__(self):
		self.rank = get_rank_by_reputation(self.reputation)

	def __str__(self):
		"""Return user's username."""
		return str(self.user)
