import GameStart as gameStart
import Classes.card as Cards
import Classes.player as Players
from GameStart import board as board

gameStart.defaultCardsAndBoard()
valid = False
gameEnded = False
turnEnded = False


while not valid:
    numberOfPlayers = int(input("Enter the number of players in the game (2 to 8 players) "))
    if numberOfPlayers !=4:
        print("Only 4 players available for now until login dings are coded")
    else:
        playerList = []
        
        newName = str(input("Enter the name of player number 1 "))
        player1 = Players.Player(1,newName)
        playerList.append(player1)

        newName = str(input("Enter the name of player number 2 "))
        player2 = Players.Player(2,newName)
        playerList.append(player2)

        newName = str(input("Enter the name of player number 3 "))
        player3 = Players.Player(3,newName)
        playerList.append(player3)

        newName = str(input("Enter the name of player number 4 "))
        player4 = Players.Player(4,newName)
        playerList.append(player4)

        valid = True



while not gameEnded:

    if not player1.bankrupt:
        turnEnded = False
        print(f"{player1.name}'s turn has started. They have a balance of {player1.balance}")
        while not turnEnded:
            turnEnded = player1.playTurn(board,playerList)
        print(f"{player1.name}'s turn has ended")

    if not player2.bankrupt:
        turnEnded = False
        print(f"{player2.name}'s turn has started. They have a balance of {player2.balance}")
        while not turnEnded:
            turnEnded = player2.playTurn(board,playerList)
        print(f"{player2.name}'s turn has ended")

    if not player3.bankrupt:
        turnEnded = False
        print(f"{player3.name}'s turn has started. They have a balance of {player3.balance}")
        while not turnEnded:
            turnEnded = player3.playTurn(board,playerList)
        print(f"{player3.name}'s turn has ended")

    if not player4.bankrupt:
        turnEnded = False
        print(f"{player4.name}'s turn has started. They have a balance of {player4.balance}")
        while not turnEnded:
            turnEnded = player4.playTurn(board,playerList)
        print(f"{player4.name}'s turn has ended")
