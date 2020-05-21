# hangmanResource.py
# Alexandra French
# I created this simple project to demonstrate all the basic aspects of Python
# to new members of the Robotics Club of Central Florida.
# This class contains quick grab printing utilities for hangman.
# Plus one building utility.

class hangmanPrintables:
	incorrectGuesses = 0

	def getPrintableHangman(self):
		return ["""
		    ------
		    |    |
		         |
		         |
		         |
		         |
		 ==========
		 ""","""
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

	def printGameStart(self, word):
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
		self.buildWordSoFar(word)
		self.printProgress(0)
		print("")

	def printGameOver(self):
		# Prints out a game over screen
		self.printHangman()
		print("""
		+-----------+
		| GAME OVER |
		+-----------+
		""")

	def printYouWin(self):
		# Prints out a game win screen
		self.printProgress(self.incorrectGuesses)
		print("""
		+----------+
		| You Win! |
		+----------+
		""")

	def printHangman(self):
		# Print the hangman corresponding to the number of attempts used
		printableHangman = self.getPrintableHangman();
		print(printableHangman[self.incorrectGuesses])

	def printProgress(self, wrongGuesses):
		# Add to an internal global, to make calling the functions easier
		self.incorrectGuesses = wrongGuesses

		# Print out the hangman, and below it, the word so far.
		self.printHangman()
		print("\t    ", end=" ")
		print(self.wordSoFar+"\n")
		
	def buildWordSoFar(self, word):
		# Always rebuild the word
		self.wordSoFar = ""

		# If any char is in letters guessed, print the letter
		# If the char is not in the letters guessed, print out placeholder
		for char in word:
			if char in self.lettersGuessed:
				self.wordSoFar += " " + char + " "
			else:
				self.wordSoFar += " _ "

	
