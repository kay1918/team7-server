"""
ASGI config for velog project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

sys.path.append('/velog')

sys.path.append('/home/ubuntu/team7elog/lib/python3.8/site-packages')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'velog.settings')

application = get_asgi_application()
