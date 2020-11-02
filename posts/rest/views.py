"""Post rest api views."""

# Django REST Framework
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.serializers import ValidationError
from rest_framework import viewsets
from rest_framework.response import Response

# Pyrty
from posts.models import Post
from posts.rest.serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):

    serializer_class = PostSerializer

    def get_queryset(self):
        """Filter by subforum__id or list all the posts."""
        queryset = Post.objects.all()
        subforum_id = self.request.query_params.get('subforum_id', None)
        if subforum_id is not None:
            queryset = queryset.filter(subforum__id=subforum_id)
        return queryset
    
    def list(self, queryset):
        """List all the obtained posts."""
        serializer = PostSerializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    def get_permissions(self):
        permissions = []
        if self.action == 'create' or self.action == 'destroy':
            permissions.append(IsAuthenticated())
        return permissions

    def get_object(self):
        """Return post by primary key."""
        return get_object_or_404(Post, id=self.kwargs['pk'])

    def destroy(self, request, *args, **kwargs):
        """Delete a post created by request.user."""
        instance = self.get_object()
        if instance.user != request.user:
            raise ValidationError('Post does not belong to the authenticated user.')
        self.perform_destroy(instance)
        run_reputation_update(request.user)
        return Response(status=status.HTTP_204_NO_CONTENT)
