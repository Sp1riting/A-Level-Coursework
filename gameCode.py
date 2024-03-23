import random
import sys
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap
import main as main
import Classes.newPlayer as Players
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
            player1 = Players.Player(1, playerNames[0], startingBalance, self.player1token, "a80000")
            playerList.append(player1)
        else:
            self.player1NameLabel.hide()
            self.player1BalanceLabel.hide()
        
        if numberOfPlayers >= 2:
            self.player2NameLabel.setText(playerNames[1])
            self.player2BalanceLabel.setText(f"£{startingBalance}")
            player2 = Players.Player(2, playerNames[1], startingBalance, self.player2token, "73ba23")
            playerList.append(player2)
        else:
            self.player2NameLabel.hide()
            self.player2BalanceLabel.hide()

        if numberOfPlayers >= 3:
            self.player3NameLabel.setText(playerNames[2])
            self.player3BalanceLabel.setText(f"£{startingBalance}")
            player3 = Players.Player(3, playerNames[2], startingBalance, self.player3token, "003eeb")
            playerList.append(player3)
        else:
            self.player3NameLabel.hide()
            self.player3BalanceLabel.hide()

        if numberOfPlayers >= 4:
            self.player4NameLabel.setText(playerNames[3])
            self.player4BalanceLabel.setText(f"£{startingBalance}")
            player4 = Players.Player(4, playerNames[3], startingBalance, self.player4token, "ffb300")
            playerList.append(player4)
        else:
            self.player4NameLabel.hide()
            self.player4BalanceLabel.hide()

        if numberOfPlayers >= 5:
            self.player5NameLabel.setText(playerNames[4])
            self.player5BalanceLabel.setText(f"£{startingBalance}")
            player5 = Players.Player(5, playerNames[4], startingBalance, self.player5token, "00d6e1")
            playerList.append(player5)
        else:
            self.player5NameLabel.hide()
            self.player5BalanceLabel.hide()

        if numberOfPlayers >= 6:
            self.player6NameLabel.setText(playerNames[5])
            self.player6BalanceLabel.setText(f"£{startingBalance}")
            player6 = Players.Player(6, playerNames[5], startingBalance, self.player6token, "6a533f")
            playerList.append(player6)
        else:
            self.player6NameLabel.hide()
            self.player6BalanceLabel.hide()

        if numberOfPlayers >= 7:
            self.player7NameLabel.setText(playerNames[6])
            self.player7BalanceLabel.setText(f"£{startingBalance}")
            player7 = Players.Player(7, playerNames[6], startingBalance, self.player7token, "ad17cb")
            playerList.append(player7)
        else:
            self.player7NameLabel.hide()
            self.player7BalanceLabel.hide()

        if numberOfPlayers >= 8:
            self.player8NameLabel.setText(playerNames[7])
            self.player8BalanceLabel.setText(f"£{startingBalance}")
            player8 = Players.Player(8, playerNames[7], startingBalance, self.player8token, "000000")
            playerList.append(player8)
        else:
            self.player8NameLabel.hide()
            self.player8BalanceLabel.hide()

        mortgageIndicators = ["N/A", 
                              self.brown1mortgaged, 
                              "N/A", 
                              self.brown2mortgaged, 
                              "N/A", 
                              self.rr1mortgaged, 
                              self.lBlue1mortgaged, 
                              "N/A", 
                              self.lBlue2mortgaged, 
                              self.lBlue3mortgaged, 
                              "N/A", 
                              self.pink1mortgaged, 
                              self.u1mortgaged, 
                              self.pink2mortgaged, 
                              self.pink3mortgaged,
                              self.rr2mortgaged,
                              self.orange1mortgaged,
                              "N/A",
                              self.orange2mortgaged,
                              self.orange3mortgaged,
                              "N/A",
                              self.red1mortgaged,
                              "N/A",
                              self.red2mortgaged,
                              self.red3mortgaged,
                              self.rr3mortgaged,
                              self.yellow1mortgaged,
                              self.yellow2mortgaged,
                              self.u2mortgaged,
                              self.yellow3mortgaged,
                              "N/A",
                              self.green1mortgaged,
                              self.green2mortgaged,
                              "N/A",
                              self.green3mortgaged,
                              self.rr4mortgaged,
                              "N/A",
                              self.dBlue1mortgaged,
                              "N/A",
                              self.dBlue2mortgaged
                              ]

        for i in mortgageIndicators:
            if not mortgageIndicators[i] == "N/A":
                mortgageIndicators[i].hide()
        
        ownershipIndicators = ["N/A", 
                              self.brown1ownership, 
                              "N/A", 
                              self.brown2ownership, 
                              "N/A", 
                              self.rr1ownership, 
                              self.lBlue1ownership, 
                              "N/A", 
                              self.lBlue2ownership, 
                              self.lBlue3ownership, 
                              "N/A", 
                              self.pink1ownership, 
                              self.u1ownership, 
                              self.pink2ownership, 
                              self.pink3ownership,
                              self.rr2ownership,
                              self.orange1ownership,
                              "N/A",
                              self.orange2ownership,
                              self.orange3ownership,
                              "N/A",
                              self.red1ownership,
                              "N/A",
                              self.red2ownership,
                              self.red3ownership,
                              self.rr3ownership,
                              self.yellow1ownership,
                              self.yellow2ownership,
                              self.u2ownership,
                              self.yellow3ownership,
                              "N/A",
                              self.green1ownership,
                              self.green2ownership,
                              "N/A",
                              self.green3ownership,
                              self.rr4ownership,
                              "N/A",
                              self.dBlue1ownership,
                              "N/A",
                              self.dBlue2ownership
                              ]

        for i in ownershipIndicators:
            if not ownershipIndicators[i] == "N/A":
                ownershipIndicators[i].hide()

        houseIndicators = ["N/A", 
                              self.brown1lcdNumber, 
                              "N/A", 
                              self.brown2lcdNumber, 
                              "N/A", 
                              "N/A",
                              self.lBlue1lcdNumber, 
                              "N/A", 
                              self.lBlue2lcdNumber, 
                              self.lBlue3lcdNumber, 
                              "N/A", 
                              self.pink1lcdNumber, 
                              "N/A",
                              self.pink2lcdNumber, 
                              self.pink3lcdNumber,
                              "N/A",
                              self.orange1lcdNumber,
                              "N/A",
                              self.orange2lcdNumber,
                              self.orange3lcdNumber,
                              "N/A",
                              self.red1lcdNumber,
                              "N/A",
                              self.red2lcdNumber,
                              self.red3lcdNumber,
                              "N/A",
                              self.yellow1lcdNumber,
                              self.yellow2lcdNumber,
                              "N/A",
                              self.yellow3lcdNumber,
                              "N/A",
                              self.green1lcdNumber,
                              self.green2lcdNumber,
                              "N/A",
                              self.green3lcdNumber,
                              "N/A",
                              "N/A",
                              self.dBlue1lcdNumber,
                              "N/A",
                              self.dBlue2lcdNumber
                              ]


        gameEnded = False
        chanceCounter = 0
        randomList = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
        random.shuffle(randomList)
        currentPlayer = playerList[0]
        self.currentPlayerLabel.setText(playerNames[0])

        if currentPlayer.inJail:
            self.inJailGroupBox.show()
            self.GOOJFCpushButton.clicked.connect(self.GOOJFCpressed(currentPlayer))
    

    def GOOJFCpressed(self, currentPlayer):
        if currentPlayer.GOOJFC:
            self.transactionLabel.setText(f"{currentPlayer.name} used their get out of jail free card.")
            currentPlayer.leaveJail(self)


        

