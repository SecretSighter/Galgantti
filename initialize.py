#!/usr/bin/env python3
import os

# initialize the django environment
# assumes ./proj/settings.py is your settings file, relative to current dir
os.environ['DJANGO_SETTINGS_MODULE'] = 'test_dmp.settings'
import django
django.setup()

# import models and run django/python commands
from homepage import models as hmod
professor = hmod.Professor.objects.get(id=123)
print(professor.name)