# HashCash Mining Challenge
# setup_cython.py
# Created by Mauro J. Pappaterra on 12 of April 2019.
from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules = cythonize('optimize_cython.pyx'))