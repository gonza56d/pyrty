# Generated by Django 3.1 on 2020-11-07 01:03

from django.db import migrations
import django_quill.fields


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20201101_0043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=django_quill.fields.QuillField(max_length=5000, verbose_name='post content'),
        ),
    ]
