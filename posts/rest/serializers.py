"""Post serializers."""

# Django REST Framework
from rest_framework import serializers

# Pyrty
from posts.models import Post
from profiles.utils import run_reputation_update


class PostSerializer(serializers.ModelSerializer):

    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'user', 'subforum', 'title', 'content']

    def create(self, validated_data):
        """Create a new Post by user in session."""

        validated_data['user'] = self.context['request'].user
        result = super().create(validated_data)
        run_reputation_update(self.context['request'].user)
        return result
