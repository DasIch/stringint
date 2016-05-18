import os
import re

from setuptools import setup


PROJECT_PATH = os.path.dirname(__file__)


def get_version():
    module_path = os.path.join(PROJECT_PATH, 'stringint.py')
    version_re = re.compile(r"^__version__ = '([\d.]+)'$")
    with open(module_path, 'r', encoding='utf-8') as module_file:
        for line in module_file:
            match = version_re.match(line)
            if match is not None:
                return match.group(1)


def read_readme():
    readme_path = os.path.join(PROJECT_PATH, 'README.rst')
    with open(readme_path, 'r', encoding='utf-8') as readme_file:
        return readme_file.read()


setup(
    name='stringint',
    version=get_version(),
    url='https://github.com/DasIch/stringint/',
    author='Daniel Neuhäuser',
    author_email='ich@danielneuhaeuser.de',
    description='represent strings as ints and vice versa',
    long_description=read_readme(),
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Implementation :: CPython'
    ],

    py_modules=['stringint']
)
