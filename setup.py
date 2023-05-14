#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('VERSION.txt', 'r') as v:
    version = v.read().strip()

with open('README.rst', 'r') as r:
    readme = r.read()

download_url = (
    'https://github.com/juliomalegria/django-chunked-upload/tarball/%s'
)

setup(
    name='django4-chunked-upload',
    packages=['chunked_upload', 'chunked_upload.migrations', 'chunked_upload.management'],
    version=version,
    description=('Upload large files to Django in multiple chunks, with the '
                 'ability to resume if the upload is interrupted. Updated to support newer versions on Django. Based on the project of Julio M Alegria.'),
    long_description=readme,
    author='Julio M Alegria & Jesus A Bravo',
    author_email='isc.alfredobravo@gmail.com',
    url='https://github.com/fredito1212/django-chunked-upload',
    download_url=download_url % version,
    install_requires=[],
    license='MIT-Zero'
)
