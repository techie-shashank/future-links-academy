"""
WSGI config for centre project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from centre.utils import get_default_django_settings_module

os.environ.setdefault("DJANGO_SETTINGS_MODULE", get_default_django_settings_module())

from django.core.wsgi import get_wsgi_application
from dj_static import Cling

application = Cling(get_wsgi_application())
