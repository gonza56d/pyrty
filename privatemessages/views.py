"""Private message views."""

# Python
# import pdb

# Django
from django.db.models import Exists, OuterRef, Q
from django.http import JsonResponse
from django.views.generic import ListView

# Pyrty
from privatemessages.forms import PrivateMessageForm
from privatemessages.models import PrivateMessage
from privatemessages import tasks
from users.models import User


class PrivateMessageList(ListView):
	"""Display inbox with list of messages from a user."""

	model = PrivateMessage
	paginate_by = 10

	def get_context_data(self, **kwargs):
		context = super(PrivateMessageList, self).get_context_data(**kwargs)
		context['current_inbox'] = self.kwargs['origin_user']
		context['inbox'] = User.objects.filter(
			Exists(PrivateMessage.objects.filter(origin_user=OuterRef('pk')))
		)
		context['private_message_form'] = PrivateMessageForm(
			target_user=User.objects.get(username=self.kwargs['origin_user'])
		)
		return context

	def get_queryset(self, queryset=None):
		private_messages = PrivateMessage.objects\
			.select_related('origin_user').filter(
			Q(
				target_user=self.request.user,
				origin_user__username=self.kwargs['origin_user']
			) |
			Q (
				target_user__username=self.kwargs['origin_user'],
				origin_user=self.request.user
			)
		).order_by('created')
		PrivateMessage.objects.filter(target_user=self.request.user).update(seen=True)
		return private_messages


def create_private_message(request):
	if request.method == 'POST':
		form = PrivateMessageForm(data=request.POST)
		if form.is_valid():
			tasks.send_private_message.delay(request.POST, request.user.id)
			return JsonResponse({'status': 200, 'message': 'Private message sent'})
