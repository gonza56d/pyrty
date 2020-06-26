"""PrivateMessage admin."""

# Django
from django.contrib import admin

# Pyrty
from private_messages.models import PrivateMessage


@admin.register(PrivateMessage)
class PrivateMessageAdmin(admin.ModelAdmin):
	"""PrivateMessage model admin."""

	list_display = ('origin_user', 'target_user', 'subject', 'message', 'created')
	search_fields = ('origin_user__username', 'target_user__username', 'created')
	list_filter = ('origin_user__username', 'target_user__username', 'created')
