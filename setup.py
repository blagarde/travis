#!/usr/bin/env python

from setuptools import setup

VERSION = '0'

setup(
    name = 'travistest',
    version = VERSION,
    install_requires = ['unicodecsv==0.10.1'],
    dependency_links = ['https://github.com/jdunck/python-unicodecsv/zipball/master#egg=unicodecsv-0.10.1'],
)
