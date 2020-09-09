"""Post urls."""

# Django
from django.urls import path

# Pyrty
from posts.views import CreatePostView, PostDetailView, submit_positive_vote, submit_negative_vote


urlpatterns = [
	path('<int:pk>', PostDetailView.as_view(), name='post'),
	path('create/<int:subforum_id>', CreatePostView.as_view(), name='create_post'),
	path('submit_positive_vote/', submit_positive_vote, name='submit_positive_vote'),
	path('submit_negative_vote/', submit_negative_vote, name='submit_negative_vote')
]
