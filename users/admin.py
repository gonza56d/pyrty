"""User models admin."""

# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Pyrty
from users.models import User


class CustomUserAdmin(UserAdmin):
	"""User model admin."""

	list_display = ('email', 'username', 'first_name', 'last_name', 'is_verified')
	search_fields = ('email', 'username', 'first_name', 'last_name')
	list_filter = ('email', 'username', 'is_verified', 'created', 'modified')


admin.site.register(User, CustomUserAdmin)
