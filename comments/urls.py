"""Comment urls."""

# Django
from django.urls import path
from comments.views import create_comment


urlpatterns = [
	path('create_comment/', create_comment, name='create_comment')
]
