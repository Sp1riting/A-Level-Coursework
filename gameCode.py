import random
import sys
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap
import main as main
import Classes.newPlayer as Players
import Classes.card as Cards
from GameStart import board as board

class GameWindow(QDialog):
    def __init__(self, username, startingBalance, moneyFromGo, numberOfPlayers, fastBankruptcy, rentFromJail, playerNames):
        super(GameWindow, self).__init__()
        loadUi('C:\\Users\\willj\\OneDrive\\Documents\\Y13\\coursework\\UI\\game.ui', self)
        self.boardImageLabel.setPixmap(QPixmap("C:\\Users\\willj\\OneDrive\\Documents\\Y13\\coursework\\gameBoard.png"))

        self.chanceCardTextBrowser.hide()
        self.endTurnButton.hide()
        self.bankruptButton.hide()
        self.playTurnButton.hide()

        self.dice1outline.hide()
        self.dice1dot1.hide()
        self.dice1dot2.hide()
        self.dice1dot3.hide()
        self.dice1dot4.hide()
        self.dice1dot5.hide()
        self.dice1dot6.hide()
        self.dice1dot7.hide()

        self.dice2outline.hide()
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
        self.displayLabel2.setText("")
        self.transactionLabel.setText("")
        self.currentPlayerLabel.setText("")

        playerList = []

        if numberOfPlayers >= 1:

            self.player1NameLabel.setText(playerNames[0])
            self.player1BalanceLabel.setText(f"£{startingBalance}")
            player1 = Players.Player(1, playerNames[0], startingBalance, self.player1token, "a80000", self.player1NameLabel, self.player1BalanceLabel)
            playerList.append(player1)
        else:
            self.player1NameLabel.hide()
            self.player1BalanceLabel.hide()
        
        if numberOfPlayers >= 2:
            self.player2NameLabel.setText(playerNames[1])
            self.player2BalanceLabel.setText(f"£{startingBalance}")
            player2 = Players.Player(2, playerNames[1], startingBalance, self.player2token, "73ba23", self.player2NameLabel, self.player2BalanceLabel)
            playerList.append(player2)
        else:
            self.player2NameLabel.hide()
            self.player2BalanceLabel.hide()

        if numberOfPlayers >= 3:
            self.player3NameLabel.setText(playerNames[2])
            self.player3BalanceLabel.setText(f"£{startingBalance}")
            player3 = Players.Player(3, playerNames[2], startingBalance, self.player3token, "003eeb", self.player3NameLabel, self.player3BalanceLabel)
            playerList.append(player3)
        else:
            self.player3NameLabel.hide()
            self.player3BalanceLabel.hide()

        if numberOfPlayers >= 4:
            self.player4NameLabel.setText(playerNames[3])
            self.player4BalanceLabel.setText(f"£{startingBalance}")
            player4 = Players.Player(4, playerNames[3], startingBalance, self.player4token, "ffb300", self.player4NameLabel, self.player4BalanceLabel)
            playerList.append(player4)
        else:
            self.player4NameLabel.hide()
            self.player4BalanceLabel.hide()

        if numberOfPlayers >= 5:
            self.player5NameLabel.setText(playerNames[4])
            self.player5BalanceLabel.setText(f"£{startingBalance}")
            player5 = Players.Player(5, playerNames[4], startingBalance, self.player5token, "00d6e1", self.player5NameLabel, self.player5BalanceLabel)
            playerList.append(player5)
        else:
            self.player5NameLabel.hide()
            self.player5BalanceLabel.hide()

        if numberOfPlayers >= 6:
            self.player6NameLabel.setText(playerNames[5])
            self.player6BalanceLabel.setText(f"£{startingBalance}")
            player6 = Players.Player(6, playerNames[5], startingBalance, self.player6token, "6a533f", self.player6NameLabel, self.player6BalanceLabel)
            playerList.append(player6)
        else:
            self.player6NameLabel.hide()
            self.player6BalanceLabel.hide()

        if numberOfPlayers >= 7:
            self.player7NameLabel.setText(playerNames[6])
            self.player7BalanceLabel.setText(f"£{startingBalance}")
            player7 = Players.Player(7, playerNames[6], startingBalance, self.player7token, "ad17cb", self.player7NameLabel, self.player7BalanceLabel)
            playerList.append(player7)
        else:
            self.player7NameLabel.hide()
            self.player7BalanceLabel.hide()

        if numberOfPlayers >= 8:
            self.player8NameLabel.setText(playerNames[7])
            self.player8BalanceLabel.setText(f"£{startingBalance}")
            player8 = Players.Player(8, playerNames[7], startingBalance, self.player8token, "000000", self.player8NameLabel, self.player8BalanceLabel)
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

        for i in range (0, len(mortgageIndicators)):
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

        for i in range (0, len(ownershipIndicators)):
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
        self.playTurnButton.setEnabled(True)

        if currentPlayer.inJail and currentPlayer.turnsInJail >= 3:
            currentPlayer.leaveJail(self)

        elif currentPlayer.inJail:
            self.inJailGroupBox.show()
            self.playTurnButton.setEnabled(False)
            self.GOOJFCpushButton.clicked.connect(lambda:self.GOOJFCpressed(currentPlayer))
            self.payBailPushButton.clicked.connect(lambda:self.payBailPressed(currentPlayer, playerList, fastBankruptcy, houseIndicators, mortgageIndicators, ownershipIndicators))
            self.rollDoublePushButton.clicked.connect(lambda:self.rollDoublePressed(currentPlayer))
        
        else:
            self.playTurnButton.show()
            self.playTurnButton.clicked.connect(lambda:self.playTurnPressed(currentPlayer, playerList, fastBankruptcy, randomList, moneyFromGo, rentFromJail, chanceCounter, houseIndicators, mortgageIndicators, ownershipIndicators))
            
            self.travelSquarePurchaseButton.clicked.connect(lambda:self.purchaseTravelSquare(currentPlayer, self.travelSquareNameLabel, board, houseIndicators, mortgageIndicators, ownershipIndicators, playerList, fastBankruptcy))
            self.travelSquareNoPurchaseButton.clicked.connect(self.noPurchaseTravelSquare)
            self.utilityPurchaseButton.clicked.connect(lambda:self.purchaseUtility(currentPlayer, self.utilityNameLabel, board, houseIndicators, mortgageIndicators, ownershipIndicators, playerList, fastBankruptcy))
            self.utilityNoPurchaseButton.clicked.connect(self.noPurchaseUtility)
            self.normalCardPurchaseButton.clicked.connect(lambda:self.purchaseNormalCard(currentPlayer, self.normalCardNameLabel, board, houseIndicators, mortgageIndicators, ownershipIndicators, playerList, fastBankruptcy))
            self.normalCardNoPurchaseButton.clicked.connect(self.noPurchaseNormalCard)
        
        self.endTurnButton.clicked.connect(lambda:self.endTurnPressed(currentPlayer, playerList))


    def purchaseTravelSquare(self, currentPlayer, cardNameLabel, board, houseIndicators, mortgageIndicators, ownershipIndicators, playerList, fastBankruptcy):
        card = Cards.locateCard(cardNameLabel.text(), board)
        Cards.card.purchaseCard(self, currentPlayer, houseIndicators, mortgageIndicators, ownershipIndicators, playerList, fastBankruptcy)
        self.travelSquareFrame.hide()

    def noPurchaseTravelSquare(self):
        self.travelSquareFrame.hide()

    def purchaseUtility(self, currentPlayer, cardNameLabel, board, houseIndicators, mortgageIndicators, ownershipIndicators, playerList, fastBankruptcy):
        card = Cards.locateCard(cardNameLabel.text(), board)
        Cards.card.purchaseCard(self, currentPlayer, houseIndicators, mortgageIndicators, ownershipIndicators, playerList, fastBankruptcy)
        self.utilityFrame.hide()

    def noPurchaseUtility(self):
        self.utilityFrame.hide()

    def purchaseNormalCard(self, currentPlayer, cardNameLabel, board, houseIndicators, mortgageIndicators, ownershipIndicators, playerList, fastBankruptcy):
        card = Cards.locateCard(cardNameLabel.text(), board)
        Cards.card.purchaseCard(self, currentPlayer, houseIndicators, mortgageIndicators, ownershipIndicators, playerList, fastBankruptcy)
        self.normalCardFrame.hide()

    def noPurchaseNormalCard(self):
        self.normalCardFrame.hide()

    
    def playTurnPressed(self, currentPlayer, playerList, fastBankruptcy, randomList, moneyFromGo, rentFromJail, chanceCounter, houseIndicators, mortgageIndicators, ownershipIndicators):
        self.playTurnButton.setEnabled(False)
        diceRoll = currentPlayer.rollDice(self)
        currentPlayer.movePlayer(self, diceRoll)
        chanceCounter = currentPlayer.checkPosition(self, board, playerList, diceRoll, chanceCounter, randomList, moneyFromGo, fastBankruptcy, rentFromJail, houseIndicators, mortgageIndicators, ownershipIndicators)
        if currentPlayer.doublesCount > 0:
            self.playTurnButton.setEnabled(True)
        else:
            self.playTurnButton.setEnabled(False)
            self.endTurnButton.show()
            
    def endTurnPressed(self, currentPlayer, playerList):
        currentPlayer = playerList[(playerList.find(currentPlayer) + 1) % len(playerList)]
        self.currentPlayerLabel = currentPlayer.name
        self.displayLabel.setText(f"{currentPlayer.name}'s turn has now started.")
        self.endTurnButton.hide()

    def GOOJFCpressed(self, currentPlayer):
        if currentPlayer.GOOJFC:
            self.transactionLabel.setText(f"{currentPlayer.name} used their get out of jail free card.")
            currentPlayer.leaveJail(self)
            currentPlayer.GOOJFC = False
            self.playTurnButton.setEnabled(True)
        else:
            self.inJailMessageLabel.setText("You do not have a get out of jail free card.")
        self.endTurnButton.show()
    
    def payBailPressed(self, currentPlayer, playerList, fastBankruptcy, houseIndicators, mortgageIndicators, ownershipIndicators):
        if currentPlayer.balance >= 50:
            self.displayLabel2.setText(f"{currentPlayer.name} paid £50 to get out of jail.")
            currentPlayer.reduceBalance(self, 50, playerList, fastBankruptcy, houseIndicators, mortgageIndicators, ownershipIndicators)
            currentPlayer.leaveJail(self)
            self.playTurnButton.setEnabled(True)
            if currentPlayer.balance >= 0:
                self.endTurnButton.show()
        else:
            self.inJailMessageLabel.setText("You don't have enough money for bail.")
            self.inJailGroupBox.hide()
            self.endTurnButton.show()
        
            
    def rollDoublePressed(self, currentPlayer):
        self.inJailGroupBox.hide()
        currentPlayer.rollDice(self)
        if currentPlayer.doublesCount == 1:
            currentPlayer.leaveJail(self)
            currentPlayer.doublesCount = 0
            self.displayLabel.setText(f"{currentPlayer.name} has rolled a doubles, and was released from jail.")
            self.playTurnButton.setEnabled(True)
        else:
            currentPlayer.turnsInJail += 1
            self.displayLabel.setText(f"{currentPlayer.name} failed to roll a double, and have now spent {currentPlayer.turnsInJail} days in jail.")


        
