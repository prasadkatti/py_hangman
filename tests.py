#!/usr/bin/env python

from __future__ import print_function

import unittest
from contextlib import contextmanager

from py_hangman.hangman import Hangman
import py_hangman


# this code is based on:
# http://stackoverflow.com/questions/21046717/python-mocking-raw-input-in-unittests
@contextmanager
def mock_input(mock):
    orig_input = py_hangman.hangman.input
    py_hangman.hangman.input = lambda _: mock
    yield
    py_hangman.hangman.input = orig_input


class TestHangman(unittest.TestCase):

    def test_update_chances(self):
        h = Hangman()
        h.answer = "foobar"

        h.chances = 1
        guess = 'f'
        h._update_chances(guess)
        self.assertEqual(h.chances, 1, "test - update chances left - 1")

        h.chances = 1
        guess = "x"
        h._update_chances(guess)
        self.assertEqual(h.chances, 0, "test - update chances left - 2")

    def test_accept_guess(self):

        h = Hangman()
        h._make_partial_answer = lambda: ''

        with mock_input('foo'):
            self.assertIsNone(h._accept_guess(), "test - accept guess - 1")

        with mock_input('123'):
            self.assertIsNone(h._accept_guess(), "test - accept guess - 2")

        h.guesses = {'a', 'b', 'c'}
        with mock_input('a'):
            self.assertIsNone(h._accept_guess(), "test - accept guess - 3")

    def test_make_partial_answer(self):
        h = Hangman()
        self.assertRaises(Exception, h._make_partial_answer)

        h.answer = "foobar"
        h.guesses = set("abc")
        self.assertEqual(h._make_partial_answer(), "***ba*",
                         "test- make partial answer - 2")


if __name__ == '__main__':
    unittest.main()
