#!/usr/bin/env python

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

dist_setup = generate_distutils_setup()

setup(**dist_setup)
