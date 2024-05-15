# django_celery/celery.py

import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Multikart.settings")
app = Celery("Multikart")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


# python -m celery -A Multikart worker -l info
# celery -A Multikart worker --beat --scheduler django --loglevel=info

# celery -A Multikart beat --scheduler django --loglevel=info
# celery -A Multikart worker --loglevel=info


