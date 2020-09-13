# Generated by Django 3.1 on 2020-09-07 01:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0002_post_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='negative_votes',
            field=models.ManyToManyField(related_name='negative_vote_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='positive_votes',
            field=models.ManyToManyField(related_name='positive_vote_set', to=settings.AUTH_USER_MODEL),
        ),
    ]