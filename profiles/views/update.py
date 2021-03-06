"""Profile update views."""

# Python
# import pdb

# Django
from django import forms
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic.edit import UpdateView

# Pyrty
from comments.models import Comment
from posts.models import Post
from privatemessages.forms import PrivateMessageForm
from profiles.models import Profile
from summaryreports.models import SummaryReport
from users.forms import UserConfigurationsForm
from users.models import User


class ProfileUpdateView(UpdateView):
    """Display own user's profile info and handle update."""
    
    model = Profile
    fields = ['first_name', 'last_name', 'birthday', 'bio']
    
    def get_object(self, queryset=None):
        """Override to select related user."""
        
        return Profile.objects.select_related('user').get(
			slug=self.kwargs.get(self.slug_url_kwarg)
        )
    
    def get_form(self, form_class=None):
        """Set widgets for form and initialy disable each field."""
        
        form = super(UpdateView, self).get_form(form_class)
        
        form.fields['first_name'].label = _('First name')
        form.fields['first_name'].widget = forms.TextInput(
			attrs={'class': 'form-control', 'disabled': ''}
		)
        form.fields['last_name'].label = _('Last name')
        form.fields['last_name'].widget = forms.TextInput(
			attrs={'class': 'form-control', 'disabled': ''}
		)
        form.fields['birthday'].label = _('Birthday')
        form.fields['birthday'].widget = forms.DateInput(
			attrs={'class': 'form-control', 'disabled': '', 'type': 'date'}
		)
        form.fields['bio'].label = _('Bio')
        form.fields['bio'].widget = forms.Textarea(
			attrs={'class': 'form-control', 'disabled': '', 'rows': '5'}
		)
        return form
    
    def get_success_url(self):
        """Redirect to own profile on update success."""
        return reverse('self_profile', args=[self.request.user])
    
    def get(self, request, *args, **kwargs):
        """Redirect to ProfileDetailView if the requested profile is not request.user."""
        user = None
        try:
            user = User.objects.get(username=self.kwargs['slug'])
        finally:
            if request.user != user:
                return redirect('profile', slug=self.kwargs['slug'])
            self.object = self.get_object()
            return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        """Load profile's last posts and comments."""
        context = super().get_context_data(**kwargs)

        user = self.object.user

        context['has_summary_reports'] = SummaryReport.objects.filter(user=user).exists()

        context['user_configurations_form'] = UserConfigurationsForm(
			initial={'summary_reports': user.summary_reports}
        )
        context['profile_posts'] = Post.objects.select_related('subforum__forum')\
			.filter(user=user)[:10]

        context['profile_comments'] = Comment.objects.filter(user=user)[:10]
        return context
