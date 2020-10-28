"""User update views."""

# Django
from django.shortcuts import redirect

# Pyrty
from users.forms import UserConfigurationsForm


def edit_user_options(request):
	if request.method == 'POST':
		form = UserConfigurationsForm(data=request.POST)
		if form.is_valid():
			summary_reports = form.cleaned_data.get('summary_reports')
			request.user.summary_reports = summary_reports
			request.user.save()
			return redirect('self_profile', slug=request.user)
