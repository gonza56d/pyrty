# Generated by Django 3.0.7 on 2020-08-05 02:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('privatemessages', '0002_auto_20200725_0026'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='privatemessage',
            name='subject',
        ),
    ]
