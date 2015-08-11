#!/usr/bin/env python
# encoding: utf-8

from setuptools import setup

setup(name='haproxystat',
      version='0.1.0',
      description='CLI tool for HAProxy statistics',
      url='http://github.com/alexanderteves/haproxystat',
      author='Alexander Teves',
      author_email='alexander.teves@gmail.com',
      license='MIT',
      packages=['haproxystat'],
      install_requires=['requests', 'argparse'],
      scripts=['bin/haproxystat'])
