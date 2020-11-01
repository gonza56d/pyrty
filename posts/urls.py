"""Post urls."""

# Django
from django.contrib.auth.decorators import login_required
from django.urls import include, path

# Django REST Framework
from rest_framework import routers

# Pyrty
from posts.rest.views import PostViewSet
from posts.views import CreatePost, delete_post, PostDetail, submit_vote


router = routers.SimpleRouter()
router.register(r'posts', PostViewSet, basename='posts')

urlpatterns = [
	path('<int:pk>', PostDetail.as_view(), name='post'),
	path('create/<int:subforum_id>', login_required(CreatePost.as_view()), name='create_post'),
	path('submit_vote/', login_required(submit_vote), name='submit_post_vote'),
	path('delete/', login_required(delete_post), name='delete_post'),
	path('rest/', include(router.urls)),
]
