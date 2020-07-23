"""PrivateMessage admin."""

# Django
from django.contrib import admin

# Pyrty
from privatemessages.models import PrivateMessage


@admin.register(PrivateMessage)
class PrivateMessageAdmin(admin.ModelAdmin):
	"""PrivateMessage model admin."""

	list_display = ('origin_user', 'target_user', 'subject', 'message', 'created', 'seen')
	search_fields = ('origin_user__username', 'target_user__username', 'created')
	list_filter = ('origin_user__username', 'target_user__username', 'created')
