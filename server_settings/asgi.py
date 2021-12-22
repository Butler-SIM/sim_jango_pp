"""
ASGI config for server_settings project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server_settings.settings.deploy")
django.setup()
