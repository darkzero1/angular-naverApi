"""
WSGI config for naverapi project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
import sys

sys.path.append('/home/navertest/naverapi')

os.environ.setdefault("PYTHON_EGG_CACHE", "/home/navertest/naverapi/naverapi/egg_cache")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "naverapi.settings")
from django.core.wsgi import get_wsgi_application
def application(environ, start_response):
    if environ['mod_wsgi.process_group'] != '':
        import signal
        os.kill(os.getpid(), signal.SIGINT)
    return ["killed"]
application = get_wsgi_application()

