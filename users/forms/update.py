"""User update forms."""

# Python
# import pdb

# Django
from django import forms
from django.utils.translation import gettext_lazy as _

# Pyrty
from users.models import User, SUMMARY_REPORTS_CHOICES


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
