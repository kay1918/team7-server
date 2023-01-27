"""
WSGI config for velog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os, sys

from django.core.wsgi import get_wsgi_application

sys.path.append('/')

# sys.path.append('/velog')

sys.path.append('/home/ubuntu/team7elog/lib/python3.8/site-packages')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'velog.settings')

application = get_wsgi_application()
