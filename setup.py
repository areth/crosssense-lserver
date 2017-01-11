# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='lserver',
    version='0.1.0',
    description='Crosssense learning server',
    long_description=readme,
    author='Areth',
    author_email='al.reshetnikov@gmail.com',
    url='https://github.com/areth/crosssense-lserver',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    entry_points={
        'console_scripts': [
            'lserver = lserver.__main__:main'
        ]
    }
)