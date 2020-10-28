"""Create comment views."""

# Django
from django.db import transaction
from django.shortcuts import redirect

# Pyrty
from comments.forms import CommentForm
from comments.views import create_notification
from notifications.tasks import create_notification
from profiles.views import run_reputation_update


def create_comment(request):
	"""Create comment view."""
	if request.method == 'POST':
		form = CommentForm(None, data=request.POST)
		if form.is_valid():
			with transaction.atomic():
				comment = form.save(commit=False)
				comment.user = request.user
				form.save()
				create_notification(request, form)
				run_reputation_update(request.user)
		return redirect('post', pk=request.POST['post'])
