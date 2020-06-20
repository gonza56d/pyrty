"""Forums views."""

# Django
from django.views.generic import ListView

# Pyrty
from forums.models import Forum


class ForumList(ListView):
    model = Forum
