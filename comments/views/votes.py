"""Comment vote views."""

# Django
from django.shortcuts import redirect

# Pyrty
from comments.forms import CommentVoteForm


def submit_vote(request):
	"""Receive and validate vote request."""

	if request.method == 'POST':
		form = CommentVoteForm(comment_id=request.POST['comment_id'],
                               data=request.POST, user=request.user)
		if form.is_valid():
			form.submit_vote(request.user)
		return redirect('post', pk=request.POST['post_id'])
