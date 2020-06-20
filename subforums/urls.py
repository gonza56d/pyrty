"""Subforums urls."""

# Django
from django.urls import path
from subforums.views import PostList


urlpatterns = [
	path('<str:subforum>', PostList.as_view(), name='subforum')
]
