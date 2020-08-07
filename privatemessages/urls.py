"""PrivateMessage urls."""

# Django
from django.urls import path

# Pyrty
from privatemessages.views import PrivateMessageList, create_private_message


urlpatterns = [
	path('inbox/<str:origin_user>', PrivateMessageList.as_view(), name='private_message'),
	path('create_private_message/', create_private_message, name='create_private_message')
]
