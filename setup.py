#!/usr/bin/env python

#
# :copyright: (c) 2012 by Mike Taylor
# :license: BSD 2-Clause
#

from distutils.core import setup

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(name='kyaku',
      version='0.1.0',
      author='Mike Taylor',
      author_email='bear@code-bear.com',
      packages=['kyaku', ],
      url='http://pypi.python.org/pypi/bearlib/',
      license=license,
      description='A set of tools to monitor social media and bridge them with mailing lists.',
      long_description=readme,
      classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development :: Libraries :: Python Modules',
      ],
     )
