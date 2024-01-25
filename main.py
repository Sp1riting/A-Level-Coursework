import random
import GameStart as gameStart
import Classes.card as Cards
import Classes.player as Players
from GameStart import board as board

valid = False
gameEnded = False



while valid == False:
    numberOfPlayers = int(input("Enter the number of players in the game (2 to 8 players) "))
    if numberOfPlayers !=4:
        print("Only 4 players available for now until login dings are coded")
    else:
        newName = str(input(f"Enter the name of player number 1 "))
        player1 = Players.Player(1,newName)
        valid = True
        
while gameEnded == False:
    player1.playTurn(board)

    

    
    