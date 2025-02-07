
#Jeff Calderon Assignment 1
# Python2.9
# A Wordle Game
# stores all correct guesses

from re import A
from Wordle import Wordle

class WordleGame(object):
	"""docstring for WordleGame"""
	def __init__(self):
		self.maxGuesses = 10
		self.nGuesses = 0

	def startGame(self):
		shortList = ['test']
		#puzzle = Wordle(wordList=shortList)
		puzzle = Wordle(file='norvig200.txt', length=5, minFreq=100000, maxFreq=978481319)
		puzzle.initGame()

		
		
		while(self.nGuesses < self.maxGuesses):
			self.nGuesses += 1
			token = input('Your guess: ')
			print("Got:'"+token+"'")
			h = puzzle.guess(token)
			if h:
				print(h)
				if h.isWin():
					print('You won in',self.nGuesses,'moves!')
					break
			else:
				print('...try again...')
				self.nGuesses += 1 #Don't want to count this one...

		if not h.isWin():
			print('Too many moves! You lose!')

def main():
	myGame = WordleGame()
	myGame.startGame()


if __name__ == '__main__':
	main()