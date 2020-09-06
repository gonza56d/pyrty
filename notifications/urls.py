"""Notification urls."""

# Django
from django.urls import path
from notifications.views import NotificationList, update_notifications


urlpatterns = [
	path('', NotificationList.as_view(), name='notifications'),
	path('update_notifications', update_notifications, name='update_notifications')
]
