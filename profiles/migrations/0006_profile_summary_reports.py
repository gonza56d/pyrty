# Generated by Django 3.1 on 2020-09-21 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_auto_20200912_1827'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='summary_reports',
            field=models.CharField(choices=[('', 'Never'), ('D', 'Daily'), ('W', 'Weekly'), ('M', 'Monthly')], default='', help_text='Set how often the summary report is obtained', max_length=1, verbose_name='Summary report interval'),
        ),
    ]
