try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    "description": "A command line interface for tracking time.",
    "author": "Kyle Long",
    "url": "none",
    "download_url": "none",
    "author_email": "uilwen@gmail.com",
    "version": "0.1",
    "install_requires": [
        "docopt"
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
