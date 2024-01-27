import GameStart as gameStart
import Classes.card as Cards
import Classes.player as Players
from GameStart import board as board

gameStart.defaultCardsAndBoard()
valid = False
gameEnded = False
turnEnded = False
chanceCounter = 0

while not valid:
    numberOfPlayers = int(input("Enter the number of players in the game (2 to 8 players) "))
    if numberOfPlayers < 2 or numberOfPlayers > 8:
        print("Please enter a valid number")
    else:
        playerList = []
        
        if numberOfPlayers >= 1:
            newName = str(input("Enter the name of player number 1 "))
            player1 = Players.Player(1,newName)
            playerList.append(player1)

        if numberOfPlayers >= 2:
            newName = str(input("Enter the name of player number 2 "))
            player2 = Players.Player(2,newName)
            playerList.append(player2)

        if numberOfPlayers >= 3:
            newName = str(input("Enter the name of player number 3 "))
            player3 = Players.Player(3,newName)
            playerList.append(player3)

        if numberOfPlayers >= 4:
            newName = str(input("Enter the name of player number 4 "))
            player4 = Players.Player(4,newName)
            playerList.append(player4)

        if numberOfPlayers >= 5:
            newName = str(input("Enter the name of player number 5 "))
            player5 = Players.Player(5,newName)
            playerList.append(player5)
        
        if numberOfPlayers >= 6:
            newName = str(input("Enter the name of player number 6 "))
            player6 = Players.Player(6,newName)
            playerList.append(player6)

        if numberOfPlayers >= 7:
            newName = str(input("Enter the name of player number 7 "))
            player7 = Players.Player(7,newName)
            playerList.append(player7)

        if numberOfPlayers >= 8:
            newName = str(input("Enter the name of player number 8 "))
            player8 = Players.Player(8,newName)
            playerList.append(player8)

        valid = True


while not gameEnded:

    if numberOfPlayers >=1 and not player1.bankrupt:
        turnEnded = False
        print(f"{player1.name}'s turn has started. They have a balance of {player1.balance}")
        while not turnEnded:
            turnEnded = player1.playTurn(board, playerList, chanceCounter)
        print(f"{player1.name}'s turn has ended")
        print("")

    if numberOfPlayers >=2 and not player2.bankrupt:
        turnEnded = False
        print(f"{player2.name}'s turn has started. They have a balance of {player2.balance}")
        while not turnEnded:
            turnEnded = player2.playTurn(board, playerList, chanceCounter)
        print(f"{player2.name}'s turn has ended")
        print("")

    if numberOfPlayers >=3 and not player3.bankrupt:
        turnEnded = False
        print(f"{player3.name}'s turn has started. They have a balance of {player3.balance}")
        while not turnEnded:
            turnEnded = player3.playTurn(board, playerList, chanceCounter)
        print(f"{player3.name}'s turn has ended")
        print("")

    if numberOfPlayers >=4 and not player4.bankrupt:
        turnEnded = False
        print(f"{player4.name}'s turn has started. They have a balance of {player4.balance}")
        while not turnEnded:
            turnEnded = player4.playTurn(board, playerList, chanceCounter)
        print(f"{player4.name}'s turn has ended")
        print("")

    if numberOfPlayers >=5 and not player5.bankrupt:
        turnEnded = False
        print(f"{player5.name}'s turn has started. They have a balance of {player5.balance}")
        while not turnEnded:
            turnEnded = player5.playTurn(board, playerList, chanceCounter)
        print(f"{player5.name}'s turn has ended")
        print("")

    if numberOfPlayers >=6 and not player6.bankrupt:
        turnEnded = False
        print(f"{player6.name}'s turn has started. They have a balance of {player6.balance}")
        while not turnEnded:
            turnEnded = player6.playTurn(board, playerList, chanceCounter)
        print(f"{player6.name}'s turn has ended")
        print("")

    if numberOfPlayers >=7 and not player7.bankrupt:
        turnEnded = False
        print(f"{player7.name}'s turn has started. They have a balance of {player7.balance}")
        while not turnEnded:
            turnEnded = player7.playTurn(board, playerList, chanceCounter)
        print(f"{player7.name}'s turn has ended")
        print("")

    if numberOfPlayers >=8 and not player8.bankrupt:
        turnEnded = False
        print(f"{player8.name}'s turn has started. They have a balance of {player8.balance}")
        while not turnEnded:
            turnEnded = player8.playTurn(board, playerList, chanceCounter)
        print(f"{player8.name}'s turn has ended")
        print("")