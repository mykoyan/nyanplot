from setuptools import setup, find_packages
import setuptools

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name='nyanplot',
    versions = '0.00',
    install_requires = requirements,
    packages = setuptools.find_packages()
    
)