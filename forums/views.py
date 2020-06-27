"""Forum views."""

# Python
# import pdb

# Django
from django.views.generic import ListView

# Pyrty
from forums.models import Forum
from subforums.models import Subforum


class SubforumList(ListView):
	"""List all the subforums children of the forum passed in the GET request."""

	model = Subforum
	forum = None

	def get_context_data(self, **kwargs):
		context = super(SubforumList, self).get_context_data(**kwargs)
		context['current_forum'] = self.forum
		context['current_forum_url'] = self.forum.url_name
		return context

	def get_queryset(self, queryset=None):
		self.forum = Forum.objects.get(name=self.kwargs['forum'].replace('_', ' '))
		return Subforum.objects.filter(forum=self.forum)
