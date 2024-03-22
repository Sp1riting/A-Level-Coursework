import sys
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap
import main as main
import Classes.player as Players

class GameWindow(QDialog):
    def __init__(self, username, startingBalance, moneyFromGo, numberOfPlayers, fastBankruptcy, rentFromJail, playerNames):
        super(GameWindow, self).__init__()
        loadUi('C:\\Users\\willj\\OneDrive\\Documents\\Y13\\coursework\\UI\\game.ui', self)
        self.boardImageLabel.setPixmap(QPixmap("C:\\Users\\willj\\OneDrive\\Documents\\Y13\\coursework\\gameBoard.png"))

        self.chanceCardTextBrowser.hide()
        self.endTurnButton.hide()
        self.bankruptButton.hide()

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

        playerList = []

        if len(playerNames) >= 1:
            self.player1NameLabel.setText(playerNames[0])
            self.player1BalanceLabel.setText(f"£{startingBalance}")
            player1 = Players.player(1, playerNames[0], startingBalance)
            playerList.append(player1)
        
        if len(playerNames) >= 2:
            self.player2NameLabel.setText(playerNames[1])
            self.player2BalanceLabel.setText(f"£{startingBalance}")
            player2 = Players.player(2, playerNames[1], startingBalance)
            playerList.append(player2)

        if len(playerNames) >= 3:
            self.player3NameLabel.setText(playerNames[2])
            self.player3BalanceLabel.setText(f"£{startingBalance}")
            player3 = Players.player(3, playerNames[2], startingBalance)
            playerList.append(player3)

        if len(playerNames) >= 4:
            self.player4NameLabel.setText(playerNames[3])
            self.player4BalanceLabel.setText(f"£{startingBalance}")
            player4 = Players.player(4, playerNames[3], startingBalance)
            playerList.append(player4)

        if len(playerNames) >= 5:
            self.player5NameLabel.setText(playerNames[4])
            self.player5BalanceLabel.setText(f"£{startingBalance}")
            player5 = Players.player(5, playerNames[4], startingBalance)
            playerList.append(player5)

        if len(playerNames) >= 6:
            self.player6NameLabel.setText(playerNames[5])
            self.player6BalanceLabel.setText(f"£{startingBalance}")
            player6 = Players.player(6, playerNames[5], startingBalance)
            playerList.append(player6)

        if len(playerNames) >= 7:
            self.player7NameLabel.setText(playerNames[6])
            self.player7BalanceLabel.setText(f"£{startingBalance}")
            player7 = Players.player(7, playerNames[6], startingBalance)
            playerList.append(player7)

        if len(playerNames) >= 8:
            self.player8NameLabel.setText(playerNames[7])
            self.player8BalanceLabel.setText(f"£{startingBalance}")
            player8 = Players.player(8, playerNames[7], startingBalance)
            playerList.append(player8)


