"""User urls."""

# Django
from django.urls import path

# Pyrty
from users.rest.views import oauth
from users.views import edit_user_options, logout_view, login_view, SignUp


urlpatterns = [
	path('login/', login_view, name='login'),
	path('logout/', logout_view, name='logout'),
	path('signup/', SignUp.as_view(), name='signup'),
	path('oauth/', oauth, name='oauth'),
	path('edit_user_options/', edit_user_options, name='edit_user_options'),
]
