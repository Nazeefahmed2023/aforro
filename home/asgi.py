"""
ASGI config for the Aforro backend project.

This exposes the ASGI callable as a module-level variable named ``application``.
Used for async servers (Daphne, Uvicorn, etc.).
"""
import os
from django.core.asgi import get_asgi_application

# Set the default Django settings module for the 'asgi' command
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'home.settings')

# This is the ASGI application used by Django's runserver and any production ASGI deployments
application = get_asgi_application()
