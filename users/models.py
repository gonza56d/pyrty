"""Users model definition."""

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

# Utilities
from utils.models import PyrtyModel


SUMMARY_REPORTS_CHOICES = [
    ('', 'Never'),
    ('D', 'Daily'),
    ('W', 'Weekly'),
    ('M', 'Monthly'),
]


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

    username_regex = RegexValidator(regex='[aA0-zZ9]', message='Only letters and numbers allowed.')

    username = models.CharField(
        'username',
        max_length=20,
        unique=True,
        help_text='Required. 20 characters or fewer. Letters and numbers only.',
        validators=[username_regex],
        error_messages={
            'unique': "A user with that username already exists.",
        },
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    is_verified = models.BooleanField(
        'verified',
        default=False,
        help_text='Set to true if user has verified its email.'
    )

    # Summary Reports
    summary_reports = models.CharField(
        'Summary report interval',
        max_length=1,
        default='',
        choices=SUMMARY_REPORTS_CHOICES,
        help_text='Set how often the summary report is obtained'
    )

    def __str__(self):
        """Return username."""
        return self.username
