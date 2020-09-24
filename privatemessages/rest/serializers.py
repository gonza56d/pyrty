"""PrivateMessage serializers."""

# Python
# import pdb

# Django REST Framework
from rest_framework import serializers

# Pyrty
from privatemessages.models import PrivateMessage
from privatemessages import tasks


class PrivateMessageSerializer(serializers.ModelSerializer):

	origin_user = serializers.PrimaryKeyRelatedField(read_only=True)

	class Meta:
		model = PrivateMessage
		fields = '__all__'

	def create(self, validated_data):
		"""Create a new PrivateMessage by user in session."""

		validated_data['origin_user'] = self.context['request'].user
		serializable = validated_data.copy()

		serializable['origin_user'] = validated_data['origin_user'].id
		serializable['target_user'] = validated_data['target_user'].id

		tasks.send_private_message.delay(serializable)
		return validated_data
