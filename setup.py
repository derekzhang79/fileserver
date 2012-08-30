import codecs
from os import path
from setuptools import setup, find_packages

read = lambda filepath: codecs.open(filepath, 'r', 'utf-8').read()

setup(
    name='fileserver',
    description='Small file server.',
    long_description=read(path.join(path.dirname(__file__), 'README.rst')),
    version='0.1a1',
    url='',
    author='ostcar',
    author_email='',
    license='zlib',
    packages=find_packages(exclude=['example']),
    include_package_data = True,
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'License :: OSI Approved :: zlib/libpng License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ],
)

