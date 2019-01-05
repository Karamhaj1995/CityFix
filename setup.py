#!/usr/bin/python3

from os.path import isfile, exists, dirname
from os import makedirs
from shutil import copyfile
from distutils.core import setup
from distutils.dir_util import copy_tree

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
