# hangman.py
# Alexandra French
""" I created this simple project to demonstrate all the basic aspects of Python
to new members of the Robotics Club of Central Florida """

import random                                   # Grab libraries that aren't already preloaded
from hangmanResource import HangmanPrintables   # Grab our utilities class (must be in same directory)


def get_mystery_word():
    # Creating the lists for the combo of words
    all_words = ["citrobot", "bowser", "robots"]  # List
    all_words[2] = "demobot"                      # Change robot to Demobot

    # Return a random word from the list
    return random.choice(all_words)


class Hangman(HangmanPrintables):
    word_so_far = ""                              # String
    letters_guessed = {""}                        # Set

    def prompt_guess(self, word):
        while True:
            # print out letters so far
            print("You have guessed the following so far: ")
            print(self.letters_guessed)

            # prompt for input, store used letters, and build the word so far
            guess = input("Guess a letter:")
            if guess in self.letters_guessed:
                print("You already guessed this. Try again.\n\n")
                continue
            self.letters_guessed.add(guess)
            self.build_word_so_far(word)                        # call inherited method

            return guess

    def main(self):
        mystery_word = get_mystery_word()                       # call included method
        wrong_guesses = 0                                       # int

        self.print_game_start(mystery_word)

        # Run through all guesses until the limit for guessing is hit
        while wrong_guesses < 7:
            guess = self.prompt_guess(mystery_word)
            if "_" not in self.word_so_far:                       # Win
                self.print_you_win()
                return mystery_word
            if guess not in self.word_so_far:                     # Incorrect letter
                print("Wrong letter")
                wrong_guesses += 1
            self.print_progress(wrong_guesses)
            print("{0} attempts left.".format(7 - wrong_guesses))

        self.print_game_over()


# This sets a base function to call, such as from the command line
if __name__ == "__main__":
    Hangman().main()
