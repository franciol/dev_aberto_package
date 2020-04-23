#!/usr/bin/env python3

from setuptools import setup

setup(name='dev_aberto_francisco_aveiro',
    version='0.1',
    author='francisco aveiro',
    license='MIT',
    packages=['dev_aberto']
    )

install_requires=[
'requests'
],

scripts=['scripts/hello.py'],