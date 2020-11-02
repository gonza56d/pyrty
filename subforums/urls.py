"""Subforums urls."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework import routers

# Pyrty
from subforums.views import PostList
from subforums.rest.views import SubforumViewSet


router = routers.SimpleRouter()
router.register(r'subforums', SubforumViewSet, basename='subforums')

urlpatterns = [
	path('<str:subforum>', PostList.as_view(), name='subforum'),
    path('rest/', include(router.urls))
]
