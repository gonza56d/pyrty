# Generated by Django 3.0.7 on 2020-06-21 18:21

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified at')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='users/pictures/profiles', verbose_name='profile picture')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='user.username')),
                ('bio', models.TextField(blank=True, max_length=1000)),
                ('is_moderator', models.BooleanField(default=False)),
                ('posts', models.PositiveIntegerField(default=0, verbose_name='posts made')),
                ('comments', models.PositiveIntegerField(default=0, verbose_name='comments made')),
                ('reputation', models.PositiveIntegerField(default=0, help_text='Score obtained from comments and votes received.', verbose_name='user reputation')),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
    ]
