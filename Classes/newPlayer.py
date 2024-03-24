import random
import Classes.card as Cards
import chance as chance
from GameStart import board as board
from PyQt5.QtWidgets import *
from PyQt5 import QtTest

class Player:

    currentPos = 0
    doublesCount = 0
    travelSquaresOwned = 0
    utilitiesOwned = 0
    housesOwned = 0
    ownedCards = []
    turnsInJail = 0
    inJail = False
    bankrupt = False
    GOOJFC = False
    
    def __init__(self, playerID, name, balance, token, colour, nameLabel, balanceLabel):
        self.playerID = playerID
        self.name = name
        self.balance = balance
        self.token = token
        self.colour = colour
        self.nameLabel = nameLabel
        self.balanceLabel = balanceLabel


    def rollDice(self, GameWindow):
        GameWindow.dice1outline.show()
        GameWindow.dice2outline.show()

        dice1 = random.randint(1, 6)

        if dice1 == 1:
            GameWindow.dice1dot4.show()
        elif dice1 == 2:
            GameWindow.dice1dot1.show()
            GameWindow.dice1dot7.show()
        elif dice1 == 3:
            GameWindow.dice1dot1.show()
            GameWindow.dice1dot4.show()
            GameWindow.dice1dot7.show()
        elif dice1 == 4:
            GameWindow.dice1dot1.show()
            GameWindow.dice1dot2.show()
            GameWindow.dice1dot6.show()
            GameWindow.dice1dot7.show()
        elif dice1 == 5:
            GameWindow.dice1dot1.show()
            GameWindow.dice1dot2.show()
            GameWindow.dice1dot4.show()
            GameWindow.dice1dot6.show()
            GameWindow.dice1dot7.show()
        elif dice1 == 6:
            GameWindow.dice1dot1.show()
            GameWindow.dice1dot2.show()
            GameWindow.dice1dot3.show()
            GameWindow.dice1dot5.show()
            GameWindow.dice1dot6.show()
            GameWindow.dice1dot7.show()

        dice2 = random.randint(1, 6)

        if dice2 == 1:
            GameWindow.dice2dot4.show()
        elif dice2 == 2:
            GameWindow.dice2dot1.show()
            GameWindow.dice2dot7.show()
        elif dice2 == 3:
            GameWindow.dice2dot1.show()
            GameWindow.dice2dot4.show()
            GameWindow.dice2dot7.show()
        elif dice2 == 4:
            GameWindow.dice2dot1.show()
            GameWindow.dice2dot2.show()
            GameWindow.dice2dot6.show()
            GameWindow.dice2dot7.show()
        elif dice2 == 5:
            GameWindow.dice2dot1.show()
            GameWindow.dice2dot2.show()
            GameWindow.dice2dot4.show()
            GameWindow.dice2dot6.show()
            GameWindow.dice2dot7.show()
        elif dice2 == 6:
            GameWindow.dice2dot1.show()
            GameWindow.dice2dot2.show()
            GameWindow.dice2dot3.show()
            GameWindow.dice2dot5.show()
            GameWindow.dice2dot6.show()
            GameWindow.dice2dot7.show()
        

        roll = dice1 + dice2
        GameWindow.displayLabel.setText(f"{self.name} threw a {dice1} and a {dice2}, giving a roll of {roll}.")
        

        if dice1 == dice2:
            self.doublesCount += 1
            if self.doublesCount == 3:
                GameWindow.displayLabel2.setText(f"{self.name} rolled three doubles, and is going to jail.")
                self.sendToJail(GameWindow)
                QtTest.QTest.qWait(2000)
                return roll
            GameWindow.displayLabel2.setText(f"{self.name} rolled a double, and will play again.")
            QtTest.QTest.qWait(2000)
        else:
            self.doublesCount = 0
            QtTest.QTest.qWait(2000)
        return roll


    def movePlayer(self, GameWindow, amount):
        self.currentPos += amount


    def checkPosition(self, GameWindow, board, playerList, roll, chanceCounter, randomList, moneyFromGo, fastBankruptcy, rentFromJail, houseIndicators, mortgageIndicators, ownershipIndicators):

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

        if self.currentPos >= 40:
            GameWindow.displayLabel2.setText(f"{self.name} passed Go, and collects £{moneyFromGo}.")
            self.addBalance(GameWindow, moneyFromGo)
            self.currentPos = self.currentPos % 40
        boardProperty = board[self.currentPos]

        if boardProperty.cardName == 'Jail' and not self.inJail:
                GameWindow.displayLabel.setText(f"{self.name} is visiting jail.")
        
        elif boardProperty.cardName == 'Jail' and self.inJail:
                GameWindow.displayLabel.setText(f"{self.name} is in jail.")

        elif boardProperty.cardName == 'Luxury Tax':
            GameWindow.displayLabel.setText(f"{self.name} landed on Luxury Tax and has been fined £75.")
            self.reduceBalance(self, GameWindow, 75, playerList, fastBankruptcy, True, houseIndicators, mortgageIndicators, ownershipIndicators)

        elif boardProperty.cardName == 'Income Tax':
            GameWindow.displayLabel.setText(f"{self.name} landed on Income Tax and has been fined £200.")
            self.reduceBalance(self, GameWindow, 200, playerList, fastBankruptcy, True, houseIndicators, mortgageIndicators, ownershipIndicators)

        elif boardProperty.cardName == 'Go To Jail':
            GameWindow.displayLabel.setText(f"{self.name} landed on Go to Jail and has been arrested!")
            self.sendToJail(GameWindow)
        
        elif boardProperty.cardName == 'Free Parking':
            GameWindow.displayLabel.setText(f"{self.name} landed on Free Parking, and is chilling for this turn.")

        elif boardProperty.cardName == 'Go':
            GameWindow.displayLabel.setText(f"{self.name} landed on Go, and is chilling for this turn.")
        
        elif boardProperty.cardName == 'Chance':
            GameWindow.displayLabel.setText(f"{self.name} landed on Chance, and will draw a card.")
            chanceCounter = chance.drawChance(self, GameWindow, board, playerList, roll, chanceCounter, randomList, moneyFromGo, fastBankruptcy, rentFromJail, houseIndicators, mortgageIndicators, ownershipIndicators)

        else:
            if boardProperty.mortgaged:
                GameWindow.displayLabel.setText(f"{self.name} landed on {boardProperty.name}, a mortgaged property.")

            elif boardProperty.ownerID != "0":
                if boardProperty.ownerID == str(self.playerID):
                    GameWindow.displayLabel.setText(f"{self.name} landed on {boardProperty.cardName}, a property they own.")
                else:
                    GameWindow.displayLabel.setText(f"{self.name} landed on {boardProperty.cardName}, a property owned by player{boardProperty.ownerID}")
                    self.payRent(GameWindow, boardProperty, playerList, roll, False, houseIndicators, mortgageIndicators, ownershipIndicators)

            else:
                GameWindow.displayLabel.setText(f"{self.name} landed on {boardProperty.cardName}")
                if boardProperty.cardSet == "Travel Square":
                    GameWindow.travelSquareFrame.show()
                elif boardProperty.cardSet == "Utility":
                    GameWindow.utilityFrame.show()
                else:
                    GameWindow.normalCardFrame.show()
        return chanceCounter


    def advanceToSquare(self, GameWindow, board, playerList, diceRoll, isDoubled, i, houseIndicators, mortgageIndicators, ownershipIndicators):
        self.currentPos = i
        if board[i].mortgaged:
            GameWindow.displayLabel.setText(f"{self.name} landed on {board[i].cardName}, a mortgaged property.")
        elif board[i].ownerID != "0":
            GameWindow.displayLabel.setText(f"{self.name} landed on {board[i].cardName}")
            self.payRent(GameWindow, board[i], playerList, diceRoll, isDoubled, houseIndicators, mortgageIndicators, ownershipIndicators)
        elif board[i].cardSet == "Travel Square":
            GameWindow.travelSquareFrame.show()
        elif board[i].cardSet == "Utility":
            GameWindow.utilityFrame.show()
        else:
            GameWindow.normalCardFrame.show()


    def leaveJail(self, GameWindow):
        self.currentPos = 10
        self.turnsInJail = 0
        self.doublesCount = 0
        self.inJail = False
        GameWindow.displayLabel2.setText(f"{self.name} has been released from jail.")
        GameWindow.inJailGroupBox.hide()
    

    def sendToJail(self, GameWindow):
        self.currentPos = 10
        self.turnsInJail = 0
        self.doublesCount = 0
        self.inJail = True
        GameWindow.displayLabel2.setText(f"{self.name} has been sent to jail.")
        GameWindow.endTurnButton.show()
        GameWindow.endTurnButton.isEnabled = True
    

    def addBalance(self, GameWindow, amount):
        self.balance += amount
        GameWindow.transactionLabel.setText(f"£{amount} has been added to {self.name}")
        return self.balance


    def reduceBalance(self, GameWindow, amount, playerList, fastBankruptcy, nonRentPayment, houseIndicators, mortgageIndicators, ownershipIndicators):
        if self.balance < amount:
            if fastBankruptcy:
                self.bankruptPlayer(GameWindow, playerList, houseIndicators, mortgageIndicators, ownershipIndicators)
            else:
                GameWindow.bankruptButton.show()
                GameWindow.endTurnButton.hide()
        else:
            self.balance -= amount
            if nonRentPayment:
                self.balanceLabel.setText(f"£{self.balance}")
                GameWindow.transactionLabel.setText(f"£{amount} has been deducted from {self.name}.")
        return self.balance
    

    def checkBankruptcy(self, amount):
        worth = 0

        for card in self.ownedCards:
            if not card.mortgaged:
                worth += card.mortgageCost
            if card.housesBuilt != "N/A":
                worth += card.housesBuilt * card.houseCost

        if (self.balance + worth) < amount:
            return True
        else:
            return False
        
    def bankruptPlayer(self, GameWindow, playerList, houseIndicators, mortgageIndicators, ownershipIndicators):
        self.balance = 0
        self.travelSquaresOwned = 0
        self.bankrupt = True
        GameWindow.self.token.hide()
        self.balanceLabel.hide()
        font = self.nameLabel.font()
        font.setStrikeOut(True)
        self.nameLabel.setFont(font)

        if len(self.ownedCards) > 0:
            for card in self.cardsOwned:
                card.owner = "Bank"
                card.ownerID = "0"
                card.mortgaged = False
                card.housesBuilt = 0
                position = board.find(card)
                if not houseIndicators[position] == "N/A":
                    houseIndicators[position].value = 0
                    houseIndicators[position].hide()
                mortgageIndicators[position].hide()
                ownershipIndicators[position].hide()
                
        playerList.remove(self)
        GameWindow.displayLabel.setText(f"{self.name} is now bankrupt. It is game over for them!")
        GameWindow.displayLabel2.setText("")
