import random
import sys
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap
import main as main
import Classes.player as Players
from GameStart import board as board

class GameWindow(QDialog):
    def __init__(self, username, startingBalance, moneyFromGo, numberOfPlayers, fastBankruptcy, rentFromJail, playerNames):
        super(GameWindow, self).__init__()
        loadUi('C:\\Users\\willj\\OneDrive\\Documents\\Y13\\coursework\\UI\\game.ui', self)
        self.boardImageLabel.setPixmap(QPixmap("C:\\Users\\willj\\OneDrive\\Documents\\Y13\\coursework\\gameBoard.png"))

        self.chanceCardTextBrowser.hide()
        self.endTurnButton.hide()
        self.bankruptButton.hide()
        self.rollDiceButton.hide()

        self.dice1Outline.hide()
        self.dice1dot1.hide()
        self.dice1dot2.hide()
        self.dice1dot3.hide()
        self.dice1dot4.hide()
        self.dice1dot5.hide()
        self.dice1dot6.hide()
        self.dice1dot7.hide()

        self.dice2Outline.hide()
        self.dice2dot1.hide()
        self.dice2dot2.hide()
        self.dice2dot3.hide()
        self.dice2dot4.hide()
        self.dice2dot5.hide()
        self.dice2dot6.hide()
        self.dice2dot7.hide()

        self.mortgageGroupBox.hide()
        self.housesGroupBox.hide()
        self.inJailGroupBox.hide()

        self.normalCardFrame.hide()
        self.utilityFrame.hide()
        self.travelSquareFrame.hide()

        self.displayLabel.setText("")
        self.transactionLabel.setText("")
        self.currentPlayerLabel.setText("")

        playerList = []

        if numberOfPlayers >= 1:
            self.player1NameLabel.setText(playerNames[0])
            self.player1BalanceLabel.setText(f"£{startingBalance}")
            player1 = Players.Player(1, playerNames[0], startingBalance)
            playerList.append(player1)
        else:
            self.player1NameLabel.hide()
            self.player1BalanceLabel.hide()
        
        if numberOfPlayers >= 2:
            self.player2NameLabel.setText(playerNames[1])
            self.player2BalanceLabel.setText(f"£{startingBalance}")
            player2 = Players.Player(2, playerNames[1], startingBalance)
            playerList.append(player2)
        else:
            self.player2NameLabel.hide()
            self.player2BalanceLabel.hide()

        if numberOfPlayers >= 3:
            self.player3NameLabel.setText(playerNames[2])
            self.player3BalanceLabel.setText(f"£{startingBalance}")
            player3 = Players.Player(3, playerNames[2], startingBalance)
            playerList.append(player3)
        else:
            self.player3NameLabel.hide()
            self.player3BalanceLabel.hide()

        if numberOfPlayers >= 4:
            self.player4NameLabel.setText(playerNames[3])
            self.player4BalanceLabel.setText(f"£{startingBalance}")
            player4 = Players.Player(4, playerNames[3], startingBalance)
            playerList.append(player4)
        else:
            self.player4NameLabel.hide()
            self.player4BalanceLabel.hide()

        if numberOfPlayers >= 5:
            self.player5NameLabel.setText(playerNames[4])
            self.player5BalanceLabel.setText(f"£{startingBalance}")
            player5 = Players.Player(5, playerNames[4], startingBalance)
            playerList.append(player5)
        else:
            self.player5NameLabel.hide()
            self.player5BalanceLabel.hide()

        if numberOfPlayers >= 6:
            self.player6NameLabel.setText(playerNames[5])
            self.player6BalanceLabel.setText(f"£{startingBalance}")
            player6 = Players.Player(6, playerNames[5], startingBalance)
            playerList.append(player6)
        else:
            self.player6NameLabel.hide()
            self.player6BalanceLabel.hide()

        if numberOfPlayers >= 7:
            self.player7NameLabel.setText(playerNames[6])
            self.player7BalanceLabel.setText(f"£{startingBalance}")
            player7 = Players.Player(7, playerNames[6], startingBalance)
            playerList.append(player7)
        else:
            self.player7NameLabel.hide()
            self.player7BalanceLabel.hide()

        if numberOfPlayers >= 8:
            self.player8NameLabel.setText(playerNames[7])
            self.player8BalanceLabel.setText(f"£{startingBalance}")
            player8 = Players.Player(8, playerNames[7], startingBalance)
            playerList.append(player8)
        else:
            self.player8NameLabel.hide()
            self.player8BalanceLabel.hide()

        self.brown1mortgaged.hide()
        self.brown2mortgaged.hide()
        self.lBlue1mortgaged.hide()
        self.lBlue2mortgaged.hide()
        self.lBlue3mortgaged.hide()
        self.pink1mortgaged.hide()
        self.pink2mortgaged.hide()
        self.pink3mortgaged.hide()
        self.orange1mortgaged.hide()
        self.orange2mortgaged.hide()
        self.orange3mortgaged.hide()
        self.red1mortgaged.hide()
        self.red2mortgaged.hide()
        self.red3mortgaged.hide()
        self.yellow1mortgaged.hide()
        self.yellow2mortgaged.hide()
        self.yellow3mortgaged.hide()
        self.green1mortgaged.hide()
        self.green2mortgaged.hide()
        self.green3mortgaged.hide()
        self.dBlue1mortgaged.hide()
        self.dBlue2mortgaged.hide()
        self.rr1mortgaged.hide()
        self.rr2mortgaged.hide()
        self.rr3mortgaged.hide()
        self.rr4mortgaged.hide()
        self.u1mortgaged.hide()
        self.u2mortgaged.hide()

        self.brown1ownership.hide()
        self.brown2ownership.hide()
        self.lBlue1ownership.hide()
        self.lBlue2ownership.hide()
        self.lBlue3ownership.hide()
        self.pink1ownership.hide()
        self.pink2ownership.hide()
        self.pink3ownership.hide()
        self.orange1ownership.hide()
        self.orange2ownership.hide()
        self.orange3ownership.hide()
        self.red1ownership.hide()
        self.red2ownership.hide()
        self.red3ownership.hide()
        self.yellow1ownership.hide()
        self.yellow2ownership.hide()
        self.yellow3ownership.hide()
        self.green1ownership.hide()
        self.green2ownership.hide()
        self.green3ownership.hide()
        self.dBlue1ownership.hide()
        self.dBlue2ownership.hide()
        self.rr1ownership.hide()
        self.rr2ownership.hide()
        self.rr3ownership.hide()
        self.rr4ownership.hide()
        self.u1ownership.hide()
        self.u2ownership.hide()

        gameEnded = False
        chanceCounter = 0
        randomList = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
        random.shuffle(randomList)

        while not gameEnded:
            for i in range (1,8):
                if numberOfPlayers >= i and not playerList[i].bankrupt:
                    self.currentPlayerLabel.setText(playerNames[i-1])
                    chanceCounter = playerList[i].playTurn(self, board, playerList, chanceCounter, randomList, moneyFromGo, fastBankruptcy, rentFromJail)

            
            counter = 0
            for player in playerList:
                if player.bankrupt:
                    counter += 1
            if counter == numberOfPlayers - 1:
                gameEnded = True
