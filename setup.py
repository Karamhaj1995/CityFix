#!/usr/bin/python3

from os.path import isfile, exists, dirname
from os import makedirs
from shutil import copyfile
from distutils.core import setup
from distutils.dir_util import copy_tree


# EK_CONF_FILE = "/etc/cityfix/conf/cityfix.conf"


# Move Default Configuration for System Starter
# if not isfile(EK_CONF_FILE):
#     try:
#         if not exists(dirname(EK_CONF_FILE)):
#             makedirs(dirname(EK_CONF_FILE))
#         copyfile("misc/Ekron-nms.conf-default", EK_CONF_FILE)
#         copyfile("misc/db.conf", EK_DB_CONF_FILE)
#         copyfile("misc/logging.conf", EK_LOG_CONF_FILE)

#     except Exception as detail:
#         print(detail)
#         raise SystemExit

setup(name='CityFix',
      version='0.1',
      description='CityFix Manager all city hazards and reports.',
      author='Karam Haj',
      author_email='karamhaj1995@gmail.com',
      packages=['server',
                'server.const',
                'server.models',
                        'client',
                'client.handlers'],
      package_dir={'cityfix': 'cityfix'},
      requires=['passlib',
                  'pymongo',
                  'validate',
                  'bson',
                  'jwt',
                  'tornado',
                  'log4mongo',
                  'mongoengine',
                  'blinker',
                  'falcon',
                  'gunicorn'])
