"""User authentication forms."""

# Django
from django.forms import Form, ModelForm
from django.utils.translation import gettext_lazy as _

# Pyrty
from users.models import User
from utils.forms import IconCharField, IconEmailField, IconPasswordField, TextArea


class LoginForm(Form):
	username = IconCharField(placeholder=_('Username or email'), icon='fas fa-user')
	password = IconPasswordField(placeholder=_('Password'), icon='fas fa-key')


class SignUpForm(ModelForm):
	"""Users' registration."""

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)
		self.fields['username'] = IconCharField(placeholder=_('Username'), icon='fas fa-user')
		self.fields['email'] = IconEmailField(placeholder=_('Email'), icon='fas fa-at')
		self.fields['password'] = IconPasswordField(placeholder=_('Password'), icon='fas fa-key')

	class Meta:
		model = User
		fields = ['username', 'email', 'password']

