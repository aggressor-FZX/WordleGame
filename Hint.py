#
#
#
# I used arrays since they are nice to iterate over and can be joined easily
# When I need strings I just ''.join() thia works nicely
# The initial call to Hint makes a class var exactly the right size list "state_array"
# The instance var is also kept seperate to show mistakes made, correct letters etc.
# But the class var remembers the progress and won't forget. 
# I had to make a call_num counter to make sure I don't over write the class var each guess
# only on the first call do I init class var state_array to list of n = word size
# after I only update the class var state_array upon correct guesses

class Hint(object):
    """docstring for Hint"""
    #class variable remembers all correct guesses
    #remembers all letters not in puzzle
    state_array = []
    wrong_let = []
    call_num = 0

    def __init__(self, guess, secretWord):

        self.guess = guess
        self.sec_word = secretWord
        self.wrong_place = []
        #instance var remembers latest guess
        self.state_array = Hint.state_array 
        self.guess_state()

		
    def guess_state(self):
        self.state_array = ['-' for x in range(len(self.guess))]
        self. wrong_place = self.state_array[:] # need a shallow copy
        self.update()


    def isWin(self):

        if self.guess == self.sec_word:
            return True

        elif ''.join(self.state_array)==self.sec_word:
            return True

        else:
            return False

            
    def update(self):
        Hint.call_num += 1
        
        #Needs to initialize a list with n entries or will throw err at list[n]
        if Hint.call_num == 1:
            Hint.state_array = self.state_array

        for i, (g_char, s_char) in enumerate( zip(self.guess, self.sec_word) ): 
            if(g_char == s_char):

                self.state_array[i] = s_char   
                Hint.state_array[i] = s_char

            elif(g_char in self.sec_word):

                self.wrong_place[i] = g_char
                
            else:
                if(g_char not in Hint.wrong_let):
                    Hint.wrong_let.append(g_char)

  


    def __repr__(self):
        
        hint_string = ''.join(Hint.state_array) 
        last_attempt = ''.join(self.state_array)
        wrong_place = ''.join(self.wrong_place)

        return (f"Last attempt had correct letters: {last_attempt}\n"
                f"Incorrectly placed: {wrong_place}\n"
                f"Correctly placed the following letters: {hint_string}\n"
                f"Not in the puzzle: {Hint.wrong_let}")