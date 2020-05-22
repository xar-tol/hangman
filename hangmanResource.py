# hangmanResource.py
# Alexandra French
# I created this simple project to demonstrate all the basic aspects of Python
# to new members of the Robotics Club of Central Florida.
# This class contains quick grab printing utilities for hangman.
# Plus one building utility.


def get_printable_hangman():
    return ["""
        ------
        |    |
             |
             |
             |
             |
     ==========
     """, """
        ------
        |    |
      [o o]  |
             |
             |
             |
     ==========
     """,
            """
        ------
        |    |
      [o o]  |
        |    |
             |
             |
     ==========
     """,
            """
        ------
        |    |
      [o o]  |
       /|    |
             |
             |
     ==========
     """,
            """
        ------
        |    |
      [o o]  |
       /|\\   |
             |
             |
     ==========
     """,
            """
        ------
        |    |
      [o o]  |
       /|\\   |
        |    |
             |
     ==========
     """,
            """
        ------
        |    |
      [o o]  |
       /|\\   |
        |    |
       /     |
     ==========
     """,
            """
        ------
        |    |
      [o o]  |
       /|\\   |
        |    |
       / \\   |
     ==========
     """]


def print_game_over():
    # Prints out a game over screen
    print("""
    +-----------+
    | GAME OVER |
    +-----------+
    """)


class HangmanPrintables:
    incorrect_guesses = 0
    word_so_far = ""
    letters_guessed = {""}

    def print_game_start(self, word):
        # Prints out the starting screen and rules
        print("""
        +------------+
        | GAME START |
        +------------+""")
        print("\nWelcome to hangman!")
        print("The rules are simple. Guess a letter.")
        print("For every wrong guess, a part of the robot is drawn.")
        print("Don't let the whole robot be drawn!")
        print("\n\n")

        # prints out the initial hangman and blank letters
        self.build_word_so_far(word)
        self.print_progress(0)
        print("")

    def print_you_win(self):
        # Prints out a game win screen
        self.print_progress(self.incorrect_guesses)
        print("""
        +----------+
        | You Win! |
        +----------+
        """)

    def print_hangman(self):
        # Print the hangman corresponding to the number of attempts used
        printable_hangman = get_printable_hangman()
        print(printable_hangman[self.incorrect_guesses])

    def print_progress(self, wrong_guesses):
        # Add to an internal global, to make calling the functions easier
        self.incorrect_guesses = wrong_guesses

        # Print out the hangman, and below it, the word so far.
        self.print_hangman()
        print("        ", end=" ")
        print(self.word_so_far + "\n")

    def build_word_so_far(self, word):
        # Always rebuild the word
        self.word_so_far = ""

        # If any char is in letters guessed, print the letter
        # If the char is not in the letters guessed, print out placeholder
        for char in word:
            if char in self.letters_guessed:
                self.word_so_far += " " + char + " "
            else:
                self.word_so_far += " _ "
