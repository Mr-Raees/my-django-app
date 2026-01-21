"""
WSGI config for cm2021 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

#import os

#from django.core.wsgi import get_wsgi_application

#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cm2021.settings')

#application = get_wsgi_application()

import os
import sys

path = '/home/itsfirsttimeimhere/cm2021'
if path not in sys.path:
    sys.path.insert(0, path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'cm2021.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

