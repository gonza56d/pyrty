"""Create comment views."""

# Python
import json

# Django
from django.db import transaction
from django.shortcuts import redirect, reverse
from django.utils.translation import gettext as _

# Pyrty
from comments.forms import CommentForm
from notifications.models import Notification
from profiles.views import run_reputation_update
from users.models import User


def create_comment(request):
    """Create comment view."""
    if request.method == 'POST':
        form = CommentForm(None, data=request.POST)
        if form.is_valid():
            with transaction.atomic():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.content = json.loads(form.cleaned_data.get('content'))['html']  # Quill form field's html
                form.save()
                create_notification(request, form)
                run_reputation_update(request.user)
        return redirect('post', pk=request.POST['post'])


def create_notification(request, form):
	"""Create a new notification for the post's author about new comment."""
	# validate comment user is not the same than post user
	post = form.cleaned_data.get('post')
	if request.user != User.objects.get(pk=post.user.id):
		notification = Notification()
		notification.origin_user = request.user
		notification.target_user = User.objects.get(pk=post.user.id)
		notification.message = f'@{request.user} ' + _('commented in your post:') + f' {post.title}'
		notification.url = reverse('post', args=[post.id])
		notification.save()
