"""Forum urls."""

# Django
from django.urls import path
from forums.views import SubforumList


urlpatterns = [
	path('<str:forum>', SubforumList.as_view(), name='forum')
]
