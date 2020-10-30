"""User authentication forms."""

# Django
from django.forms import Form, ModelForm
from django.utils.translation import gettext_lazy as _

# Pyrty
from users.models import User
from utils.forms import IconCharField, IconPasswordField, TextArea


class LoginForm(Form):
	username = IconCharField(placeholder='Username or email', icon='fas fa-user')
	password = IconPasswordField(placeholder='Password', icon='fas fa-key')


class SignUpForm(ModelForm):
	"""Users' registration."""

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)
		self.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
		self.fields['email'].widget = forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
		self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})

	class Meta:
		model = User
		fields = ['username', 'email', 'password']

