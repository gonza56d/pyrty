# Generated by Django 3.1 on 2020-11-07 01:49

from django.db import migrations
import django_quill.fields


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20201107_0113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=django_quill.fields.QuillField(max_length=5000, verbose_name='post content'),
        ),
    ]