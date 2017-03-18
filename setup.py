from setuptools import setup, find_packages
import py_hangman

LONG_DESCRIPTION = """
This is a simple text-based 2-player version of Hangman.
More description will be added later.
"""

setup(
    name="py_hangman",
    version=py_hangman.__version__,
    description="A 2-player version of Hangman",
    long_description=LONG_DESCRIPTION,
    url="https://github.com/prasadkatti/py_hangman",
    author="Prasad Katti",
    author_email="prasadmkatti@gmail.com",
    packages=find_packages(),
    keywords='games hangman packaging',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Games/Entertainment',
    ],
    entry_points={
        'console_scripts': [
            'hangman=py_hangman.hangman:main',
        ],
    }
)
