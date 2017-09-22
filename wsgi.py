"""
WSGI config for locallibrary project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

#Is used to help django application comminucate with the web server. You can treat this as boilerplate 

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "locallibrary.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
