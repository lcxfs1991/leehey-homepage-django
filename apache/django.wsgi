import os
import sys
import django.core.handlers.wsgi

os.environ['DJANGO_SETTINGS_MODULE']= 'homepage.settings'
app_path ="/Users/lcxfs1991/web/homepage/"

sys.path.append(app_path)
application = django.core.handlers.wsgi.WSGIHandler()
