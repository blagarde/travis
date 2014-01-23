#!/usr/bin/env python

from setuptools import setup

VERSION = '0'

setup(
    name = 'travistest',
    version = VERSION,
    install_requires = ['unicodecsv'],
    dependency_links = ['git+https://github.com/jdunck/python-unicodecsv/master/tarball'],
)
