#!/usr/bin/python

# python setup.py sdist --format=zip,gztar

from setuptools import setup
import os
import sys
import platform
import imp


version = imp.load_source('version', 'lib/version.py')

if sys.version_info[:3] < (2, 7, 0):
    sys.exit("Error: Electrum requires Python version >= 2.7.0...")



data_files = []
if platform.system() in [ 'Linux', 'FreeBSD', 'DragonFly']:
    usr_share = os.path.join(sys.prefix, "share")
    data_files += [
        (os.path.join(usr_share, 'applications/'), ['electrum-pkb.desktop']),
        (os.path.join(usr_share, 'pixmaps/'), ['icons/electrum-pkb.png'])
    ]


setup(
    name="Electrum-PKB",
    version=version.ELECTRUM_VERSION,
    install_requires=[
        'slowaes>=0.1a1',
        'ecdsa>=0.9',
        'pbkdf2',
        'requests',
        'qrcode',
        'ltc_scrypt',
        'protobuf',
        'tlslite',
        'dnspython',
    ],
    package_dir={
        'electrum_pkb': 'lib',
        'electrum_pkb_gui': 'gui',
        'electrum_pkb_plugins': 'plugins',
    },
    packages=['electrum_pkb','electrum_pkb_gui','electrum_pkb_gui.qt','electrum_pkb_plugins'],
    package_data={
        'electrum_pkb': [
            'wordlist/*.txt',
            'locale/*/LC_MESSAGES/electrum.mo',
        ],
        'electrum_pkb_gui': [
            "qt/themes/cleanlook/name.cfg",
            "qt/themes/cleanlook/style.css",
            "qt/themes/sahara/name.cfg",
            "qt/themes/sahara/style.css",
            "qt/themes/dark/name.cfg",
            "qt/themes/dark/style.css",
        ]
    },
    scripts=['electrum-pkb'],
    data_files=data_files,
    description="Lightweight ParkByte Wallet",
    author="pkbDEV",
    author_email="pkbcoin@twitter",
    license="GNU GPLv3",
    url="http://electrum-pkb.net",
    long_description="""Lightweight ParkByte Wallet"""
)
