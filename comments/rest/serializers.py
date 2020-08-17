"""Comment serializers."""

# Django REST Framework
from rest_framework import serializers

# Pyrty
from comments.models import Comment


class CommentSerializer(serializers.ModelSerializer):
	"""Comment model serializer."""

	class Meta:
		model = Comment
		fields = '__all__'
