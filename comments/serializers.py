"""Comment serializers."""

# Django REST Framework
from rest_framework import serializers

# Pyrty
from commments.models import Comment


class CreateCommentSerializer(serializers.ModelSerializer):
	"""Create comment serializer."""

	class Meta:
		model = Comment
		fields = ['user', 'post', 'content']
