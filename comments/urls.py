"""Comment urls."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework import routers

# Pyrty
from comments.rest.views import ListComments
from comments.views import create_comment, delete_comment


urlpatterns = [
	path('create_comment/', create_comment, name='create_comment'),
	path('delete_comment/', delete_comment, name='delete_comment'),
	path('rest/list_comments/', ListComments.as_view(), name='api_list_comments')
]
