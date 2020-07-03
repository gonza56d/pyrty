"""Celery app config."""

# Python
import os

# Django
from django.apps import apps, AppConfig
from django.conf import settings

# Celery
from celery import Celery


if not settings.configured:
	# Set default Django settings for Celery
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')


app = Celery('pyrty')


app.config_from_object('django.conf:settings', namespace='CELERY')


class CeleryAppConfig(AppConfig):
	name = 'pyrty.taskapp'
	verbose_name = 'Celery Config'

	def ready(self):
		installed_apps = [app_config.name for app_config in apps.get_app_configs()]
		app.autodiscover_tasks(lambda: installed_apps, force=True)
