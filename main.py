import random
import GameStart as gameStart
import Classes.card as Cards
import Classes.player as Players
from GameStart import board as board


def playGame(numberOfPlayers, startingBalance, moneyFromGo, fastBankruptcy, rentFromJail):
    gameStart.defaultCardsAndBoard()
    valid = False
    gameEnded = False
    chanceCounter = 0
    randomList = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    random.shuffle(randomList)

    playerList = []
    
    if numberOfPlayers >= 1:
        newName = str(input("Enter the name of player number 1 "))
        player1 = Players.Player(1, newName, startingBalance)
        playerList.append(player1)

    if numberOfPlayers >= 2:
        newName = str(input("Enter the name of player number 2 "))
        player2 = Players.Player(2, newName, startingBalance)
        playerList.append(player2)

    if numberOfPlayers >= 3:
        newName = str(input("Enter the name of player number 3 "))
        player3 = Players.Player(3, newName, startingBalance)
        playerList.append(player3)

    if numberOfPlayers >= 4:
        newName = str(input("Enter the name of player number 4 "))
        player4 = Players.Player(4, newName, startingBalance)
        playerList.append(player4)

    if numberOfPlayers >= 5:
        newName = str(input("Enter the name of player number 5 "))
        player5 = Players.Player(5, newName, startingBalance)
        playerList.append(player5)
    
    if numberOfPlayers >= 6:
        newName = str(input("Enter the name of player number 6 "))
        player6 = Players.Player(6, newName, startingBalance)
        playerList.append(player6)

    if numberOfPlayers >= 7:
        newName = str(input("Enter the name of player number 7 "))
        player7 = Players.Player(7, newName, startingBalance)
        playerList.append(player7)

    if numberOfPlayers >= 8:
        newName = str(input("Enter the name of player number 8 "))
        player8 = Players.Player(8, newName, startingBalance)
        playerList.append(player8)


    while not gameEnded:

        if numberOfPlayers >=1 and not player1.bankrupt:
            print(f"{player1.name}'s turn has started. They have a balance of {player1.balance}")
            chanceCounter = player1.playTurn(board, playerList, chanceCounter, randomList, moneyFromGo, fastBankruptcy, rentFromJail)
            print(f"{player1.name}'s turn has ended")
            print("")

        if numberOfPlayers >=2 and not player2.bankrupt:
            print(f"{player2.name}'s turn has started. They have a balance of {player2.balance}")
            chanceCounter = player2.playTurn(board, playerList, chanceCounter, randomList, moneyFromGo, fastBankruptcy, rentFromJail)
            print(f"{player2.name}'s turn has ended")
            print("")

        if numberOfPlayers >=3 and not player3.bankrupt:
            print(f"{player3.name}'s turn has started. They have a balance of {player3.balance}")
            chanceCounter = player3.playTurn(board, playerList, chanceCounter, randomList, moneyFromGo, fastBankruptcy, rentFromJail)
            print(f"{player3.name}'s turn has ended")
            print("")

        if numberOfPlayers >=4 and not player4.bankrupt:
            print(f"{player4.name}'s turn has started. They have a balance of {player4.balance}")
            chanceCounter = player4.playTurn(board, playerList, chanceCounter, randomList, moneyFromGo, fastBankruptcy, rentFromJail)
            print(f"{player4.name}'s turn has ended")
            print("")

        if numberOfPlayers >=5 and not player5.bankrupt:
            print(f"{player5.name}'s turn has started. They have a balance of {player5.balance}")
            chanceCounter = player5.playTurn(board, playerList, chanceCounter, randomList, moneyFromGo, fastBankruptcy, rentFromJail)
            print(f"{player5.name}'s turn has ended")
            print("")

        if numberOfPlayers >=6 and not player6.bankrupt:
            print(f"{player6.name}'s turn has started. They have a balance of {player6.balance}")
            chanceCounter = player6.playTurn(board, playerList, chanceCounter, randomList, moneyFromGo, fastBankruptcy, rentFromJail)
            print(f"{player6.name}'s turn has ended")
            print("")

        if numberOfPlayers >=7 and not player7.bankrupt:
            print(f"{player7.name}'s turn has started. They have a balance of {player7.balance}")
            chanceCounter = player7.playTurn(board, playerList, chanceCounter, randomList, moneyFromGo, fastBankruptcy, rentFromJail)
            print(f"{player7.name}'s turn has ended")
            print("")

        if numberOfPlayers >=8 and not player8.bankrupt:
            print(f"{player8.name}'s turn has started. They have a balance of {player8.balance}")
            chanceCounter = player8.playTurn(board, playerList, chanceCounter, randomList, moneyFromGo, fastBankruptcy, rentFromJail)
            print(f"{player8.name}'s turn has ended")
            print("")
        
        counter = 0
        for player in playerList:
            if player.bankrupt:
                counter += 1
        if counter == len(playerList) - 1:
            gameEnded = True


valid = False

while not valid:
    valid = True

    if input("Do you want players to be instantly bankrupted? (y/n) ") == 'y':
        fastBankruptcy = True
    else:
        fastBankruptcy = False
    
    if input("Do you want players to gain rent from jail? (y/n) ") == 'y':
        rentFromJail = True
    else:
        rentFromJail = False

    numberOfPlayers = int(input("Enter the number of players in the game (2 to 8) "))
    startingBalance = int(input("Enter starting balance of players (0 to 10000) "))
    moneyFromGo = int(input("Enter money gained from Go from players (0 to 2000) "))

    if numberOfPlayers < 2 or numberOfPlayers > 8:
        print("Number of players is not valid")
        valid = False
    if startingBalance > 10000 or startingBalance < 0:
        print("Starting balance is not valid")
        valid = False
    if moneyFromGo > 2000 or startingBalance < 0:
        print("Money from Go is not valid")
        valid = False
    
    if valid == False and input("Do you want to go with the default values? You can reenter settings if not (y/n) ") == 'y':
        numberOfPlayers = 4
        startingBalance = 1500
        moneyFromGo = 200


playGame(numberOfPlayers, startingBalance, moneyFromGo, fastBankruptcy, rentFromJail)
print("Game has ended")