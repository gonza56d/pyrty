"""Profile detail views."""

# Django
from django.shortcuts import redirect
from django.views.generic.detail import DetailView

# Pyrty
from comments.models import Comment
from posts.models import Post
from privatemessages.forms import PrivateMessageForm
from profiles.models import Profile
from users.models import User


class ProfileDetailView(DetailView):
    """Display third users' profile info."""
    
    model = Profile
    
    def get_object(self, queryset=None):
        """Override to select related user."""
        
        return Profile.objects.select_related('user').get(
            slug=self.kwargs.get(self.slug_url_kwarg)
        )
    
    def get(self, request, *args, **kwargs):
        """Redirect to ProfileUpdateView if the requested profile is the same than request.user."""
        user = None
        try:
            user = User.objects.get(username=self.kwargs['slug'])
        finally:
            if request.user == user:
                return redirect('self_profile', slug=self.kwargs['slug'])
            self.object = self.get_object()
            context = self.get_context_data(object=self.object)
            return self.render_to_response(context)
    
    def get_context_data(self, **kwargs):
        """Load private message form, and profile's last posts and comments."""
        
        context = super().get_context_data(**kwargs)
        context['private_message_form'] = PrivateMessageForm(
            target_user=User.objects.get(username=self.kwargs['slug'])
        )
        context['profile_posts'] = Post.objects.select_related('subforum__forum').filter(
			user=context['object'].user
		)[:10]
        context['profile_comments'] = Comment.objects.select_related('post').filter(
			user=context['object'].user
		)[:10]
        return context
