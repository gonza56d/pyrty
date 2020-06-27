"""Forum urls."""

# Django
from django.urls import path

# Pyrty
from forums.views import SubforumList


urlpatterns = [
	path('<str:forum>', SubforumList.as_view(), name='forum')
]
