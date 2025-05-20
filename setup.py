# setup.py
from setuptools import setup, find_packages

setup(
    name='pygame_template',
    version='1',
    packages=find_packages(),
    install_requires=[
        'pygame-ce',
        'numpy'
    ],
)
