"""Post urls."""

# Django
from django.urls import path

# Pyrty
from posts.views import CreatePostView, PostDetailView, submit_vote


urlpatterns = [
	path('<int:pk>', PostDetailView.as_view(), name='post'),
	path('create/<int:subforum_id>', CreatePostView.as_view(), name='create_post'),
	path('submit_vote/', submit_vote, name='submit_vote')
]
