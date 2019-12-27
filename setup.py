# encoding: utf-8
from setuptools import setup, find_packages


setup(
    name='simpy-agents',
    version='0.1',
    author='Jake Nunemaker',
    author_email='jake.d.nunemaker@gmail.com',
    description='An extension of SimPy for working with distinct agents.',
    install_requires=[],
    packages=find_packages(where='simpy'),
    package_dir={'': 'simpy'},
    include_package_data=True,
)
