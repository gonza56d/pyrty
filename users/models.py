"""Users model definition."""

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser

# Utilities
from utils.models import PyrtyModel


class User(PyrtyModel, AbstractUser):
    """User model.

    Extend from Django's AbstractUser. Change the username field to email field
    and add some extra fields.
    """

    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique': 'That email is already taken.'
        }
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    first_name = models.CharField(
        max_length=50,
        null=True
    )

    last_name = models.CharField(
        max_length=50,
        null=True
    )

    is_verified = models.BooleanField(
        'verified',
        default=False,
        help_text='Set to true if user has verified its email.'
    )

    def __str__(self):
        """Return username."""
        return self.username
