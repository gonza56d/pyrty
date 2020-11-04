"""Comment rest api views."""

# Python
import pdb

# Django
from django.db.models import Prefetch

# Django REST Framework
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.serializers import ValidationError
from rest_framework import viewsets
from rest_framework.response import Response

# Pyrty
from comments.models import Comment
from comments.rest.serializers import CommentSerializer, CommentVoteSerializer
from profiles.views import run_reputation_update
from users.models import User
from utils import vote_manager


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def submit_vote(request):
    """Receive vote submit from POST request."""

    # Serialize and validate
    serialized_data = CommentVoteSerializer(data=request.data)
    if not serialized_data.is_valid():
        return Response(data=serialized_data.errors )
    
    # Get user and comment with user's vote if it has
    user_queryset = User.objects.filter(username=request.user.username)
    positive_vote_prefetch = Prefetch(
        'positive_votes', queryset=user_queryset, to_attr='user_positive_vote'
    )
    negative_vote_prefetch = Prefetch(
        'negative_votes', queryset=user_queryset, to_attr='user_negative_vote'
    )
    comment = Comment.objects.prefetch_related(positive_vote_prefetch)\
        .prefetch_related(negative_vote_prefetch).get(pk=request.data['comment_id'])
    
    # Validate vote it's not by request.user
    if comment.user.id == request.user.id:
        return Response(data={'status': status.HTTP_403_FORBIDDEN,
        'message': 'User cannot vote its self comments.'})
    
    # Send comment instance and vote value for handling
    positive = serialized_data.data['positive']
    vote_manager.handle(positive, comment, request.user)
    serializer = CommentSerializer(comment)
    return Response(data=serializer.data)


class CommentViewSet(viewsets.ModelViewSet):
    
    serializer_class = CommentSerializer
    
    def get_queryset(self):
        """Filter by post__id or list all the comments."""
        queryset = Comment.objects.all()
        post__id = self.request.query_params.get('post_id', None)
        if post__id is not None:
            queryset = queryset.filter(post__id=post__id)
        return queryset
    
    def get_permissions(self):
        permissions = []
        if self.action == 'create' or self.action == 'destroy':
            permissions.append(IsAuthenticated)
        return [p() for p in permissions]
        
    def retrieve(self, request, pk=None):
        """Retrieve a comment."""
        queryset = Comment.objects.all()
        comment = get_object_or_404(queryset, pk=pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        """Delete a comment created by request.user from a post."""
        
        instance = self.get_object()
        if instance.user != request.user:
            raise ValidationError('Comment does not belong to the authenticated user.')
        self.perform_destroy(instance)
        run_reputation_update(request.user)
        return Response(status=status.HTTP_204_NO_CONTENT)
