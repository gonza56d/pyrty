"""Notification urls."""

# Django
from django.urls import path
from notifications.views import get_notification, NotificationList


urlpatterns = [
	path('', NotificationList.as_view(), name='notifications'),
    path('get_notification/<int:pk>', get_notification, name='get_notification'),
]
