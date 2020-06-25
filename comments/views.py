"""Comment views."""

# Python
import pdb

# Django
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.shortcuts import redirect

# Pyrty
from comments.forms import CommentForm
from comments.models import Comment


def create_comment(request):
	"""Create comment view."""
	if request.method == 'POST':
		form = CommentForm(None, data=request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.user = request.user
			comment.save()
		return redirect('post', pk=int(request.POST['post']))


def delete_comment(request):
	"""Delete comment view."""
	if request.method == 'POST':
		try :
			comment = Comment.objects.get(id=request.POST.get('id'), user=request.user)
			comment.delete()
			return JsonResponse({'status': 200, 'message': 'Comment deleted'})
		except ObjectDoesNotExist:
			return JsonResponse({'status': 404, 'message': 'Comment not found'})
	else:
		return JsonResponse({'status': 405, 'message': 'Method not allowed'})
	return JsonResponse({'status': 400, 'message': 'Bad request'})
