#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = [ 'tifffile==2020.10.1' ]

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="Ilan Gold",
    author_email='ilan_gold@hms.harvard.edu',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="A cli tool for generating IFD offsets within a tiff file, useful for optimizing load times of remote tiff files in viewers like viv.",
    entry_points={
        'console_scripts': [
            'generate_tiff_offsets=generate_tiff_offsets.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme,
    long_description_content_type='text/markdown',
    include_package_data=True,
    keywords='generate_tiff_offsets',
    name='generate_tiff_offsets',
    packages=find_packages(include=['generate_tiff_offsets', 'generate_tiff_offsets.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/ilan-gold/generate-tiff-offsets',
    version='0.1.7',
    zip_safe=False,
)
