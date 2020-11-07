"""Pyrty views."""

# Django
from django.shortcuts import redirect
from django.views.generic import ListView

# Pyrty
from users.models import User
from forums.models import Forum


class ForumList(ListView):
	"""List all the forums."""
	model = Forum
