#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    "youtube-dl>=2016.4.19",
    "PyChromecast>=0.7.0",
    "Click>=5.0",
]

test_requirements = [
]

setup(
    name='catt',
    version='0.0.1',
    description="Cast All The Things allows you to send videos from many, many online sources to your Chromecast.",
    long_description=readme + '\n\n' + history,
    author="Stavros Korokithakis",
    author_email='hi@stavros.io',
    url='https://github.com/skorokithakis/catt',
    packages=[
        'catt',
    ],
    package_dir={'catt':
                 'catt'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords="chromecast cast catt cast_all_the_things",
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    entry_points={
        'console_scripts': ['catt=catt.cli:cli'],
    },
)