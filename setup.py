#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import path
from codecs import open

from setuptools import setup

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pyjisho',
    packages=['jisho'],
    version='0.1.0',
    license='MIT',
    description='Python HTTP client for the Jisho.org search API.',
    author='Matt Palen',
    url='https://github.com/matthewmpalen/pyjisho',
    download_url = 'https://github.com/matthewmpalen/pyjisho/archive/0.1.0.tar.gz',
    project_urls={
        'Bug Reports': 'https://github.com/matthewmpalen/pyjisho/issues'
    },
    install_requires=[
        'requests'
    ],
    keywords=[
        'Japanese',
        'English',
        'translation',
        'dictionary',
        'language',
        'jisho',
        '辞書',
        'じしょ'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    long_description=long_description,
    long_description_content_type='text/markdown',
)