"""Private message asynchronous tasks."""

# Python
import logging, time

# Django
from django.core import serializers

# Pyrty
from privatemessages.forms import PrivateMessageForm
from pyrty.celery import app as celery_app
from users.models import User


@celery_app.task(bind=True, default_retry_delay=30)
def send_private_message(*args, **kwargs):
    """
    Asynchronously send private message. Retry in 30 secs if fail.
    """
    form = PrivateMessageForm(data=post_request)
    if form.is_valid():
        private_message = form.save(commit=False)
        private_message.origin_user = User.objects.get(id=user_id)
        private_message.save()
        print('saved')

    logging.info('PrivateMessage sent: ' + str(private_message))
