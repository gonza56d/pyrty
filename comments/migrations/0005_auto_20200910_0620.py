# Generated by Django 3.1 on 2020-09-10 06:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0004_auto_20200910_0451'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'get_latest_by': 'created', 'ordering': ['created', 'modified']},
        ),
    ]