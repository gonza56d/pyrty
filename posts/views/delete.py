"""Delete post views."""

# Django
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.shortcuts import redirect

# Pyrty
from posts.models import Post
from profiles.views.utils import run_reputation_update


@login_required
def delete_post(request):
	"""Post delete request."""

	if request.method == 'POST':
		post = Post.objects.get(id=request.POST['delete_post_id'])
		
		if post.user == request.user:
			post.delete()
			run_reputation_update(request.user)
			return redirect('forums')
		else:
			raise ValidationError("Deletion of other users' posts is not allowed")
