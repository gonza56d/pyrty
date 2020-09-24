"""PrivateMessage serializers."""

# Django REST Framework
from rest_framework import serializers

# Pyrty
from privatemessages.models import PrivateMessage


class PrivateMessageSerializer(serializers.ModelSerializer):

	origin_user = serializers.PrimaryKeyRelatedField(read_only=True)

	class Meta:
		model = PrivateMessage
		fields = '__all__'

	def create(self, validated_data):
		"""Create a new PrivateMessage by user in session."""

		validated_data['origin_user'] = self.context['request'].user
		return super().create(validated_data)
