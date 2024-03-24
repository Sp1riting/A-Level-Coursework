import random
import Classes.card as Cards
import chance as chance
from GameStart import board as board

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
        

        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        roll = dice1 + dice2
        print(f"{self.name} threw a {dice1} and a {dice2}, giving a roll of {roll}.")

        if dice1 == dice2:
            self.doublesCount += 1
            if self.doublesCount == 3:
                self.sendToJail(GameWindow)
                return roll
        else:
            self.doublesCount = 0
        return roll

    
    def leaveJail(self, GameWindow):
        self.currentPos = 10
        self.turnsInJail = 0
        self.doublesCount = 0
        self.inJail = False
        GameWindow.displayLabel.setText(f"{self.name} has been released from jail.")
        GameWindow.inJailGroupBox.hide()
    

    def reduceBalance(self, GameWindow, amount, playerList, fastBankrutcy, nonRentPayment, houseIndicators, mortgageIndicators, ownershipIndicators):
        if self.balance < amount:
            if fastBankrutcy:
                self.bankruptPlayer(GameWindow, playerList, houseIndicators, mortgageIndicators, ownershipIndicators)
            else:
                GameWindow.bankruptButton.show()
                GameWindow.endTurnButton.hide()
        else:
            self.balance -= amount
            if nonRentPayment:
                self.balanceLabel.setText(f"£{self.balance}")
                GameWindow.transactionLabel.setText(f"£{amount} has been deducted from {self.name}.")
    

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
