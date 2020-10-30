"""Comment vote views."""

# Pyrty
from comments.forms import CommentVoteForm


def submit_vote(request):
	"""Receive and validate vote request."""

	if not request.user.is_authenticated:
		return redirect('signup')

	if request.method == 'POST':
		form = CommentVoteForm(comment_id=request.POST['comment_id'],
                               data=request.POST, user=request.use)
		if form.is_valid():
			form.submit_vote(request.user)
		return redirect('post', pk=request.POST['post_id'])