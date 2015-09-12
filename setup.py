from setuptools import setup

setup(name='userd',
      version='0.1',
      description='Web based userinterface to userdatabases',
      url='http://github.com/banduri/userd',
      author='Alexander Kasper',
      author_email='asklepios@riseup.net',
      license='GPLv2',
      packages=['userd'],
      install_requires=[
          'sqlalchemy',
          'jinja2'
      ],
      zip_safe=False)

