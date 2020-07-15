from setuptools import setup

setup(
  name='Cassandra FDW',
  version='1.1.0',
  license='Postgresql',
  packages=['cassandra_fdw'],
  install_requires=[
    'cassandra-driver==3.24.0',
    'pytz'
  ],
  dependency_links=['http://github.com/Kozea/Multicorn/tarball/master#egg=package-1.0']
)
