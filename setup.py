#!/usr/bin/env python

from distutils.core import setup

setup(
        name='py-viitenumero',
        version='1.0',
        description='Python module for generating Finnish national payment reference number',
        author='Mohanjith Sudirikku Hannadige',
        author_email='moha@codemaster.fi',
        url='http://www.codemaster.fi/python/maksu/',
        download_url = 'https://github.com/codemasteroy/py-viitenumero/tarball/1.0',
        packages=[ 'maksu' ],
        keywords=[ 'payments', 'creditor reference', 'finland', 'suomi' ],
)
