"""Profile utils."""

# Python
# import pdb

# Pyrty
from comments.models import Comment
from posts.models import Post
from profiles.models import Profile


def run_reputation_update(user):
    """Recalculate and update user profile's reputation.

    Count posts, comments, and received votes, then sum them to get the new reputation score.
    """

    posts = Post.objects.prefetch_related('positive_votes')\
        .prefetch_related('negative_votes').filter(user=user)

    comments = Comment.objects.prefetch_related('positive_votes')\
        .prefetch_related('negative_votes').filter(user=user)

    n_posts = posts.count()
    n_comments = comments.count()
    n_positive_votes = (
        sum([post.positive_votes.count() for post in posts]) +
        sum([comment.positive_votes.count() for comment in comments])
    )
    n_negative_votes = (
        sum([post.negative_votes.count() for post in posts]) +
        sum([comment.negative_votes.count() for comment in comments])
    )

    score = n_posts * 20 + n_comments * 5 + n_positive_votes * 3 - n_negative_votes * 3

    profile = Profile.objects.filter(user=user).update(reputation=score)
