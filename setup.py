try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    "description": "A command line interface for tracking time.",
    "author": "Kyle Long and Andy Gertjejansen",
    "url": "none",
    "download_url": "none",
    "author_email": "uilwen@gmail.com",
    "version": "0.2",
    "install_requires": [
        "docopt",
        "python-dateutil"
    ],
    "tests_require": [],
    "packages": ["hackytrack"],
    "scripts": [
        "bin/hackytrack",
        "bin/hackyanalyze"
    ],
    "name": "hackytrack"
}

setup(**config)
