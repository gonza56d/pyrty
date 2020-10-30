"""Comment rest api views."""

# Python
# import pdb

# Django REST Framework
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.serializers import ValidationError
from rest_framework import viewsets
from rest_framework.response import Response

# Pyrty
from comments.models import Comment
from comments.rest.serializers import CommentSerializer
from profiles.views import run_reputation_update


class CommentViewSet(viewsets.ModelViewSet):

	serializer_class = CommentSerializer
	queryset = Comment.objects.all()

	def get_permissions(self):
		permissions = []
		if self.action == 'create' or self.action == 'destroy':
			permissions.append(IsAuthenticated)
		return [p() for p in permissions]

	def get_object(self):
		"""Return comment by primary key."""
		return get_object_or_404(Comment, id=self.kwargs['pk'])

	def destroy(self, request, *args, **kwargs):
		"""Delete a comment created by request.user from a post."""

		instance = self.get_object()
		if instance.user != request.user:
			raise ValidationError('Comment does not belong to the authenticated user.')
		self.perform_destroy(instance)
		run_reputation_update(request.user)
		return Response(status=status.HTTP_204_NO_CONTENT)

	def retrieve(self, request, pk=None):
		pass

	def update(self, request, pk=None):
		pass

	def partial_update(self, request, pk=None):
		pass
