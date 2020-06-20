"""Forum models admin."""

# Django
from django.contrib import admin

# Pyrty
from forums.models import Forum


@admin.register(Forum)
class ForumAdmin(admin.ModelAdmin):
	"""Forum model admin."""

	list_display = ('name', 'subforums', 'new_posts', 'modified')
	list_filter = ('name', 'modified')
	search_fields = ('name',)
