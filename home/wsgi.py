"""
WSGI config for the Aforro backend project.

This exposes the WSGI callable as a module-level variable named ``application``.
Used by production servers (gunicorn, uWSGI, etc.).
"""
import os
from django.core.wsgi import get_wsgi_application

# Set the default Django settings module for the 'wsgi' command
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'home.settings')

# This is the WSGI application used by Django's runserver and any production WSGI deployments
application = get_wsgi_application()
