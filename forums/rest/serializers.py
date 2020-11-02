"""Forum serializers."""

# Django REST Framework
from rest_framework import serializers

# Pyrty
from forums.models import Forum


class ForumSerializer(serializers.ModelSerializer):
    """Forum model serializer."""

    class Meta:
        model = Forum
        fields = '__all__'
