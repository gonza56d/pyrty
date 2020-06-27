"""PrivateMessage urls."""

# Django
from django.urls import path

# Pyrty
from private_messages.views import PrivateMessageList


urlpatterns = [
	path('<str:origin_user>', PrivateMessageList.as_view(), name='private_message')
]
