# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='sample',
    version='0.0.1',
    description='Personal Sample package based on Python-Guide.org',
    long_description=readme,
    author='Chris Baker',
    author_email='gaoler@electronicpanopticon.com',
    url='https://github.com/folkengine/samplemod',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

