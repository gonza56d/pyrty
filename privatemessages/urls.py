"""PrivateMessage urls."""

# Django
from django.contrib.auth.decorators import login_required
from django.urls import include, path

# Django REST Framework
from rest_framework import routers

# Pyrty
from privatemessages.rest.views import PrivateMessageViewSet
from privatemessages.views import PrivateMessageList, create_private_message


router = routers.SimpleRouter()
router.register(r'private_messages', PrivateMessageViewSet, basename='private_messages')

urlpatterns = [
	path('inbox/<str:origin_user>', login_required(PrivateMessageList.as_view()), name='private_message'),
	path('create_private_message/', login_required(create_private_message), name='create_private_message'),
	path('rest/', include(router.urls))
]
