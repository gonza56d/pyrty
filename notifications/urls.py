"""Notification urls."""

# Django
from django.urls import path
from notifications.views import update_notifications


urlpatterns = [
	path('update_notifications', update_notifications, name='update_notifications')
]
