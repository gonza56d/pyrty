"""Comment views."""

# Python
import pdb

# Django
from django.shortcuts import redirect

# Pyrty
from comments.forms import CommentForm
from comments.models import Comment


def create_comment(request):
	"""Create a comment view."""
	if request.method == 'POST':
		form = CommentForm(None, data=request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.user = request.user
			comment.save()
		return redirect('post', pk=int(request.POST['post']))
