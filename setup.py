
from setuptools import setup, find_packages

setup(
    name='pybugg',
    version='0.1.0',
    packages=find_packages(include=["pybugg"]),
    entry_points = {
        'console_scripts': ['pybugg=pybugg.inject_pudb:main'],
    }

)
