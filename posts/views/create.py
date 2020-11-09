"""Create post views."""

# Python
import json

# Django
from django import forms
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.shortcuts import redirect
from django.views.generic.edit import CreateView
from django_quill.forms import QuillFormField

# Pyrty
from posts.models import Post
from profiles.views import run_reputation_update
from subforums.models import Subforum


class CreatePost(CreateView):
    """Create a new post view."""
    
    model = Post
    subforum = None  # used to set post's subforum
    
    fields = ['subforum', 'title', 'content']
    
    def get_success_url(self):
        return reverse('subforum', args=[self.kwargs['subforum_id']])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subforum'] = self.subforum  # used as url parameter
        return context
    
    def get_form(self, form_class=None):
        """Init form by hiding subforum option and leaving current subforum 
        as the only choice."""
        
        form = super(CreatePost, self).get_form(form_class)
        
        form.fields['subforum'] = forms.ModelChoiceField(
			queryset=Subforum.objects.filter(pk=self.subforum.id),
			empty_label=None,
			label = '',
			widget = forms.Select(attrs={'class': 'form-control', 'style': 'display:none;'})
		)
        form.fields['title'].label = _('Title')
        form.fields['title'].widget = forms.TextInput(
			attrs={'class': 'form-control my-2', 'placeholder': _('Title')}
		)
        form.fields['content'] = QuillFormField()
        form.fields['content'].label = _('Content')
        return form
        
    def get(self, request, *args, **kwargs):
        """Handle GET request and populate Subforum object."""
        self.subforum = Subforum.objects.get(pk=self.kwargs['subforum_id'])
        return super().get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        """Handle POST request and create a new Post object."""
        self.subforum = Subforum.objects.get(pk=self.kwargs['subforum_id'])
        form = self.get_form()
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.content = json.loads(form.cleaned_data.get('content'))['html']  # Quill form field's html
            post.save()
            run_reputation_update(request.user)
            return redirect('post', pk=post.id)
        return super().post(request, *args, **kwargs)
    
