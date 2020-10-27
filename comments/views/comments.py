"""Comment views."""

# Python
# import pdb

# Django
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import redirect

# Pyrty
from comments.forms import CommentForm, CommentVoteForm
from comments.models import Comment
from comments.views import create_notification
from profiles.utils import run_reputation_update


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
