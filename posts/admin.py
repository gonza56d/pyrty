"""Post models admin."""

# Django
from django.contrib import admin

# Pyrty
from posts.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	"""Post model admin."""

	list_display = ('user', 'subforum', 'title', 'content', 'answers', 'modified', 'created')
	search_fields = ('user', 'subforum', 'title', 'modified', 'created')
	list_filter = ('user__username', 'user__email', 'subforum__name', 'title',
		'modified', 'created')
