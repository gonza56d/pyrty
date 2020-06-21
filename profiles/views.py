"""Profile views."""

# Django
from django.views.generic.detail import DetailView

# Pyrty
from profiles.models import Profile


class ProfileDetailView(DetailView):
	"""Display a profile info."""

	model = Profile

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context
