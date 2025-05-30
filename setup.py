#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re

from setuptools import setup, find_packages

# Python versions this package is compatible with
python_requires = '>=3.6, <4'

# Packages that this package imports. List everything apart from standard lib packages.
install_requires = [
    'sensirion-i2c-driver',
    'sensirion-i2c-adapter',
    'sensirion_driver_support_types~=0.2.0',
    'sensirion-shdlc-sensorbridge>=0.1.1,<0.3.0'
]

# Packages required for tests and docs
extras_require = {
    'test': [
        'flake8~=3.7.8',
        'pytest~=6.2.5',
        'pytest-cov~=3.0.0',
    ],
    'docs': [
        'click==8.0.4',
        'jinja2==3.0.1',
        'sphinx~=2.2.1',
        'sphinx-rtd-theme~=0.4.3',
    ]
}

# Read version number from version.py
version_line = open("sensirion_i2c_scd30/version.py", "rt").read()
result = re.search(r"^version = ['\"]([^'\"]*)['\"]", version_line, re.M)
if result:
    version_string = result.group(1)
else:
    raise RuntimeError("Unable to find version string")

# Use README.rst and CHANGELOG.rst as package description
root_path = os.path.dirname(__file__)
readme = open(os.path.join(root_path, 'README.rst')).read()
changelog = open(os.path.join(root_path, 'CHANGELOG.rst')).read()
long_description = readme.strip() + "\n\n" + changelog.strip() + "\n"

setup(
    name='sensirion_i2c_scd30',
    version=version_string,
    author='Sensirion',
    author_email='info@sensirion.com',
    description='I2C driver for the Sensirion SCD30 sensor family',
    license='BSD',
    keywords="""Sensirion SCD30
        I2C
        SCD30""",
    url='https://sensirion.github.io/python-i2c-scd30/',
    packages=find_packages(exclude=['tests', 'tests.*']),
    long_description=long_description,
    python_requires=python_requires,
    install_requires=install_requires,
    extras_require=extras_require,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: Other/Proprietary License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
