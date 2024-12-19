# setup.py

from setuptools import setup, find_packages
import os

# Read the contents of your README file
with open(os.path.join(os.path.dirname(__file__), 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='hello_ridwaanhall',
    version='0.3.0',
    packages=find_packages(),
    install_requires=[],  # Add your dependencies here
    author='Ridwan Halim',
    author_email='ridwaanhall.dev@gmail.com',
    description='A package that says hello to Ridwaan',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ridwaanhall/hello_ridwaanhall',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
