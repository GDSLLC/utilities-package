import sys
if sys.version_info.major < 3:
    sys.exit('Python 3 required but lower version found. Aborted.')

from __future__ import absolute_import, division, print_function, unicode_literals

from setuptools import setup

setup(
    name='utilities-package',
    version='0.0.3',
    description='utilities package',
    url='https://github.com/terminal-labs/utilities',
    author='Terminal Labs',
    author_email='solutions@terminallabs.com',
    license="license",
    packages=['utilities'],
    zip_safe=False,
    install_requires=[
        'six',
        'bash',
        'termcolor',
    ],
    )
