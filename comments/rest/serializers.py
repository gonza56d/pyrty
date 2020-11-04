"""Comment serializers."""

# Django REST Framework
from rest_framework import serializers

# Pyrty
from comments.models import Comment
from profiles.views import run_reputation_update


class CommentVoteSerializer(serializers.Serializer):
    """Serializer for comment votes."""

    positive = serializers.BooleanField()
    comment_id = serializers.IntegerField()


class CommentSerializer(serializers.ModelSerializer):
	"""Comment model serializer."""

	user = serializers.PrimaryKeyRelatedField(read_only=True)

	class Meta:
		model = Comment
		fields = ['id', 'user', 'post', 'content', 'created', 'score']

	def create(self, validated_data):
		"""Create a new comment in some post, by request.user."""

		validated_data['user'] = self.context['request'].user
		result = super().create(validated_data)
		run_reputation_update(validated_data['user'])
		return result
