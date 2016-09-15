import sae
sae.add_vendor_dir('vendor')
from healthdaily import wsgi
#import os



import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'healthdaily.settings'
import django.core.handlers.wsgi
#import sae
try:
    application = sae.create_wsgi_app(django.core.handlers.wsgi.WSGIHandler())
except:
    application = sae.create_wsgi_app(wsgi.application)
