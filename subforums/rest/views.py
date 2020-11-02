"""Subforum REST views."""

# Django
from django.shortcuts import get_object_or_404

# Django REST Framework
from rest_framework import viewsets
from rest_framework.response import Response

# Pyrty
from subforums.models import Subforum
from subforums.rest.serializers import SubforumSerializer


class SubforumViewSet(viewsets.ModelViewSet):
    """Subforum model viewset."""

    serializer_class = SubforumSerializer

    def get_queryset(self):
        """Filter by forum__id or list all the subforums."""
        queryset = Subforum.objects.all()
        forum_id = self.request.query_params.get('forum_id', None)
        if forum_id is not None:
            queryset = queryset.filter(forum__id=forum_id)
        return queryset

    def list(self, queryset):
        """List all the obtained subforums."""
        serializer = SubforumSerializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """Retrieve a subforum."""
        queryset = Subforum.objects.all()
        forum = get_object_or_404(queryset, pk=pk)
        serializer = SubforumSerializer(forum)
        return Response(serializer.data)
