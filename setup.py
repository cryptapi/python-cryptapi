#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(

    name='python-cryptapi',

    version='1.0.4',

    packages=find_packages(),

    author="CryptAPI",

    author_email="info@cryptapi.io",
    install_requires=[
        'requests'
    ],
    description="Python Library for CryptAPI payment gateway",
    long_description_content_type="text/markdown",
    long_description=long_description,

    include_package_data=True,

    url='https://github.com/cryptapi/python-cryptapi',
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 5 - Production/Stable",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
    ],

    license="MIT",

    zip_safe=False,
)
