"""Profile models admin."""

# Django
from django.contrib import admin

# Pyrty
from profiles.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
	"""Profile model admin."""

	list_display = ('user', 'is_moderator', 'reputation', 'created', 'modified')
	search_fields = ('user__username', 'user__email', 'user__first_name', 'user__last_name')
	list_filter = ('reputation', 'is_moderator', 'created', 'modified')
