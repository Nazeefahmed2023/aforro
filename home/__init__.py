# This ensures the Celery app is always imported when Django starts.
# See: https://docs.celeryq.dev/en/stable/django/first-steps-with-django.html
from .celery import app as celery_app

