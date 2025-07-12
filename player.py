import random

class Player:
    def __init__(self, name):
        self.name = name
        self.letters = []
        self.letter_ops = 'aaaaaaaaabbccddddeeeeeeeeeeeeffggghhiiiiiiiiijkllllmmnnnnnnooooooooppqrrrrrrssssttttttuuuuvvwwxyyz'
        for i in range(7):
            self.drawLetter()

    def getName(self):
        return self.name
    
    def getLetters(self):
        return self.letters
    
    def drawLetter(self):
        new_letter = random.choice(self.letter_ops)
        self.letters.append(new_letter)
        return new_letter
    
    def printLetters(self):
        return ' '.join(self.letters)
    
    def checkWord(self,word):
        original_letters = self.letters.copy()
        
        for l in word:
            if l in self.letters:
                self.letters.remove(l)
            else:
                self.letters = original_letters.copy()
                return False
        
        return True
        