"""Post positive and negative votes forms."""

# Python
import pdb

# Django
from django import forms
from django.core.exceptions import ValidationError
from django.db.models import Prefetch

# Pyrty
from posts.models import Post
from profiles.utils import run_reputation_update
from users.models import User
from utils import vote_manager


class PostVoteForm(forms.Form):
    """Form for post vote submit."""

    post = forms.ModelChoiceField(queryset=Post.objects.all())
    positive = forms.BooleanField()
    user = None

    def __init__(self, post_id=None, positive=None, user=None, *args, **kwargs):
        """
        Init with post's id to vote, and positive=True/False for voting value.
        """

        super(PostVoteForm, self).__init__(*args, **kwargs)

        self.fields['post'] = forms.ModelChoiceField(
            queryset=Post.objects.filter(id=post_id),
            empty_label=None,
            required=True
        )
        self.fields['positive'] = forms.BooleanField(
            initial=positive,
            required=False
        )
        self.user = user

    def clean(self):
        cd = self.cleaned_data
        post = cd.get('post')
        if post.user == self.user:
            raise ValidationError("Voting your own post is not allowed")

    def submit_vote(self, user):
        """Submit user vote for a post."""

        # get variables
        cd = self.cleaned_data
        post, positive = cd.get('post'), cd.get('positive')

        user_queryset = User.objects.filter(username=user.username)

        prefetch_positive = Prefetch('positive_votes', queryset=user_queryset, 
            to_attr='user_positive_vote')

        prefetch_negative = Prefetch('negative_votes', queryset=user_queryset, 
            to_attr='user_negative_vote')

        instance = Post.objects.prefetch_related(prefetch_positive)\
            .prefetch_related(prefetch_negative).select_related('user').get(pk=post.id)

        # vote submit
        vote_manager.handle(positive, instance, user)

        # profile score update
        run_reputation_update(instance.user)
