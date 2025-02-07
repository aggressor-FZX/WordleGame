from genericpath import samefile
from operator import length_hint
import random
from Hint import Hint


#this is way for h.isWin to be false rather than for h to be bool since bool has no isWin method
#at the same time that "if h:" is false
class FalsyHint:
    def __init__(self, len):
        self.len = len

    def __bool__(self):
        return False
    def isWin(self):
        return False
    def __repr__(self):
        return f" The guess must have {self.len} letters"


   #I tried to use all the methods listed but didn't feel like i needed so many
class Wordle(object):
    """docstring for Wordle"""
    def __init__(self, file=None, wordList=[], length=0, minFreq=-1, maxFreq=-1):

        self.w_list = wordList
        self.sec_word = ''
        self.getKnownWords(file, length, minFreq, maxFreq)


    def numberOfKnownWords(self, file, length, minFreq, maxFreq):

        words = []

        with open(file, 'r') as openfile:
            print(f'the word size is {length}')
            for line in openfile:
                line_info = line.split()
                if len(line_info[0]) == length:
                    if ( int(line_info[1]) > minFreq and int(line_info[1]) < maxFreq ) :
                        
                        self.w_list.append(line_info[0])

                        words.append(line_info[0])
        return words

 
    def getKnownWords(self, file, length, minFreq, maxFreq):
        self.w_list = self.loadWords(file, length, minFreq, maxFreq)
        return self.w_list 


    def loadWords(self, file, length, minFreq, maxFreq):
        # Since leaving maxFreq at 0 wont return anything
        # I have to make it super big  
        if maxFreq == 0 : self.maxFreq = 100000000000000000

        words = self.numberOfKnownWords(file, length, minFreq, maxFreq)

        return  words
        

    
    # Prepare the game for playing by choosing a new secret word.
    def initGame(self):
        self.sec_word = random.choice(self.w_list)
        #print(f"secret word is {self.sec_word}")
       


    def guess(self, guess):
        if len(self.sec_word) != len(guess):
           fhint = FalsyHint(len(self.sec_word)) 
           print(fhint)
           return fhint

        hint = Hint(guess, self.sec_word)

        return hint



                    


                

