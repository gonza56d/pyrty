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
    queryset = Post.objects.all()

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
