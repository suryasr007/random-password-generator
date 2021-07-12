from setuptools import setup, find_packages
from codecs import open
from os import path


VERSION = 'v2.2.0'

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='random-password-generator',
    version=VERSION,
    description='Simple and custom random password generator for python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/suryasr007/random-password-generator',
    author='Surya Teja Reddy Valluri',
    author_email='94suryateja@gmail.com',
    license='MIT',
    py_modules=['password_generator'],
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable

        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Utilities',
        'Operating System :: POSIX'
    ],
    keywords='random password generator different lengths'
)
