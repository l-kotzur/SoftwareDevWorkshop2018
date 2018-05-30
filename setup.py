import os, setuptools, re

setuptools.setup(
    name='printNumbers',
    version='0.1',
    author='Guido Trensch',
    url='https://github.com/gtrensch/SoftwareDevWorkshop2018',
    packages='printNumbers',
    include_package_data=True,
    # includes all files in sdist that are tracked in git, additional using the MANIFEST.in to exclude some of them
    install_requires='docopt',
)
