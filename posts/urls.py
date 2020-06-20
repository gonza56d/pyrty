"""Posts urls."""

# Django
from django.urls import path
from posts.views import PostDetailView


urlpatterns = [
	path('<int:pk>', PostDetailView.as_view(), name='post')
]
