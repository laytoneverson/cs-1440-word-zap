from player import Player
import sys

def getUserString(prompt):
    return str(input(prompt)).strip()

def getUserInt(prompt):
    user_input = ''
    while user_input == '':
        try:
            user_input = int(input(prompt))
            if user_input <= 0:
                raise Exception('Please enter a number greater than zero.')
        except ValueError:
            print("Please enter a number.")
            user_input = ''
        except Exception as e:
            print(str(e))
            user_input = ''

    return user_input

def playTurn(player):
    while True: 
        print(f"{player.getName()}, it is your turn!")
        print(f"Your letters are: {player.printLetters()}")
    
        word = getUserString('Enter a word to play (or press enter to pass) ').lower()
        print('You enetered ' + word)
        if word == '':
            newLetter = player.drawLetter() 
            print(f'You get another letter, "{newLetter}"!\n')
            return None     
        
        if player.checkWord(word):
            print('Great job!')
            return len(player.getLetters()) == 0
         
        print('Check your letters and try again!\n')


def getPlayers():
    numPlayers = getUserInt('How many players will be playing? ')
    players = []
    for i in range(1, numPlayers + 1):
        playerName = getUserString(f'Enter name for player {i}? ')
        players.append(Player(playerName))
    
    return players 

def main():
    print('Welcome! Time to play! Try to use all of your letters.')
    print('The first player that uses all of their letters wins!')
    players = getPlayers()
    winner = None
    while winner is None:        
        for p in players:
            result = playTurn(p)
        for p in players:
            if len(p.getLetters()) == 0:
                winner = p.getName()
                break
            
    print(f'{winner} wins!')
    
if __name__ == '__main__':
    main()