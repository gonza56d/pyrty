# Generated by Django 3.1 on 2020-09-12 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20200906_0519'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='posts',
        ),
        migrations.AlterField(
            model_name='profile',
            name='reputation',
            field=models.PositiveIntegerField(default=0, help_text='Score obtained from posts and comments made, and votes received.', verbose_name='user reputation'),
        ),
    ]
