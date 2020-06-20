"""User auth backends."""

# Python
# import pdb

# Django
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

# Pyrty
UserModel = get_user_model()


class UserBackend(ModelBackend):
	"""Auth against settings.USER_AUTH_MODEL.

	Override the authentication method in order to be able to authenticate with email or username.
	"""

	def authenticate(self, request, username=None, password=None, **kwargs):
		if username is None:
			username = kwargs.get(UserModel.USERNAME_FIELD)
		if username is None or password is None:
			return
		try:
			user = UserModel._default_manager.get_by_natural_key(username)
		except UserModel.DoesNotExist:
			try:
				user = UserModel._default_manager.get(username=username)
			except UserModel.DoesNotExist:
				# Run the default password hasher once to reduce the timing
				# difference between an existing and a nonexistent user (#20760).
				UserModel().set_password(password)
		if user.check_password(password) and self.user_can_authenticate(user):
			return user
