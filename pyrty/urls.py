"""Project main URLs."""

# Django
from django.contrib import admin
from django.urls import path, include

# Pyrty
from pyrty.views import ForumList

urlpatterns = [
	# Django Admin
    path('admin/', admin.site.urls),
    # Pyrty
    path('', ForumList.as_view(), name='forums'),
    # Forums
    path('forums/', include('forums.urls')),
    # Posts
    path('posts/', include('posts.urls')),
    # Subforums
    path('subforums/', include('subforums.urls')),
    # Users
    path('users/', include('users.urls'))
]
