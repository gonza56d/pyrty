"""Comment rest api views."""

# Python
# import pdb

# Django
from django.contrib import auth

# Django REST Framework
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Pyrty
from users.forms import LoginForm


@api_view(['POST'])
def oauth(request):
    form = LoginForm(data=request.data)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        return Response({'message': 'Invalid username and/or password.'}, status=status.HTTP_401_UNAUTHORIZED)
    return Response({'message': 'Username/email and password must be provided.'}, status=status.HTTP_400_BAD_REQUEST)
