"""PrivateMessage REST views."""

# Django REST Framework
from rest_framework import viewsets

# Pyrty
from privatemessages.rest.serializers import PrivateMessageSerializer


class PrivateMessageViewSet(viewsets.ModelViewSet):

	serializer_class = PrivateMessageSerializer

	# TODO
