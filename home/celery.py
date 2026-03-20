
"""
Celery app configuration for Aforro backend.

This sets up Celery to work with Django settings and autodiscover tasks.
"""
import os
from celery import Celery

# Set the default Django settings module for Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'home.settings')

# Create the Celery app instance
app = Celery('home')

# Load configuration from Django settings, using the 'CELERY_' prefix
app.config_from_object('django.conf:settings', namespace='CELERY')

# Autodiscover tasks in all installed apps
app.autodiscover_tasks()
