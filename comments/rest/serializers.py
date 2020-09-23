"""Comment serializers."""

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
