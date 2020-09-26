"""Comment urls."""

# Python
# import pdb

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework import routers

# Pyrty
from comments.rest.views import CommentViewSet
from comments.views import create_comment, delete_comment, submit_vote


router = routers.SimpleRouter()
router.register(r'comments', CommentViewSet, basename='comments')

urlpatterns = [
	path('create_comment/', create_comment, name='create_comment'),
	path('delete_comment/', delete_comment, name='delete_comment'),
	path('submit_vote/', submit_vote, name='submit_comment_vote'),
	path('rest/', include(router.urls)),
]
