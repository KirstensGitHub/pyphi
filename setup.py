#!/usr/bin/env python3
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as f:
    readme = f.read()


requires = ['numpy >=1.8.1, <2.0.0',
            'scipy >=0.13.3, <1.0.0',
            'git+https://github.com/wmayner/pyemd#egg=pyemd']


setup(
    name="cyphi",
    version='0.0.2',
    description='Python library for computing integrated information.',
    author='Will Mayner',
    author_email='wmayner@gmail.com',
    long_description=readme,
    include_package_data=True,
    install_requires=requires,
    packages=['cyphi'],
    package_data={'': ['LICENSE']},
    license='GNU General Public License v3.0',
    zip_safe=False,
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Scientific/Engineering'
    ),
)
