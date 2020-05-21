# hangman.py
# Alexandra French
""" I created this simple project to demonstrate all the basic aspects of Python
to new members of the Robotics Club of Central Florida """

import random									# Grab libraries that aren't already preloaded
from hangmanResource import hangmanPrintables	# Grab our utilities class (must be in same directory)

class hangman(hangmanPrintables):
	wordSoFar = ""					# String
	lettersGuessed = {""}			# Set

	def getMysteryWord(self):
		# Creating the lists for the combo of words
		allWords = ["citrobot", "bowser", "robots"]					# List
		allWords[2] = "demobot"										# Change robot to Demobot

		# Return a random word from the list
		return random.choice(allWords)

	def promptGuess(self, word, currentAttempt):
		while True:
			# print out letters so far
			print("You have guessed the following so far: ")
			print(self.lettersGuessed)
			
			# prompt for input, store used letters, and build the word so far
			guess = input("Guess a letter:")
			if guess in self.lettersGuessed:
				print("You already guessed this. Try again.\n\n")
				continue
			self.lettersGuessed.add(guess)
			self.buildWordSoFar(word)								# call inherited method

			return guess


	def main(self):
		mysteryWord = self.getMysteryWord()							# call native method
		wrongGuesses = 0;											# int

		self.printGameStart(mysteryWord)

		# Run through all guesses until the limit for guessing is hit
		while(wrongGuesses < 7):
			guess = self.promptGuess(mysteryWord, wrongGuesses)
			if "_" not in self.wordSoFar:							# Win
				self.printYouWin()
				return mysteryWord
			if guess not in self.wordSoFar:							# Incorrect letter
				print("Wrong letter")
				wrongGuesses += 1
			self.printProgress(wrongGuesses)
			print("{0} attempts left.".format(7 - wrongGuesses))

		self.printGameOver()

# This sets a base function to call, such as from the command line
if __name__ == "__main__":
	hangman().main()