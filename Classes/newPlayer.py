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
    ownedCards = None
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


    def rollDice(self, GameWindow, gameValues):
        GameWindow.dice1outline.show()
        GameWindow.dice2outline.show()
        
        GameWindow.dice1dot1.hide()
        GameWindow.dice1dot2.hide()
        GameWindow.dice1dot3.hide()
        GameWindow.dice1dot4.hide()
        GameWindow.dice1dot5.hide()
        GameWindow.dice1dot6.hide()
        GameWindow.dice1dot7.hide()

        GameWindow.dice2dot1.hide()
        GameWindow.dice2dot2.hide()
        GameWindow.dice2dot3.hide()
        GameWindow.dice2dot4.hide()
        GameWindow.dice2dot5.hide()
        GameWindow.dice2dot6.hide()
        GameWindow.dice2dot7.hide()

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
        
        if self.inJail:
            if dice1 == dice2:
                self.leaveJail(GameWindow)
                self.doublesCount = 0
                GameWindow.displayLabel.setText(f"{self.name} has rolled a double, and was released from jail.")
                GameWindow.playTurnButton.setEnabled(True)
            else:
                self.turnsInJail += 1
                GameWindow.displayLabel.setText(f"{self.name} failed to roll a double, and have now spent {self.turnsInJail} days in jail.")
                GameWindow.endTurnButton.show()

        elif dice1 == dice2:
            self.doublesCount += 1
            if self.doublesCount == 3:
                GameWindow.displayLabel2.setText(f"{self.name} rolled three doubles, and is going to jail.")
                self.sendToJail(GameWindow, gameValues)
                QtTest.QTest.qWait(1000)
                return roll
            GameWindow.displayLabel2.setText(f"{self.name} rolled a double, and will play again.")
            QtTest.QTest.qWait(1000)
        else:
            self.doublesCount = 0
            QtTest.QTest.qWait(1000)
        return roll


    def movePlayer(self, GameWindow, amount):
        self.currentPos += amount


    def checkPosition(self, GameWindow, board, playerList, roll, gameValues, moneyFromGo, fastBankruptcy, rentFromJail, houseIndicators, mortgageIndicators, ownershipIndicators):

        GameWindow.dice1outline.hide()
        GameWindow.dice1dot1.hide()
        GameWindow.dice1dot2.hide()
        GameWindow.dice1dot3.hide()
        GameWindow.dice1dot4.hide()
        GameWindow.dice1dot5.hide()
        GameWindow.dice1dot6.hide()
        GameWindow.dice1dot7.hide()

        GameWindow.dice2outline.hide()
        GameWindow.dice2dot1.hide()
        GameWindow.dice2dot2.hide()
        GameWindow.dice2dot3.hide()
        GameWindow.dice2dot4.hide()
        GameWindow.dice2dot5.hide()
        GameWindow.dice2dot6.hide()
        GameWindow.dice2dot7.hide()

        if self.currentPos >= 40:
            GameWindow.displayLabel2.setText(f"{self.name} passed Go, and collects £{moneyFromGo}.")
            gameValues.passedGo += 1
            self.addBalance(GameWindow, moneyFromGo, gameValues)
            self.currentPos = self.currentPos % 40
        boardProperty = board[self.currentPos]
        self.token.move(gameValues.cardPositions[self.currentPos * 2], gameValues.cardPositions[self.currentPos * 2 + 1])

        if boardProperty.cardName == 'Jail' and not self.inJail:
                GameWindow.displayLabel.setText(f"{self.name} is visiting jail.")
        
        elif boardProperty.cardName == 'Jail' and self.inJail:
                GameWindow.displayLabel.setText(f"{self.name} is in jail.")
                

        elif boardProperty.cardName == 'Luxury Tax':
            GameWindow.displayLabel.setText(f"{self.name} landed on Luxury Tax and has been fined £75.")
            self.reduceBalance(GameWindow, 75, playerList, fastBankruptcy, True, houseIndicators, mortgageIndicators, ownershipIndicators, gameValues)

        elif boardProperty.cardName == 'Income Tax':
            GameWindow.displayLabel.setText(f"{self.name} landed on Income Tax and has been fined £200.")
            self.reduceBalance(GameWindow, 200, playerList, fastBankruptcy, True, houseIndicators, mortgageIndicators, ownershipIndicators, gameValues)

        elif boardProperty.cardName == 'Go To Jail':
            GameWindow.displayLabel.setText(f"{self.name} landed on Go to Jail and has been arrested!")
            self.sendToJail(GameWindow)
        
        elif boardProperty.cardName == 'Free Parking':
            GameWindow.displayLabel.setText(f"{self.name} landed on Free Parking, and is chilling for this turn.")

        elif boardProperty.cardName == 'Go':
            GameWindow.displayLabel.setText(f"{self.name} landed on Go, and is chilling for this turn.")
        
        elif boardProperty.cardName == 'Chance':
            GameWindow.displayLabel.setText(f"{self.name} landed on Chance, and will draw a card.")
            chanceCounter = chance.drawChance(self, GameWindow, board, playerList, roll, gameValues, moneyFromGo, fastBankruptcy, rentFromJail, houseIndicators, mortgageIndicators, ownershipIndicators)
            QtTest.QTest.qWait(1000)


        else:
            if boardProperty.mortgaged:
                GameWindow.displayLabel.setText(f"{self.name} landed on {boardProperty.name}, a mortgaged property.")

            elif boardProperty.ownerID != "0":
                if boardProperty.ownerID == str(self.playerID):
                    GameWindow.displayLabel.setText(f"{self.name} landed on {boardProperty.cardName}, a property they own.")
                else:
                    GameWindow.displayLabel.setText(f"{self.name} landed on {boardProperty.cardName}, a property owned by player{boardProperty.ownerID}")
                    self.payRent(GameWindow, boardProperty, playerList, roll, False, fastBankruptcy, houseIndicators, mortgageIndicators, ownershipIndicators, gameValues)

            else:
                GameWindow.displayLabel.setText(f"{self.name} landed on {boardProperty.cardName}")
                GameWindow.endTurnButton.setEnabled(False)
                GameWindow.bankruptButton.setEnabled(False)
                GameWindow.mortgageButton.setEnabled(False)
                GameWindow.housesButton.setEnabled(False)
                GameWindow.tradeButton.setEnabled(False)

                if boardProperty.cardSet == "Travel Square":
                    GameWindow.travelSquareFrame.show()
                    GameWindow.travelSquareNameLabel.setText(boardProperty.cardName)
                elif boardProperty.cardSet == "Utility":
                    GameWindow.utilityFrame.show()
                    GameWindow.utilityNameLabel.setText(boardProperty.cardName)
                else:
                    GameWindow.normalCardFrame.show()
                    GameWindow.normalCardNameLabel.setText(boardProperty.cardName)
                    GameWindow.normalCardColourDisplayLabel.setText(boardProperty.cardSet)
                    GameWindow.normalCardCostDisplayLabel.setText(f"£{boardProperty.cost}")
                    GameWindow.normalCardHouseCostDisplayLabel.setText(f"£{boardProperty.houseCost}")
                    GameWindow.normalCardBaseAmountLabel.setText(f"£{boardProperty.rentAmounts[0]}")
                    GameWindow.normalCardOneAmountLabel.setText(f"£{boardProperty.rentAmounts[1]}")
                    GameWindow.normalCardTwoAmountLabel.setText(f"£{boardProperty.rentAmounts[2]}")
                    GameWindow.normalCardThreeAmountLabel.setText(f"£{boardProperty.rentAmounts[3]}")
                    GameWindow.normalCardFourAmountLabel.setText(f"£{boardProperty.rentAmounts[4]}")
                    GameWindow.normalCardFiveAmountLabel.setText(f"£{boardProperty.rentAmounts[5]}")


    def advanceToSquare(self, GameWindow, board, playerList, diceRoll, isDoubled, fastBankruptcy, i, houseIndicators, mortgageIndicators, ownershipIndicators, gameValues):
        self.currentPos = i
        self.token.move(gameValues.cardPositions[i * 2], gameValues.cardPositions[i * 2 + 1])
        if board[i].mortgaged:
            GameWindow.displayLabel.setText(f"{self.name} landed on {board[i].cardName}, a mortgaged property.")
        elif board[i].ownerID != "0":
            GameWindow.displayLabel.setText(f"{self.name} landed on {board[i].cardName}")
            self.payRent(GameWindow, board[i], playerList, diceRoll, isDoubled, fastBankruptcy, houseIndicators, mortgageIndicators, ownershipIndicators, gameValues)
        else:
            GameWindow.endTurnButton.setEnabled(False)
            GameWindow.bankruptButton.setEnabled(False)
            GameWindow.mortgageButton.setEnabled(False)
            GameWindow.housesButton.setEnabled(False)
            GameWindow.tradeButton.setEnabled(False)

            if board[i].cardSet == "Travel Square":
                GameWindow.travelSquareFrame.show()
                GameWindow.travelSquareNameLabel.setText(board[i].cardName)
            elif board[i].cardSet == "Utility":
                GameWindow.utilityFrame.show()
                GameWindow.utilityNameLabel.setText(board[i].cardName)
            else:
                GameWindow.normalCardFrame.show()
                GameWindow.normalCardNameLabel.setText(board[i].cardName)
                GameWindow.normalCardColourDisplayLabel.setText(board[i].cardSet)
                GameWindow.normalCardCostDisplayLabel.setText(f"£{board[i].cost}")
                GameWindow.normalCardHouseCostDisplayLabel.setText(f"£{board[i].houseCost}")
                GameWindow.normalCardBaseAmountLabel.setText(f"£{board[i].rentAmounts[0]}")
                GameWindow.normalCardOneAmountLabel.setText(f"£{board[i].rentAmounts[1]}")
                GameWindow.normalCardTwoAmountLabel.setText(f"£{board[i].rentAmounts[2]}")
                GameWindow.normalCardThreeAmountLabel.setText(f"£{board[i].rentAmounts[3]}")
                GameWindow.normalCardFourAmountLabel.setText(f"£{board[i].rentAmounts[4]}")
                GameWindow.normalCardFiveAmountLabel.setText(f"£{board[i].rentAmounts[5]}")


    def leaveJail(self, GameWindow):
        self.currentPos = 10
        self.turnsInJail = 0
        self.doublesCount = 0
        self.inJail = False
        GameWindow.displayLabel2.setText(f"{self.name} has been released from jail.")
        GameWindow.inJailGroupBox.hide()
    

    def sendToJail(self, GameWindow, gameValues):
        self.currentPos = 10
        self.turnsInJail = 0
        self.doublesCount = 0
        self.inJail = True
        self.token.move(gameValues.cardPositions[self.currentPos * 2], gameValues.cardPositions[self.currentPos * 2 + 1])
        GameWindow.displayLabel2.setText(f"{self.name} has been sent to jail.")
        GameWindow.playTurnButton.setEnabled(False)
        GameWindow.endTurnButton.show()
        GameWindow.endTurnButton.setEnabled(True)
    

    def addBalance(self, GameWindow, amount, gameValues):
        self.balance += amount
        GameWindow.transactionLabel.setText(f"£{amount} has been added to {self.name}")
        gameValues.moneyEarned += amount
        self.balanceLabel.setText(f"£{self.balance}")
        return self.balance


    def reduceBalance(self, GameWindow, amount, playerList, fastBankruptcy, nonRentPayment, houseIndicators, mortgageIndicators, ownershipIndicators, gameValues):
        self.balance -= amount
        if self.balance < 0:
            if fastBankruptcy:
                return self.balance
            else:
                GameWindow.bankruptButton.show()
                GameWindow.endTurnButton.hide()
        elif nonRentPayment:
                self.balanceLabel.setText(f"£{self.balance}")
                GameWindow.transactionLabel.setText(f"£{amount} has been deducted from {self.name}.")
        return self.balance
    

    def payRent(self, GameWindow, card, playerList, roll, isDoubled, fastBankruptcy, houseIndicators, mortgageIndicators, ownershipIndicators, gameValues):
        cardOwner = self.findOwner(card, playerList)
        if cardOwner.inJail == True and gameValues.rentFromJail == False:
            GameWindow.displayLabel2.setText("Players cannot gain rent from jail, so no money was transactioned.")
        else:
            if card.cardSet == "Travel Square":
                if cardOwner.travelSquaresOwned == 1:
                    rent = 25
                elif cardOwner.travelSquaresOwned == 2:
                    rent = 50
                elif cardOwner.travelSquaresOwned == 3:
                    rent = 100
                elif cardOwner.travelSquaresOwned == 4:
                    rent = 200
            elif card.cardSet == "Utility":
                if cardOwner.utilitiesOwned == 1:
                    rent = roll * 4
                elif cardOwner.utilitiesOwned == 2:
                    rent = roll * 10
            else:
                rent = card.rentAmounts[card.housesBuilt]
            if isDoubled:
                rent *= 2
            GameWindow.displayLabel2.setText(f"{self.name} is paying £{rent} to {cardOwner.name} for rent.")
            self.reduceBalance(GameWindow, rent, playerList, fastBankruptcy, False, houseIndicators, mortgageIndicators, ownershipIndicators, gameValues)
            cardOwner.addBalance(GameWindow, rent, gameValues)
            gameValues.rentPaid += rent


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
        
    def bankruptPlayer(self, GameWindow, playerList, houseIndicators, mortgageIndicators, ownershipIndicators, gameValues):
        self.balance = -1
        self.travelSquaresOwned = 0
        self.bankrupt = True
        self.token.hide()
        self.balanceLabel.hide()
        font = self.nameLabel.font()
        font.setStrikeOut(True)
        self.nameLabel.setFont(font)

        if len(self.ownedCards) > 0:
            for card in self.ownedCards:
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
        GameWindow.displayLabel2.setText(f"{self.name} is now bankrupt. It is game over for them!")
        GameWindow.displayLabel.setText("")
        GameWindow.endTurnButton.hide()
        GameWindow.bankruptButton.show()
        if len(playerList) == 1:
            gameValues.gameEnded = True


    def findOwner(self, card, playerList):
         for person in playerList:
            if str(person.playerID) == card.ownerID:
                return person
