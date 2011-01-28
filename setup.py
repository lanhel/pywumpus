#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#-------------------------------------------------------------------------------
"""Hunt the Wumpus"""
__author__ = ('Lance Finn Helsten',)
__version__ = '1.2'
__copyright__ = """Copyright (C) 2009 Lance Finn Helsten"""
__license__ = """
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import sys
if sys.version_info < (3, 0):
    raise Exception("pyzombie requires Python 3.0 or higher.")
from distutils.core import setup

setup(
    name='pywumpus',
    version=__version__,
    author='Lance Finn Helsten',
    author_email='lanhel@me.com',
	#maintainer='',
    #maintainer_email='',
    url='http://code.google.com/p/pywumpus/',
    description='Hunt the Wumpus (1972) Python translation.',
    long_description=open('README.txt').read(),
    platforms=['OS Independent'],
    download_url='http://code.google.com/p/pywumpus/downloads/list',
    license="GNU General Public License",    
    classifiers=[
		'Development Status :: 5 - Production/Stable',
		'Environment :: Console',
		'Intended Audience :: Developers',
		'Intended Audience :: Education',
		'Intended Audience :: End Users/Desktop',
		'License :: OSI Approved :: GNU General Public License (GPL)',
		'Operating System :: OS Independent',
		'Programming Language :: Python :: 3',
		'Topic :: Education',
		'Topic :: Games/Entertainment'
    ],
    scripts=['pywumpus.py'],
)


