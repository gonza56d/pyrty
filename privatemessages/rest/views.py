"""PrivateMessage REST views."""

# Django
from django.db.models import Q
from django.shortcuts import get_object_or_404

# Django REST Framework
from rest_framework import viewsets
from rest_framework.response import Response

# Pyrty
from privatemessages.models import PrivateMessage
from privatemessages.rest.serializers import PrivateMessageSerializer


class PrivateMessageViewSet(viewsets.ModelViewSet):

	serializer_class = PrivateMessageSerializer

	def list(self, request):
		queryset = PrivateMessage.objects.filter(
			Q(origin_user=request.user) |
			Q(target_user=request.user)
		)
		serializer = PrivateMessageSerializer(queryset, many=True)
		return Response(serializer.data)

	def retrieve(self, request, pk=None):
		queryset = PrivateMessage.objects.filter(
			Q(origin_user=request.user) |
			Q(target_user=request.user)
		)
		private_message = get_object_or_404(queryset, pk=pk)
		serializer = PrivateMessageSerializer(queryset)
		return Response(serializer.data)
