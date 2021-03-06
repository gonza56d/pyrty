# Generated by Django 3.1 on 2020-11-01 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified at')),
                ('content', models.TextField(max_length=1000)),
            ],
            options={
                'ordering': ['created', 'modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
    ]
