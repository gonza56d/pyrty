"""Comment views."""

# Python
# import pdb

# Django
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse

# Pyrty
from comments.forms import CommentVoteForm
from comments.models import Comment
from comments.views import create_notification
from profiles.views import run_reputation_update


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
