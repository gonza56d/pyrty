"""Pyrty views."""

# Django
from django.views.generic import ListView

# Pyrty
from forums.models import Forum


class ForumList(ListView):
	"""List all the forums."""
	model = Forum
