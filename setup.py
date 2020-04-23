#!/usr/bin/env python3

from setuptools import setup

setup(name='dev_aberto_franciscocra',
    version='0.3',
    author='francisco aveiro',
    license='MIT',
    homepage="",
    packages=['dev_aberto']
    )

install_requires=[
'requests'
],


scripts=['scripts/hello.py'],