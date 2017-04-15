.. image:: https://travis-ci.org/prasadkatti/py_hangman.svg?branch=master
    :target: https://travis-ci.org/prasadkatti/py_hangman
.. image:: https://badge.fury.io/py/py-hangman.svg
    :target: https://badge.fury.io/py/py-hangman

2 Player Hangman
================

Overview
--------

Welcome to this 2 Player Hangman game.

Note: This project was primarily created for the following purposes -

- Getting hands-on experience with GitHub
- Learning simple game development in Python
- Understanding packaging and distribution in Python
- Getting some experience with tools like tox and Travis CI

Installing Hangman
------------------

The project is available on PyPI - https://pypi.python.org/pypi/py-hangman

As such, you can install using ``pip install py-hangman``.

Or you can also install from source by cloning the repo and
running ``pip install .`` from the directory containing setup.py.

Running Hangman
---------------

A binary called *hangman* is created during installation.

If you install the project inside a virtualenv, the hangman binary will
be present in the bin directory of the virtualenv.

Run the hangman binary to start the game. Follow the instructions on screen to continue.

Testing
-------

Tests are written using unittest. Run them with -
``python tests.py -b``

Demo
----

|asciicast|

.. |asciicast| image:: https://asciinema.org/a/azy7c3q7zb0oipwdusx5jzodb.png
   :target: https://asciinema.org/a/azy7c3q7zb0oipwdusx5jzodb
