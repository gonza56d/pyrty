"""Notification admin."""

# Django
from django.contrib import admin

# Pyrty
from notifications.models import Notification


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
	"""Notification model admin."""

	list_display = ('origin_user', 'target_user', 'url', 'message', 'created')
	search_fields = ('origin_user__username', 'target_user__username', 'created')
	list_filter = ('origin_user__username', 'target_user__username', 'created')
