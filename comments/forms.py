"""Comment forms."""

# Django
from django import forms

# Pyrty
from comments.models import Comment


class CommentForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(CommentForm, self).__init__(*args, **kwargs)
		self.fields['content'].widget = forms.Textarea(attrs={'class': 'form-control'})
		self.fields['content'].label = 'Message'

	class Meta:
		model = Comment
		fields = ['content']
