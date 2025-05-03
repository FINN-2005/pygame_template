# setup.py
from setuptools import setup, find_packages

setup(
    name='pygame_template',       # Name of the package
    version='1',                  # Version of the package
    packages=find_packages(),     # Automatically find the 'mine' package
    install_requires=[            # List any dependencies here
        'pygame-ce',
        'numpy'
    ],
)
