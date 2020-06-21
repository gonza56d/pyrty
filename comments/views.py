"""Comment views."""

# Python
import pdb

# Django REST Framework
from rest_framework.decorators import api_view

# Pyrty
from comments.serializers import CreateCommentSerializer


@api_view(['POST'])
def create_comment(request):
	pdb.set_trace()
	serializer = CreateCommentSerializer(request.data)
	pdb.set_trace()  # TODO
	serializer.save()
	return serializer.data
