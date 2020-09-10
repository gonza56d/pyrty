# Generated by Django 3.1 on 2020-09-10 04:51

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0003_auto_20200907_0109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='negative_votes',
            field=models.ManyToManyField(related_name='p_negative_vote_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='positive_votes',
            field=models.ManyToManyField(related_name='p_positive_vote_set', to=settings.AUTH_USER_MODEL),
        ),
    ]
