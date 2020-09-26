"""Post urls."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework import routers

# Pyrty
from posts.rest.views import PostViewSet
from posts.views import CreatePostView, PostDetailView, submit_vote, delete_post


router = routers.SimpleRouter()
router.register(r'posts', PostViewSet, basename='posts')

urlpatterns = [
	path('<int:pk>', PostDetailView.as_view(), name='post'),
	path('create/<int:subforum_id>', CreatePostView.as_view(), name='create_post'),
	path('submit_vote/', submit_vote, name='submit_post_vote'),
	path('delete/', delete_post, name='delete_post'),
	path('rest/', include(router.urls)),
]
