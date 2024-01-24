import random
import GameStart as gameStart
import Classes.Card as Cards
import Classes.Player as Players

valid = False
gameEnded = False
board = gameStart.defaultCardsAndBoard()


while valid == False:
    numberOfPlayers = int(input("Enter the number of players in the game (2 to 8 players) "))
    if numberOfPlayers !=4:
        print("Only 4 players available for now until login dings are coded")
    else:
        newName = str(input(f"Enter the name of player number 1 "))
        player1 = Players.Player(1,newName,1500,[],0,0,0,False,False,0,0,0,0)
        #newName = str(input(f"Enter the name of player number 2 "))
        #player2 = Players.Player(2,newName,1500,[],0,0,0,False,False,0,0,0,0)
        #newName = str(input(f"Enter the name of player number 3 "))
        #player3 = Players.Player(3,newName,1500,[],0,0,0,False,False,0,0,0,0)
        #newName = str(input(f"Enter the name of player number 4 "))
        #player4 = Players.Player(4,newName,1500,[],0,0,0,False,False,0,0,0,0)
        valid = True
        
        
while gameEnded == False:
    roll = player1.rollDice()
    player1.currentPos = player1.movePlayer(roll)
    if player1.inJail:
        player1.playInJail()
    else:
        player1.checkPosition(board)
    player1.doublesCount = 0

    
    