"""Notification urls."""

# Django
from django.contrib.auth.decorators import login_required
from django.urls import path
from notifications.views import get_notification, NotificationList


urlpatterns = [
	path('', login_required(NotificationList.as_view()), name='notifications'),
    path('get_notification/<int:pk>', login_required(get_notification), name='get_notification'),
]
