"""Forum urls."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework import routers

# Pyrty
from forums.rest.views import ForumViewSet
from forums.views import SubforumList


router = routers.SimpleRouter()
router.register(r'forums', ForumViewSet, basename='forums')

urlpatterns = [
	path('<str:forum>', SubforumList.as_view(), name='forum'),
	path('rest/', include(router.urls))
]
