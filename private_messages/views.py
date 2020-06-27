"""Private message views."""

# Django
from django.db.models import Exists, OuterRef
from django.views.generic import ListView

# Pyrty
from private_messages.models import PrivateMessage
from users.models import User


class PrivateMessageList(ListView):
	"""Display inbox with list of messages from a user."""

	model = PrivateMessage

	def get_context_data(self, **kwargs):
		context = super(PrivateMessageList, self).get_context_data(**kwargs)
		context['current_inbox'] = self.kwargs['origin_user']
		context['inbox'] = User.objects.filter(
			Exists(PrivateMessage.objects.filter(origin_user=OuterRef('pk')))
		)
		return context

	def get_queryset(self, queryset=None):
		private_messages = PrivateMessage.objects.filter(
			target_user=self.request.user, 
			origin_user__username=self.kwargs['origin_user']
		).order_by('created')
		private_messages.update(seen=True)
		return private_messages
