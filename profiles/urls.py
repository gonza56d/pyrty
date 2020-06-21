"""Profile urls."""

# Django
from django.urls import path
from profiles.views import ProfileDetailView


urlpatterns = [
	path('<slug:slug>', ProfileDetailView.as_view(), name='profile')
]
