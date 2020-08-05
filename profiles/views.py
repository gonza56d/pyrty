"""Profile views."""

# Django
from django.views.generic.detail import DetailView

# Pyrty
from privatemessages.forms import PrivateMessageForm
from profiles.models import Profile
from users.models import User


class ProfileDetailView(DetailView):
	"""Display a profile info."""

	model = Profile

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['private_message_form'] = PrivateMessageForm(
			target_user=User.objects.get(username=self.kwargs['slug'])
		)
		return context
