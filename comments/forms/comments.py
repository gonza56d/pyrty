"""Comment forms."""

# Python
# import pdb

# Django
from django import forms

# Pyrty
from comments.models import Comment
from posts.models import Post


class CommentForm(forms.ModelForm):
	"""Form to create a new comment."""

	def __init__(self, post, *args, **kwargs):
		"""Init form with comment's post to set ready for create. Pass None
		when handling a post method."""

		super(CommentForm, self).__init__(*args, **kwargs)

		if post is not None:
			self.fields['post'] = forms.ModelChoiceField(
				queryset=Post.objects.filter(id=post.id),
				empty_label=None,
				widget=forms.Select(attrs={'style': 'display:none;'})
			)

	class Meta:
		model = Comment
		fields = ['post', 'content']
