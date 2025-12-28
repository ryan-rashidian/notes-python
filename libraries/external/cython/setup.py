"""Setup for Cython module."""

from setuptools import setup
from Cython.Build import cythonize

setup (
    name='Hello Module',
    ext_modules=cythonize('hello.pyx'),
)

