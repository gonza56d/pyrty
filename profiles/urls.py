"""Profile urls."""

# Django
from django.urls import path
from profiles.views import ProfileDetailView, ProfileUpdateView


urlpatterns = [
	path('<slug:slug>', ProfileDetailView.as_view(), name='profile'),
	path('self/<slug:slug>', ProfileUpdateView.as_view(success_url='/'), name='self_profile')
]
