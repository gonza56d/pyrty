"""Subforum serializers."""

# Django REST Framework
from rest_framework import serializers

# Pyrty
from subforums.models import Subforum


class SubforumSerializer(serializers.ModelSerializer):
    """Subforum model serializer."""

    class Meta:
        model = Subforum
        fields = '__all__'
