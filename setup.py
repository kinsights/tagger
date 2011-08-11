#!/usr/bin/env python
# -*- coding; utf-8 -*-

from distutils.core import setup

setup(
    name='tagger',
    version='0.5.20110811',
    description='A module for extracting relevant tags from text documents.',
    long_description=open('README.rst', 'r').read(),
    author='Alessandro Presta',
    author_email = 'https://github.com/apresta',
    maintainer='Torkn',
    maintainer_email = 'https://github.com/Torkn',
    url='https://github.com/Torkn/tagger',
    license='Python Software Foundation License',
    packages=['tagger',],
    package_dir={'tagger': '.'},
    package_data={'tagger': ['data/*.pkl', 'doc/*', 'data/*', 'tests/*', 'README.rst']},
    requires=['stemming (>=1.0)', 'nltk (>=2.0)'],
    provides=['tagger'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Text Processing",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: Python Software Foundation License",
    ],
    )
