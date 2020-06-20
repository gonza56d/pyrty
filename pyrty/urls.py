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
    path('forums/', include('forums.urls')),
]
