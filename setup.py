#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import sys
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

PROJECT_DESCRIPTION = 'Command line utility to assisst in collection metrics from large Galaxies for community analysis'
PACKAGES = [
    'grt-client',
]
ENTRY_POINTS = '''
    [console_scripts]
    grt-export=grt:export
    grt-upload=grt:upload
'''

setup(
    name='grt-client',
    version='21.01.0',
    description=PROJECT_DESCRIPTION,
    # long_description=readme + '\n\n' + history,
    # long_description_content_type="text/x-rst",
    author="Helena Rasche",
    author_email="helena.rasche@gmail.com",
    packages=PACKAGES,
    entry_points=ENTRY_POINTS,
    include_package_data=True,
    # install_requires=requirements,
    license="AFL",
    classifiers=[
        # 'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Environment :: Console',
        'License :: OSI Approved :: Academic Free License (AFL)',
        'Operating System :: POSIX',
        'Natural Language :: English',
        "Programming Language :: Python :: 3",
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
