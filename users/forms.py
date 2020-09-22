"""User forms."""

# Python
import pdb

# Django
from django import forms
from django.utils.translation import gettext_lazy as _

# Pyrty
from users.models import User, SUMMARY_REPORTS_CHOICES


class LoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username or email'}))
	password = forms.CharField(widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))


class SignUpForm(forms.ModelForm):
	"""Users' registration."""

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)
		self.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
		self.fields['email'].widget = forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
		self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})

	class Meta:
		model = User
		fields = ['username', 'email', 'password']


class UserConfigurationsForm(forms.ModelForm):
	"""User summary reports interval configuration."""

	def __init__(self, *args, **kwargs):
		super(UserConfigurationsForm, self).__init__(*args, **kwargs)
		self.fields['summary_reports'].widget = forms.Select(
			attrs={'class': 'form-control'},
			choices=SUMMARY_REPORTS_CHOICES
		)
		self.fields['summary_reports'].label = _('user_configurations_form')

	class Meta:
		model = User
		fields = ['summary_reports',]
