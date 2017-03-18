#!/usr/bin/env python

import getpass


class Hangman(object):

    MAX_NUM_CHANCES = 5

    SUCCESS_MSG = "You have got it. The word to guess was - \n{0}\nGood Job."

    FAILURE_MSG = "Sorry. Better luck next time. The word to guess was - \n\n{0}\n"

    INVALID_GUESS_MSG = "\n!!! Invalid guess. Needs to be a single character. !!!\n"

    WELCOME_MSG = ("\n{0}\n\nThis is the 2 player version. Player A decides a word which "
                   "Player B will guess.\n".format(" Welcome to Hangman! ".center(79, '=')))

    PLAYER_A_TURN = " Player A ".center(79, '-')

    PLAYER_B_TURN = " Player B ".center(79, '-')


    def __init__(self):
        self.chances = self.MAX_NUM_CHANCES
        self.guesses = set()

    def _welcome_msg(self):
        print self.WELCOME_MSG

    def _get_quiz_word(self):
        print self.PLAYER_A_TURN
        self.answer = getpass.getpass("Enter the word to guess: ")

    def _make_partial_answer(self):
        if hasattr(self, 'answer'):
            return ''.join([i if i in self.guesses or not i.isalpha() else '*' for i in self.answer])
        else:
            raise Exception("Player A hasn't picked a word yet!")

    def _accept_apply_guess(self):
        print self.PLAYER_B_TURN
        print "\n{0}\n".format(self._make_partial_answer().center(79, ' '))
        print "Chances left {0}".format(self.chances)
        guess = raw_input("Enter a char: ")
        if len(guess) != 1 or not guess.isalpha():
            print self.INVALID_GUESS_MSG
            return
        self.guesses.add(guess)
        self.guesses.add(guess.swapcase())
        if guess not in self.answer:
            self.chances -= 1

    def _word_guessed(self):
        return self.answer == self._make_partial_answer()

    def start_game(self):
        self._welcome_msg()
        self._get_quiz_word()
        while self.chances:
            self._accept_apply_guess()
            if self._word_guessed():
                print self.SUCCESS_MSG.format(self.answer.center(79, ' '))
                return
        print self.FAILURE_MSG.format(self.answer.center(79, ' '))


if __name__ == "__main__":
    try:
        Hangman().start_game()
    except KeyboardInterrupt:
        print
        print " Goodbye! ".center(79, '*')