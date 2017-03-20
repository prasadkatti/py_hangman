#!/usr/bin/env python

import unittest
from contextlib import contextmanager

from py_hangman.hangman import Hangman

# this code is take from:
# http://stackoverflow.com/questions/21046717/python-mocking-raw-input-in-unittests
@contextmanager
def mock_raw_input(mock):
    original_raw_input = __builtins__.raw_input
    __builtins__.raw_input = lambda _: mock
    yield
    __builtins__.raw_input = original_raw_input


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

        with mock_raw_input('foo'):
            self.assertIsNone(h._accept_guess(), "test - accept guess - 1")

        with mock_raw_input('123'):
            self.assertIsNone(h._accept_guess(), "test - accept guess - 2")

        h.guesses = {'a', 'b', 'c'}
        with mock_raw_input('a'):
            self.assertIsNone(h._accept_guess(), "test - accept guess - 3")

    def test_make_partial_answer(self):
        h = Hangman()
        self.assertRaises(Exception, h._make_partial_answer)

        h.answer = "foobar"
        h.guesses = set("abc")
        self.assertEqual(h._make_partial_answer(), "***ba*", "test- make partial answer - 2")


if __name__ == '__main__':
    unittest.main()
