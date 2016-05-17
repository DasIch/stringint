import os

from setuptools import setup


def read_readme():
    readme_path = os.path.join(os.path.dirname(__file__), 'README.rst')
    with open(readme_path, 'r', encoding='utf-8') as readme_file:
        return readme_file.read()


setup(
    name='stringint',
    version='0.1',
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
