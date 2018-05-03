#!/usr/bin/env python3

from setuptools import setup

# Work around mbcs bug in distutils.
# http://bugs.python.org/issue10945
import codecs
try:
    codecs.lookup('mbcs')
except LookupError:
    ascii = codecs.lookup('ascii')
    codecs.register(lambda name, enc=ascii: {True: enc}.get(name == 'mbcs'))

VERSION = '1.0.2'

setup(
    name='onegramcoin',
    version=VERSION,
    description='Python library for onegram',
    long_description=open('README.md').read(),
	download_url='https://gitlab.com/onegram-developers/python-onegram/-/archive/v' + VERSION + '/python-onegram-v' + VERSION + '.zip',
    author='Frantisek Horvath',
    author_email='frantisek.horvath@01cryptohouse.com',
    maintainer='Frantisek Horvath',
    maintainer_email='frantisek.horvath@01cryptohouse.com',
    url='https://gitlab.com/onegram-developers/python-onegram',
    keywords=['onegram', 'library', 'api', 'rpc'],
    packages=[
        "onegram",
        "onegramapi",
        "onegrambase"
    ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Financial and Insurance Industry',
        'Topic :: Office/Business :: Financial',
    ],
    install_requires=[
        "onegramlib>=1.0.4",
        "websockets",
        "appdirs",
        "Events",
        "scrypt",
        "pycryptodome",  # for AES, installed through graphenelib already
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    include_package_data=True,
    zip_safe=True,
)
