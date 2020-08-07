"""Post urls."""

# Django
from django.urls import path

# Pyrty
from posts.views import CreatePostView, PostDetailView


urlpatterns = [
	path('<int:pk>', PostDetailView.as_view(), name='post'),
	path('create/<int:subforum_id>', CreatePostView.as_view(), name='create_post')
]
