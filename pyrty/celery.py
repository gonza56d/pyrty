from __future__ import absolute_import, unicode_literals

import os

from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pyrty.settings')

app = Celery('pyrty')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
	sender.add_periodic_task(
		crontab(hour=21, minute=45, day_of_week=1),
		debuggin()
	)


@app.task(bind=True, default_retry_delay=30)
def debuggin(self):
	print('debug ran')
