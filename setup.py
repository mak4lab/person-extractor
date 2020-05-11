from setuptools import setup
from os.path import abspath, dirname, join

root_dir = abspath(dirname(__file__))

with open(join(root_dir, "README.md")) as f:
    long_description = f.read()

setup(
    name = 'person-extractor',
    packages = ['person_extractor'],
    package_dir = {'person_extractor': 'person_extractor'},
    package_data = {'person_extractor': ['README.md', '__init__.py','test/__init__.py','test/data/en-uk_names.csv']},
    version = '4.0.0',
    description = 'Extract people from text',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author = 'Daniel J. Dufour, Victoria D. Mak',
    author_email = 'daniel@mak4lab.com, victoria@mak4lab.com',
    url = 'https://github.com/Mak4Lab/person-extractor',
    download_url = 'https://github.com/Mak4Lab/person-extractor/tarball/download',
    keywords = ['entity extraction', 'person'],
    classifiers = [
        'Development Status :: 3 - Alpha',
        "Programming Language :: Python :: 3",
        "License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication",
        "Operating System :: OS Independent",
    ]
)
