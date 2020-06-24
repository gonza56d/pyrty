"""Comment forms."""

# Python
# import pdb

# Django
from django import forms

# Pyrty
from comments.models import Comment
from posts.models import Post


class CommentForm(forms.ModelForm):
	def __init__(self, post, *args, **kwargs):
		super(CommentForm, self).__init__(*args, **kwargs)

		if post is not None:
			self.fields['post'] = forms.ModelChoiceField(
				queryset=Post.objects.filter(id=post.id),
				empty_label=None,
				widget=forms.Select(attrs={'style': 'display:none;'})
			)

		self.fields['content'].widget = forms.Textarea(attrs={'class': 'form-control'})

	class Meta:
		model = Comment
		fields = ['post', 'content']
