"""Private message create views."""

# Django
from django.http import JsonResponse

# Pyrty
from privatemessages import tasks
from privatemessages.forms import PrivateMessageForm


def create_private_message(request):
    """Send private message."""
    if request.method == 'POST':
        form = PrivateMessageForm(data=request.POST)
        if form.is_valid():
            tasks.send_private_message.delay(request.POST, request.user.id)
            return JsonResponse({'status': 200, 'message': 'Private message sent'})
