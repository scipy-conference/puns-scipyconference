#!/usr/bin/env python

from distutils.core import setup

setup(name='scipyconference',
      version='0.1dev',
      description='SciPy Conference',
      author='SciPy Conference Organizers',
      include_package_data=True,
      package_data={'scipyconference': ['puns.json']},
      )
