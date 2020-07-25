"""Comment models admin."""

# Django
from django.contrib import admin

# Pyrty
from comments.models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
	"""Comment model admin."""

	list_display = ('user', 'post', 'content', 'created', 'modified')
	list_filter = ('user__username', 'user__email', 'post__title', 'content', 'created', 'modified')
	search_fields = ('user__username', 'user__email', 'post__title', 'content')
