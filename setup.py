# encoding: utf-8
from setuptools import setup, find_packages


setup(
    name='simpy-agents',
    version='0.1',
    author='Jake Nunemaker',
    author_email='jake.d.nunemaker@gmail.com',
    credits='Ontje Lünsdorf, Stefan Scherfke',
    description='An extension of SimPy for working with distinct agents.',
    install_requires=[],
    packages=["simpy", "simpy.resources"],
    include_package_data=True,
)
