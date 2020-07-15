import subprocess
from setuptools import setup, find_packages, Extension

setup(
  name='Cassandra FDW',
  version='1.1.0',
  license='Postgresql',
  packages=['cassandra_fdw'],
  install_requires=[
    'cassandra-driver==3.23.0',
    'http://github.com/Kozea/Multicorn/tarball/master#egg=package-1.0'
  ],
)