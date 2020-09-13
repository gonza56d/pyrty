"""Comment views."""

# Python
# import pdb

# Django
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import redirect
from django.urls import reverse

# Pyrty
from comments.forms import CommentForm, CommentVoteForm
from comments.models import Comment
from notifications.models import Notification
from profiles.utils import run_reputation_update
from users.models import User


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


def delete_comment(request):
	"""Delete comment view."""
	if request.method == 'POST':
		try :
			comment = Comment.objects.get(id=request.POST.get('id'), user=request.user)
			comment.delete()
			run_reputation_update(request.user)
			return JsonResponse({'status': 200, 'message': 'Comment deleted'})
		except ObjectDoesNotExist:
			return JsonResponse({'status': 404, 'message': 'Comment not found'})
	else:
		return JsonResponse({'status': 405, 'message': 'Method not allowed'})
	return JsonResponse({'status': 400, 'message': 'Bad request'})


def create_notification(request, form):
	"""Create a notification from a new comment."""
	# validate comment user is not the same than post user
	post = form.cleaned_data.get('post')
	if request.user != User.objects.get(pk=post.user.id):
		notification = Notification()
		notification.origin_user = request.user
		notification.target_user = User.objects.get(pk=post.user.id)
		notification.message = "{} commented in your post: '{}'".format(request.user, post.title)
		notification.url = reverse('post', args=[post.id])
		notification.save()


def submit_vote(request):
	"""Receive and validate vote request."""

	if not request.user.is_authenticated:
		return redirect('signup')

	if request.method == 'POST':
		form = CommentVoteForm(comment_id=request.POST['comment_id'], data=request.POST, user=request.user)
		if form.is_valid():
			form.submit_vote(request.user)
		return redirect('post', pk=request.POST['post_id'])
