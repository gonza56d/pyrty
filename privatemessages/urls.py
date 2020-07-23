"""PrivateMessage urls."""

# Django
from django.urls import path

# Pyrty
from privatemessages.views import PrivateMessageList


urlpatterns = [
	path('<str:origin_user>', PrivateMessageList.as_view(), name='private_message')
]
