import random
import sys
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap
import main as main
import Classes.newPlayer as Players
import Classes.card as Cards
from GameStart import board as board
from endGameCode import EndGameWindow as endGameWindow 

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
            player1 = Players.Player(1, playerNames[0], startingBalance, self.player1token, "#a80000", self.player1NameLabel, self.player1BalanceLabel)
            if player1.ownedCards == None:
                player1.ownedCards = []
            playerList.append(player1)
        else:
            self.player1NameLabel.hide()
            self.player1BalanceLabel.hide()
            self.player1token.hide()
        
        if numberOfPlayers >= 2:
            self.player2NameLabel.setText(playerNames[1])
            self.player2BalanceLabel.setText(f"£{startingBalance}")
            player2 = Players.Player(2, playerNames[1], startingBalance, self.player2token, "#73ba23", self.player2NameLabel, self.player2BalanceLabel)
            if player2.ownedCards == None:
                player2.ownedCards = []
            playerList.append(player2)
        else:
            self.player2NameLabel.hide()
            self.player2BalanceLabel.hide()
            self.player2token.hide()

        if numberOfPlayers >= 3:
            self.player3NameLabel.setText(playerNames[2])
            self.player3BalanceLabel.setText(f"£{startingBalance}")
            player3 = Players.Player(3, playerNames[2], startingBalance, self.player3token, "#003eeb", self.player3NameLabel, self.player3BalanceLabel)
            if player3.ownedCards == None:
                player3.ownedCards = []
            playerList.append(player3)
        else:
            self.player3NameLabel.hide()
            self.player3BalanceLabel.hide()
            self.player3token.hide()

        if numberOfPlayers >= 4:
            self.player4NameLabel.setText(playerNames[3])
            self.player4BalanceLabel.setText(f"£{startingBalance}")
            player4 = Players.Player(4, playerNames[3], startingBalance, self.player4token, "#ffb300", self.player4NameLabel, self.player4BalanceLabel)
            if player4.ownedCards == None:
                player4.ownedCards = []
            playerList.append(player4)
        else:
            self.player4NameLabel.hide()
            self.player4BalanceLabel.hide()
            self.player4token.hide()

        if numberOfPlayers >= 5:
            self.player5NameLabel.setText(playerNames[4])
            self.player5BalanceLabel.setText(f"£{startingBalance}")
            player5 = Players.Player(5, playerNames[4], startingBalance, self.player5token, "#00d6e1", self.player5NameLabel, self.player5BalanceLabel)
            if player5.ownedCards == None:
                player5.ownedCards = []
            playerList.append(player5)
        else:
            self.player5NameLabel.hide()
            self.player5BalanceLabel.hide()
            self.player5token.hide()

        if numberOfPlayers >= 6:
            self.player6NameLabel.setText(playerNames[5])
            self.player6BalanceLabel.setText(f"£{startingBalance}")
            player6 = Players.Player(6, playerNames[5], startingBalance, self.player6token, "#6a533f", self.player6NameLabel, self.player6BalanceLabel)
            if player6.ownedCards == None:
                player6.ownedCards = []
            playerList.append(player6)
        else:
            self.player6NameLabel.hide()
            self.player6BalanceLabel.hide()
            self.player6token.hide()

        if numberOfPlayers >= 7:
            self.player7NameLabel.setText(playerNames[6])
            self.player7BalanceLabel.setText(f"£{startingBalance}")
            player7 = Players.Player(7, playerNames[6], startingBalance, self.player7token, "#ad17cb", self.player7NameLabel, self.player7BalanceLabel)
            if player7.ownedCards == None:
                player7.ownedCards = []
            playerList.append(player7)
        else:
            self.player7NameLabel.hide()
            self.player7BalanceLabel.hide()
            self.player7token.hide()

        if numberOfPlayers >= 8:
            self.player8NameLabel.setText(playerNames[7])
            self.player8BalanceLabel.setText(f"£{startingBalance}")
            player8 = Players.Player(8, playerNames[7], startingBalance, self.player8token, "#000000", self.player8NameLabel, self.player8BalanceLabel)
            if player8.ownedCards == None:
                player8.ownedCards = []
            playerList.append(player8)
        else:
            self.player8NameLabel.hide()
            self.player8BalanceLabel.hide()
            self.player8token.hide()

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

        gameValues = values(playerList[0], random.sample([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16], 17), rentFromJail)
        self.currentPlayerLabel.setText(playerNames[0])
        self.playTurnButton.show()

        self.playTurnButton.clicked.connect(lambda:self.playTurnPressed(gameValues, playerList, fastBankruptcy, moneyFromGo, rentFromJail, houseIndicators, mortgageIndicators, ownershipIndicators, username))
        
        self.travelSquarePurchaseButton.clicked.connect(lambda:self.purchaseTravelSquare(gameValues.currentPlayer, self.travelSquareNameLabel, board, houseIndicators, mortgageIndicators, ownershipIndicators, playerList, fastBankruptcy, gameValues))
        self.travelSquareNoPurchaseButton.clicked.connect(self.noPurchaseTravelSquare)
        self.utilityPurchaseButton.clicked.connect(lambda:self.purchaseUtility(gameValues.currentPlayer, self.utilityNameLabel, board, houseIndicators, mortgageIndicators, ownershipIndicators, playerList, fastBankruptcy, gameValues))
        self.utilityNoPurchaseButton.clicked.connect(self.noPurchaseUtility)
        self.normalCardPurchaseButton.clicked.connect(lambda:self.purchaseNormalCard(gameValues.currentPlayer, self.normalCardNameLabel, board, houseIndicators, mortgageIndicators, ownershipIndicators, playerList, fastBankruptcy, gameValues))
        self.normalCardNoPurchaseButton.clicked.connect(self.noPurchaseNormalCard)
        
        self.endTurnButton.clicked.connect(lambda:self.endTurnPressed(gameValues, playerList))
        self.bankruptButton.clicked.connect(lambda:self.bankruptPressed(gameValues, playerList, houseIndicators, mortgageIndicators, ownershipIndicators))
        self.housesButton.clicked.connect(lambda:self.housesMenu(gameValues, playerList, board, fastBankruptcy, houseIndicators, mortgageIndicators, ownershipIndicators))
        self.mortgageButton.clicked.connect(lambda:self.mortgageMenu(gameValues, playerList, board, fastBankruptcy, houseIndicators, mortgageIndicators, ownershipIndicators))

        self.unmortgageItemButton.clicked.connect(lambda:self.unmortgagePressed(board, gameValues, playerList, fastBankruptcy, houseIndicators, mortgageIndicators, ownershipIndicators))
        self.mortgageItemButton.clicked.connect(lambda:self.mortgagePressed(board, gameValues, houseIndicators, mortgageIndicators, ownershipIndicators))
        self.mortgageReturnButton.clicked.connect(self.returnMortgagePressed)

        self.buyHouseButton.clicked.connect(lambda:self.buyHousePressed(gameValues, playerList, fastBankruptcy, houseIndicators, mortgageIndicators, ownershipIndicators, board))
        self.sellHouseButton.clicked.connect(lambda:self.sellHousePressed(gameValues, houseIndicators, mortgageIndicators, ownershipIndicators, board))
        self.houseReturnButton.clicked.connect(self.houseReturnPressed)

        self.GOOJFCpushButton.clicked.connect(lambda:self.GOOJFCpressed(gameValues.currentPlayer))
        self.payBailPushButton.clicked.connect(lambda:self.payBailPressed(gameValues.currentPlayer, playerList, fastBankruptcy, houseIndicators, mortgageIndicators, ownershipIndicators, gameValues))
        self.rollDoublePushButton.clicked.connect(lambda:self.rollDoublePressed(gameValues))
    

    def mortgageMenu(self, gameValues, board):
        self.mortgageButton.setEnabled(False)
        self.housesButton.setEnabled(False)
        self.tradeButton.setEnabled(False)
        self.endTurnButton.setEnabled(False)
        self.bankruptButton.setEnabled(False)
        self.playTurnButton.setEnabled(False)
        self.unmortgageSelectionComboBox.clear()
        self.unmortgageSelectionComboBox.addItem("Select Property")
        self.mortgageSelectionComboBox.clear()
        self.mortgageSelectionComboBox.addItem("Select Property")
        self.mortgageGroupBox.show()
        if len(gameValues.currentPlayer.ownedCards) > 0:
            for card in gameValues.currentPlayer.ownedCards:
                currentCard =  Cards.locateCard(card, board)
                if currentCard.mortgaged == True:
                    self.unmortgageSelectionComboBox.addItem(f"{currentCard.cardName}")
                else:
                    self.mortgageSelectionComboBox.addItem(f"{currentCard.cardName}")


    def unmortgagePressed(self, board, gameValues, playerList, fastBankruptcy, houseIndicators, mortgageIndicators, ownershipIndicators):
        cardString = self.unmortgageSelectionComboBox.currentText()
        if cardString == "Select Property":
            self.mortgageLabel.setText("Please select a property")
        else:
            currentCard = Cards.locateCard(cardString, board)
            Cards.Card.unmortgage(currentCard, self, gameValues, playerList, fastBankruptcy, houseIndicators, mortgageIndicators, ownershipIndicators, board)
    
    def mortgagePressed(self, board, gameValues, houseIndicators, mortgageIndicators, ownershipIndicators):
        cardString = self.mortgageSelectionComboBox.currentText()
        if cardString == "Select Property":
            self.mortgageLabel.setText("Please select a property")
        else:
            currentCard = Cards.locateCard(cardString, board)
            Cards.Card.mortgage(currentCard, self, gameValues.currentPlayer, gameValues, houseIndicators, mortgageIndicators, ownershipIndicators, board)

    def returnMortgagePressed(self):
        self.mortgageGroupBox.hide()
        self.mortgageButton.setEnabled(True)
        self.housesButton.setEnabled(True)
        self.tradeButton.setEnabled(True)
        self.endTurnButton.setEnabled(True)
        self.bankruptButton.setEnabled(True)
        self.playTurnButton.setEnabled(True)
        self.buyHouseSelectionComboBox.clear()
        self.sellHouseSelectionComboBox.clear()

    def housesMenu(self, gameValues, board):
        self.mortgageButton.setEnabled(False)
        self.housesButton.setEnabled(False)
        self.tradeButton.setEnabled(False)
        self.endTurnButton.setEnabled(False)
        self.bankruptButton.setEnabled(False)
        self.playTurnButton.setEnabled(False)
        self.buyHouseSelectionComboBox.clear()
        self.buyHouseSelectionComboBox.addItem("Select Property")
        self.sellHouseSelectionComboBox.clear()
        self.sellHouseSelectionComboBox.addItem("Select Property")
        self.housesGroupBox.show()
        if len(gameValues.currentPlayer.ownedCards) > 0:
            for card in gameValues.currentPlayer.ownedCards:
                currentCard =  Cards.locateCard(card, board)
                if currentCard.cardSet != "Travel Square" and currentCard.cardSet != "Utility":
                    if currentCard.housesBuilt < 5:
                        self.buyHouseSelectionComboBox.addItem(f"{currentCard.cardName}")
                    if currentCard.housesBuilt > 0:
                        self.sellHouseSelectionComboBox.addItem(f"{currentCard.cardName}")

    def buyHousePressed(self, gameValues, playerList, fastBankruptcy, houseIndicators, mortgageIndicators, ownershipIndicators, board):
        cardString = self.buyHouseSelectionComboBox.currentText()
        if cardString == "Select Property":
            self.housesLabel.setText("Please select a property")
        else:
            currentCard = Cards.locateCard(cardString, board)
            Cards.Card.purchaseHouse(currentCard, self, gameValues, playerList, fastBankruptcy, houseIndicators, mortgageIndicators, ownershipIndicators, board)

    def sellHousePressed(self, gameValues, houseIndicators, mortgageIndicators, ownershipIndicators, board):
        cardString = self.sellHouseSelectionComboBox.currentText()
        if cardString == "Select Property":
            self.housesLabel.setText("Please select a property")
        else:
            currentCard = Cards.locateCard(cardString, board)
            Cards.Card.sellHouse(currentCard, self, gameValues.currentPlayer, gameValues, houseIndicators, mortgageIndicators, ownershipIndicators, board)

    def houseReturnPressed(self):
        self.housesGroupBox.hide()
        self.mortgageButton.setEnabled(True)
        self.housesButton.setEnabled(True)
        self.tradeButton.setEnabled(True)
        self.endTurnButton.setEnabled(True)
        self.bankruptButton.setEnabled(True)
        self.playTurnButton.setEnabled(True)

    def purchaseTravelSquare(self, currentPlayer, cardNameLabel, board, houseIndicators, mortgageIndicators, ownershipIndicators, playerList, fastBankruptcy, gameValues):
        gameValues.currentPlayer, self.travelSquareNameLabel, board, houseIndicators, mortgageIndicators, ownershipIndicators, playerList, fastBankruptcy, gameValues
        card = Cards.locateCard(cardNameLabel.text(), board)
        Cards.Card.purchaseCard(card, self, currentPlayer, houseIndicators, mortgageIndicators, ownershipIndicators, playerList, fastBankruptcy, gameValues, board)
        self.travelSquareFrame.hide()
        self.endTurnButton.setEnabled(True)
        self.bankruptButton.setEnabled(True)

    def noPurchaseTravelSquare(self):
        self.travelSquareFrame.hide()
        self.endTurnButton.setEnabled(True)
        self.bankruptButton.setEnabled(True)

    def purchaseUtility(self, currentPlayer, cardNameLabel, board, houseIndicators, mortgageIndicators, ownershipIndicators, playerList, fastBankruptcy, gameValues):
        card = Cards.locateCard(cardNameLabel.text(), board)
        Cards.Card.purchaseCard(card, self, currentPlayer, houseIndicators, mortgageIndicators, ownershipIndicators, playerList, fastBankruptcy, gameValues, board)
        self.utilityFrame.hide()
        self.endTurnButton.setEnabled(True)
        self.bankruptButton.setEnabled(True)

    def noPurchaseUtility(self):
        self.utilityFrame.hide()
        self.endTurnButton.setEnabled(True)
        self.bankruptButton.setEnabled(True)

    def purchaseNormalCard(self, currentPlayer, cardNameLabel, board, houseIndicators, mortgageIndicators, ownershipIndicators, playerList, fastBankruptcy, gameValues):
        card = Cards.locateCard(cardNameLabel.text(), board)
        Cards.Card.purchaseCard(card, self, currentPlayer, houseIndicators, mortgageIndicators, ownershipIndicators, playerList, fastBankruptcy, gameValues, board)
        self.normalCardFrame.hide()
        self.endTurnButton.setEnabled(True)
        self.bankruptButton.setEnabled(True)

    def noPurchaseNormalCard(self):
        self.normalCardFrame.hide()
        self.endTurnButton.setEnabled(True)
        self.bankruptButton.setEnabled(True)

    
    def playTurnPressed(self, gameValues, playerList, fastBankruptcy, moneyFromGo, rentFromJail, houseIndicators, mortgageIndicators, ownershipIndicators, username):
        self.mortgageButton.setEnabled(False)
        self.tradeButton.setEnabled(False)
        self.housesButton.setEnabled(False)
        if gameValues.gameEnded:
            self._new_window = endGameWindow(gameValues, playerList, username)
            self.close()
            self._new_window.show()
        else:
            if gameValues.currentPlayer.inJail:
                if gameValues.currentPlayer.turnsInJail >= 3:
                    gameValues.currentPlayer.leaveJail(self)
                else:
                    self.inJailMessageLabel.setText("")
                    self.inJailGroupBox.show()
                    self.playTurnButton.setEnabled(False)
                    return
            self.mortgageButton.setEnabled(False)
            self.housesButton.setEnabled(False)
            self.tradeButton.setEnabled(False)
            self.displayLabel2.setText("")
            self.chanceCardTextBrowser.hide()
            self.playTurnButton.setEnabled(False)
            diceRoll = gameValues.currentPlayer.rollDice(self, gameValues)
            if gameValues.currentPlayer.doublesCount > 0:
                gameValues.doublesRolled += 1
            gameValues.currentPlayer.movePlayer(self, diceRoll)
            gameValues.currentPlayer.checkPosition(self, board, playerList, diceRoll, gameValues, moneyFromGo, fastBankruptcy, rentFromJail, houseIndicators, mortgageIndicators, ownershipIndicators)
            if fastBankruptcy and gameValues.currentPlayer.balance < 0:
                tempIndex = (playerList.index(gameValues.currentPlayer)) % len(playerList)
                gameValues.currentPlayer.bankruptPlayer(self, playerList, houseIndicators, mortgageIndicators, ownershipIndicators, gameValues)
                gameValues.currentPlayer = playerList[tempIndex]
                self.currentPlayerLabel.setText(gameValues.currentPlayer.name)
                self.displayLabel.setText(f"{gameValues.currentPlayer.name}'s turn has now started.")
                self.bankruptButton.hide()
                self.endTurnButton.hide()
                self.playTurnButton.setEnabled(True)
                return
            
            elif gameValues.currentPlayer.balance < 0:
                self.playTurnButton.setEnabled(False)
                self.endTurnButton.hide()
                self.bankruptButton.show()
            elif gameValues.currentPlayer.doublesCount > 0:
                self.playTurnButton.setEnabled(True)
            elif gameValues.currentPlayer.balance >= 0:
                self.playTurnButton.setEnabled(False)
                self.endTurnButton.show()
            
    def endTurnPressed(self, gameValues, playerList):
        self.mortgageButton.setEnabled(True)
        self.housesButton.setEnabled(True)
        self.tradeButton.setEnabled(True)
        self.displayLabel2.setText("")
        self.chanceCardTextBrowser.hide()
        gameValues.currentPlayer = playerList[(playerList.index(gameValues.currentPlayer) + 1) % len(playerList)]
        self.currentPlayerLabel.setText(gameValues.currentPlayer.name)
        self.displayLabel.setText(f"{gameValues.currentPlayer.name}'s turn has now started.")
        self.endTurnButton.hide()
        self.playTurnButton.setEnabled(True)

    def bankruptPressed(self, gameValues, playerList, houseIndicators, mortgageIndicators, ownershipIndicators):
        self.mortgageButton.setEnabled(True)
        self.housesButton.setEnabled(True)
        self.tradeButton.setEnabled(True)
        tempIndex = (playerList.index(gameValues.currentPlayer)) % len(playerList)
        gameValues.currentPlayer.bankruptPlayer(self, playerList, houseIndicators, mortgageIndicators, ownershipIndicators, gameValues)
        gameValues.currentPlayer = playerList[tempIndex]
        self.currentPlayerLabel.setText(gameValues.currentPlayer.name)
        self.displayLabel.setText(f"{gameValues.currentPlayer.name}'s turn has now started.")
        self.bankruptButton.hide()
        self.endTurnButton.hide()
        self.playTurnButton.setEnabled(True)


    def GOOJFCpressed(self, currentPlayer):
        if currentPlayer.GOOJFC:
            self.transactionLabel.setText(f"{currentPlayer.name} used their get out of jail free card.")
            currentPlayer.leaveJail(self)
            currentPlayer.GOOJFC = False
            self.playTurnButton.setEnabled(True)
            self.endTurnButton.show()
        else:
            self.inJailMessageLabel.setText("You do not have a get out of jail free card.")
        
    
    def payBailPressed(self, currentPlayer, playerList, fastBankruptcy, houseIndicators, mortgageIndicators, ownershipIndicators, gameValues):
        if currentPlayer.balance >= 50:
            self.displayLabel2.setText(f"{currentPlayer.name} paid £50 to get out of jail.")
            currentPlayer.reduceBalance(self, 50, playerList, fastBankruptcy, True, houseIndicators, mortgageIndicators, ownershipIndicators, gameValues)
            currentPlayer.leaveJail(self)
            self.playTurnButton.setEnabled(True)
            if currentPlayer.balance >= 0:
                self.endTurnButton.show()
                self.playTurnButton.setEnabled(False)
        else:
            self.inJailMessageLabel.setText("You don't have enough money for bail.")

            
    def rollDoublePressed(self, gameValues):
        self.inJailGroupBox.hide()
        gameValues.currentPlayer.rollDice(self, gameValues)
        


        
class values:
    doublesRolled = 0; propertiesPurchased = 0; moneyEarned = 0; rentPaid = 0; passedGo = 0
    gameEnded = False
    chanceCounter = 0
    cardPositions = [1010, 1010,
                    900, 1010,
                    820, 1010,
                    730, 1010,
                    650, 1010,
                    560, 1010,
                    480, 1010,
                    390, 1010,
                    310, 1010,
                    220, 1010,
                    100, 960,
                    100, 900,
                    100, 810,
                    100, 730,
                    100, 640,
                    100, 560,
                    100, 470,
                    100, 380,
                    100, 300,
                    100, 210,
                    100, 90,
                    220, 100,
                    310, 100,
                    390, 100,
                    480, 100,
                    560, 100,
                    650, 100,
                    730, 100,
                    820, 100,
                    900, 100,
                    990, 70,
                    1010, 220,
                    1010, 300,
                    1010, 390,
                    1010, 470,
                    1010, 550,
                    1010, 640,
                    1010, 730,
                    1010, 810,
                    1010, 900
                    ]
    def __init__(self, currentPlayer, randomList, rentFromJail):
        self.currentPlayer = currentPlayer
        self.randomList = randomList
        self.rentFromJail = rentFromJail

