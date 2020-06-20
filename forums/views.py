"""Forums views."""

# Django
from django.views.generic import ListView

# Pyrty
from forums.models import Forum
from subforums.models import Subforum


class SubforumList(ListView):
	model = Subforum
	forum = ""

	def get_queryset(self):
		print(self.forum)
		forum = Forum.objects.get(name=self.forum.replace('_', ' '))
		return Subforum.objects.filter(forum=forum)
