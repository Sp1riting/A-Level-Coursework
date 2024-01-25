import GameStart as gameStart
import Classes.card as Cards
import Classes.player as Players
from GameStart import board as board

gameStart.defaultCardsAndBoard()
valid = False
gameEnded = False
turnEnded = False


while valid == False:
    numberOfPlayers = int(input("Enter the number of players in the game (2 to 8 players) "))
    if numberOfPlayers !=4:
        print("Only 4 players available for now until login dings are coded")
    else:
        newName = str(input(f"Enter the name of player number 1 "))
        player1 = Players.Player(1,newName)
        newName = str(input(f"Enter the name of player number 2 "))
        player2 = Players.Player(2,newName)
        newName = str(input(f"Enter the name of player number 3 "))
        player3 = Players.Player(3,newName)
        newName = str(input(f"Enter the name of player number 4 "))
        player4 = Players.Player(4,newName)
        valid = True

while gameEnded == False:

    if player1.bankrupt == False:
        turnEnded = False
        print(f"{player1.name}'s turn has started. They have a balance of {player1.balance}")
        while turnEnded == False:
            turnEnded = player1.playTurn(board)
        print(f"{player1.name}'s turn has ended")

    if player2.bankrupt == False:
        turnEnded = False
        print(f"{player2.name}'s turn has started. They have a balance of {player2.balance}")
        while turnEnded == False:
            turnEnded = player2.playTurn(board)
        print(f"{player2.name}'s turn has ended")

    if player3.bankrupt == False:
        turnEnded = False
        print(f"{player3.name}'s turn has started. They have a balance of {player3.balance}")
        while turnEnded == False:
            turnEnded = player3.playTurn(board)
        print(f"{player3.name}'s turn has ended")

    if player4.bankrupt == False:
        turnEnded = False
        print(f"{player4.name}'s turn has started. They have a balance of {player4.balance}")
        while turnEnded == False:
            turnEnded = player4.playTurn(board)
        print(f"{player4.name}'s turn has ended")

    

    
    