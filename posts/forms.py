"""Post positive and negative votes forms."""

# Python
import pdb

# Django
from django import forms
from django.db.models import Prefetch

# Pyrty
from posts.models import Post


class PostVoteForm(forms.Form):
    """Form for post vote submit."""

    def __init__(self, post_id=None, positive=None, *args, **kwargs):
        """Init with post's id to vote, and positive=True/False for voting value."""

        super(PostVoteForm, self).__init__(*args, **kwargs)

        self.fields['post'] = forms.ModelChoiceField(
            queryset=Post.objects.filter(id=post_id),
            empty_label=None,
            required=True
        )
        self.fields['positive'] = forms.BooleanField(
            initial=positive,
            required=True
        )

    post = forms.ModelChoiceField(queryset=Post.objects.all())
    positive = forms.BooleanField()

    def submit_vote(self, user):
        post, positive = self.cleaned_data.get('post'), self.cleaned_data.get('positive')
        user_queryset = User.objects.filter(username=self.request.user.username)

        prefetch_positive = Prefetch('positive_votes', queryset=user_queryset, to_attr='user_positive_vote')
        prefetch_negative = Prefetch('negative_votes', queryset=user_queryset, to_attr='user_negative_vote')

        existing = Post.objects.prefetch_related(prefetch_positive).prefetch_related(prefetch_negative).get(pk=post.id)

        if positive and positive_vote.delete():
            return

        
        negative_vote = Post.objects.prefetch_related(prefetch_negative).user_negative_vote

        if not positive and negative_vote.delete():
            return
        
        positive_vote.delete()
        negative_vote.delete()#TODO


