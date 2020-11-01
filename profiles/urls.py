"""Profile urls."""

# Django
from django.contrib.auth.decorators import login_required
from django.urls import path
from profiles.views import ProfileDetailView, ProfileUpdateView


urlpatterns = [
	path('<slug:slug>', login_required(ProfileDetailView.as_view()), name='profile'),
	path('self/<slug:slug>', login_required(ProfileUpdateView.as_view()), name='self_profile')
]
