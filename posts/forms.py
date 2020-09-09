"""Post positive and negative votes forms."""

# Python
import pdb

# Django
from django import forms
from django.db.models import Prefetch

# Pyrty
from posts.models import Post
from users.models import User


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
            required=False
        )

    post = forms.ModelChoiceField(queryset=Post.objects.all())
    positive = forms.BooleanField()

    def submit_vote(self, user):
        """Handle user vote request

        Vote can be either positive or negative.
        If a vote of the same type (negative/positive) already exists for this post
        and user, delete and exit function.
        If a vote of the contrary type already exists for this post and user,
        delete the contrary vote and create the submit type.
        """

        post, positive = self.cleaned_data.get('post'), self.cleaned_data.get('positive')
        user_queryset = User.objects.filter(username=user.username)
        prefetch_positive = Prefetch('positive_votes', queryset=user_queryset, to_attr='user_positive_vote')
        prefetch_negative = Prefetch('negative_votes', queryset=user_queryset, to_attr='user_negative_vote')
        existing = Post.objects.prefetch_related(prefetch_positive).prefetch_related(prefetch_negative).get(pk=post.id)

        if positive and len(existing.user_positive_vote) > 0:
            # positive vote delete request
            return existing.positive_votes.remove(user)
        elif not positive and len(existing.user_positive_vote) > 0:
            # negative vote create request and existing positive vote
            existing.positive_votes.remove(user)

        if not positive and len(existing.user_negative_vote) > 0:
            # negative vote delete request
            return existing.negative_votes.remove(user)
        elif positive and len(existing.user_negative_vote) > 0:
            # positive vote create request and existing negative vote
            existing.negative_votes.remove(user)

        # create correspondent vote after deletion check
        if positive:
            existing.positive_votes.add(user)
        elif not positive:
            existing.negative_votes.add(user)
