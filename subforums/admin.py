"""Subforum models admin."""

# Django
from django.contrib import admin

# Pyrty
from subforums.models import Subforum


@admin.register(Subforum)
class SubforumAdmin(admin.ModelAdmin):
	"""Subforum model admin."""

	list_display = ('forum', 'name', 'posts', 'new_posts', 'modified')
	search_fields = ('forum__name', 'name', 'modified')
	list_filter = ('forum__name', 'name', 'modified')
