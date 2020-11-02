"""Forum REST views."""

# Django
from django.shortcuts import get_object_or_404

# Django REST Framework
from rest_framework import viewsets
from rest_framework.response import Response

# Pyrty
from forums.models import Forum
from forums.rest.serializers import ForumSerializer


class ForumViewSet(viewsets.ModelViewSet):
    """Forum model viewset."""
    
    serializer_class = ForumSerializer
    
    def list(self, queryset):
        """List all the forums."""
        queryset = Forum.objects.all()
        serializer = ForumSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        """Retrieve a forum."""
        queryset = Forum.objects.all()
        forum = get_object_or_404(queryset, pk=pk)
        serializer = ForumSerializer(forum)
        return Response(serializer.data)
