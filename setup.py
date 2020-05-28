import os

from setuptools import find_packages, setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='pydarwin',
    version='0.0.4',
    description='A simple genetic algorithm for use in Python.',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    keywords='genetic algorithm',
    url='https://github.com/privat-matthieu/pydarwin',
    author='Matthieu Privat',
    author_email='privatm@my.erau.edu',
    license='MIT',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'
    ],
    packages=find_packages(exclude=['*.tests']))