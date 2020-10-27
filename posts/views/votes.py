"""Post vote views."""

# Django
from django.shortcuts import redirect

# Pyrty
from posts.forms import PostVoteForm


@login_required
def submit_vote(request):
	"""Receive and validate vote request."""

	if request.method == 'POST':
		form = PostVoteForm(
			post_id=request.POST['post'], data=request.POST, user=request.user
		)
		if form.is_valid():
			form.submit_vote(request.user)
		return redirect('post', pk=request.POST['post'])
