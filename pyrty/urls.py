"""Project main URLs."""

# Django
from django.contrib import admin
from django.urls import path, include

# Pyrty
from pyrty.views import ForumList
from utils.dbinjector.db_injector import DBInjector

urlpatterns = [
	# Django Admin
    path('admin/', admin.site.urls),
    # Pyrty
    path('', ForumList.as_view(), name='forums'),
    # Comments
    path('comments/', include('comments.urls')),
    # Forums
    path('forums/', include('forums.urls')),
    # Posts
    path('posts/', include('posts.urls')),
    # Private Messages
    path('private_messages/', include('privatemessages.urls')),
    # Profiles
    path('profiles/', include('profiles.urls')),
    # Subforums
    path('subforums/', include('subforums.urls')),
    # Users
    path('users/', include('users.urls'))
]


# db_inj = DBInjector()
