"""Comment serializers."""

# Python
# import pdb

# Django
from django.core.exceptions import ObjectDoesNotExist

# Django REST Framework
from rest_framework import serializers

# Pyrty
from comments.models import Comment


class CommentSerializer(serializers.ModelSerializer):
	"""Comment model serializer."""

	user = serializers.PrimaryKeyRelatedField(read_only=True)

	class Meta:
		model = Comment
		fields = '__all__'

	def create(self, validated_data):
		"""Create a new comment in some post, by request.user."""

		validated_data['user'] = self.context['request'].user
		return super().create(validated_data)

	def list(self, request):
		"""List all the comments from some post."""

		if 'post' not in request.query_params:
			raise ValidationError('Post id must be provided.')

		q = self.queryset.filter(post=request.query_params['post'])
		serializer = CommentSerializer(q, many=True)
		return Response(serializer.data)
