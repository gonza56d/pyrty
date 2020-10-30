"""Asynchronous private message tasks."""

# Python
import logging
from time import sleep

# Django
from django.core import serializers

# Pyrty
from privatemessages.forms import PrivateMessageForm
from pyrty.celery import app as celery_app
from users.models import User


@celery_app.task(bind=True, default_retry_delay=30)
def send_private_message(self, post_request, user_id=None):
    """
    Asynchronously send private message. Retry in 30 secs if fail.
    """
    sleep(10)
    form = PrivateMessageForm(data=post_request)

    if form.is_valid():
        private_message = form.save(commit=False)
        private_message.origin_user = User.objects.get(id=user_id or post_request['origin_user'])
        private_message.save()
        logging.info('PrivateMessage sent: ' + str(private_message))
    else:
        logging.warning('Private message failed: ' + 
            'post_request: ' + str(post_request) + ' - user_id: ' + str(user_id))
