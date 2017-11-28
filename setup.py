"""
This file creates a package from the project source folder (portfolio_danny_jager)
"""

from setuptools import setup

setup(
    name='portfolio_danny_jager',
    packages=['portfolio_danny_jager'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)
