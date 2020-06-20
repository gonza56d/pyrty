"""PrivateMessage models admin."""

# Django
from django.contrib import admin

# Pyrty
from private_messages.models import PrivateMessage


@admin.register(PrivateMessage)
class PrivateMessageAdmin(admin.ModelAdmin):
	"""PrivateMessage model admin."""

	list_display = ('from_user', 'to_user', 'subject', 'message', 'created')
	search_fields = ('from_user__username', 'to_user__username', 'created')
	list_filter = ('from_user__username', 'to_user__username', 'created')
