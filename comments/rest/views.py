"""Comment rest api views."""

# Python
import pdb

# Django REST Framework
from rest_framework import status
from rest_framework.serializers import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response

# Pyrty
from comments.models import Comment
from comments.rest.serializers import CommentSerializer


class ListComments(APIView):
	"""List all the comments from a post."""

	def get(self, request, format=None):

		if 'post' not in request.query_params:
			raise ValidationError('Post id must be provided.')

		q = Comment.objects.filter(post=request.query_params['post'])
		serializer = CommentSerializer(q, many=True)
		return Response(serializer.data)
