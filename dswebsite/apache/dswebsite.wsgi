import os, sys
path = '/Users/kayhandursun/dsweb/dswebsite/'
if path not in sys.path:
    sys.path.append(path)

path = '/Users/kayhandursun/dsweb/dswebsite/dscience/'
if path not in sys.path:
    sys.path.append(path)

#Calculate the path based on the location of the WSGI script.
apache_configuration = os.path.dirname(__file__)
project = os.path.dirname(apache_configuration)
workspace = os.path.dirname(project)
sys.path.append(workspace)

os.environ['DJANGO_SETTINGS_MODULE'] = 'dswebsite.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

