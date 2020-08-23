"""Comment rest api views."""

# Python
import pdb

# Django REST Framework
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.serializers import ValidationError
from rest_framework import viewsets
from rest_framework.response import Response

# Pyrty
from comments.models import Comment
from comments.rest.serializers import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):

	serializer_class = CommentSerializer
	queryset = Comment.objects.all()

	def get_permissions(self):
		permissions = []
		if self.action == 'create':
			permissions.append(IsAuthenticated)
		return [p() for p in permissions]

	def list(self, request):
		"""List all the comments from some post."""

		if 'post' not in request.query_params:
			raise ValidationError('Post id must be provided.')

		q = self.queryset.filter(post=request.query_params['post'])
		serializer = CommentSerializer(q, many=True)
		return Response(serializer.data)

	def retrieve(self, request, pk=None):
		pass

	def update(self, request, pk=None):
		pass

	def partial_update(self, request, pk=None):
		pass

	def destroy(self, request, pk=None):
		pass
