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
    
    def __init__(self, playerID, name, balance):
        self.playerID = playerID
        self.name = name
        self.balance = balance
    

    def rollDice(self):
        input("Press enter to roll the dice ")

        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        roll = dice1 + dice2
        print(f"{self.name} threw a {dice1} and a {dice2}, giving a roll of {roll}.")

        if dice1 == dice2:
            self.doublesCount += 1
            if self.doublesCount == 3:
                self.sendToJail()
                return roll
        else:
            self.doublesCount = 0
        return roll
    

    def sendToJail(self):
        self.currentPos = 10
        self.turnsInJail = 0
        self.doublesCount = 0
        self.inJail = True
    
    def leaveJail(self):
        self.currentPos = 10
        self.turnsInJail = 0
        self.doublesCount = 0
        self.inJail = False

    def playInJail(self, board, playerList, chanceCounter, randomList, moneyFromGo, fastBankruptcy, rentFromJail):
        self.doublesCount = 0

        if self.turnsInJail >= 3:
            print("Now that you have spent 3 turns in jail, you have been released and will roll again")
            self.leaveJail()
            self.playTurn(board, playerList, chanceCounter, randomList, moneyFromGo, fastBankruptcy, rentFromJail)
            return
        
        if self.GOOJFC:
            choice = input("Do you want to use your get out of jail free card to exit jail? (y/n) ")
            if choice == "y":
                self.leaveJail()
                self.GOOJFC = False
                print("You used your get out of jail free card.")
                diceRoll = self.rollDice()
                self.movePlayer(diceRoll)
                chanceCounter = self.checkPosition(board, playerList, diceRoll, chanceCounter, randomList, moneyFromGo, fastBankruptcy, rentFromJail)
                return

        self.rollDice()

        if self.doublesCount == 1:
            print("Your double got you out of jail")
            self.leaveJail()
            diceRoll = self.rollDice()
            self.movePlayer(diceRoll)
            chanceCounter = self.checkPosition(board, playerList, diceRoll, chanceCounter, randomList, moneyFromGo, fastBankruptcy, rentFromJail)
            return
        
        bail = input("Would you like to pay the £50 bail? (y/n) ")

        if bail == "y":
            self.leaveJail()
            self.reduceBalance(50)
            print("You are no longer in jail")
        else:
            self.turnsInJail += 1
            print(f"You spent the turn in jail, and have now spent {self.turnsInJail} in jail")


    def movePlayer(self, amount):
        self.currentPos += amount
        return self.currentPos 
    

    def addBalance(self, amount):
        self.balance += amount
        print(f"{self.name} now has £{self.balance}")
        return self.balance
    

    def reduceBalance(self, amount, playerList):
        if self.balance < amount:
            bankruptCheck = self.checkBankruptcy(amount, playerList)
            if not bankruptCheck:
                sell = input("Do you want to sell houses and properties to avoid going bankrupt? (y/n)")
                if sell == "y":
                    pass
                    #Add option to sell/mortgage houses and properties.
                else:
                    self.bankruptPlayer(playerList)
            else:
                self.bankruptPlayer(playerList)
        else:
            self.balance -= amount
            print(f"{self.name} now has £{self.balance}")
            return self.balance
    

    def bankruptPlayer(self, playerList):
        self.balance = 0
        self.travelSquaresOwned = 0
        self.bankrupt = True
        
        if len(self.ownedCards) > 0:
            for card in self.cardsOwned:
                card.owner = "Bank"
                card.ownerID = "0"
                card.mortgaged = False
                card.housesBuilt = 0
        
        print(f"Unfortunately, {self.name} is now bankrupt! It's game over for them!")

    

    def checkBankruptcy(self, amount, playerList):
        worth = 0

        for card in self.ownedCards:
            if not card.mortgaged:
                worth += card.mortgageCost
            if card.housesBuilt != "N/A":
                worth += card.housesBuilt * card.houseCost

        if (self.balance + worth) < amount:
            self.bankruptPlayer(playerList)
            return True
        else:
            return False


    def findOwner(self, card, playerList):
         for person in playerList:
            if str(person.playerID) == card.ownerID:
                return person


    def payRent(self, card, playerList, roll, isDoubled):
        cardOwner = self.findOwner(card, playerList)
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
        print(f"{self.name} is paying £{rent} to {cardOwner.name} for rent.")
        self.reduceBalance(rent, playerList)
        cardOwner.addBalance(rent)
    
    def advanceToSquare(self, board, playerList, diceRoll, isDoubled, i):
        print(f"{self.name} landed on {board[i].cardName}")
        self.currentPos = i
        if board[i].mortgaged:
            print(f"{self.name} landed on a mortgaged property.")
        elif board[i].ownerID != "0":
            self.payRent(board[i], playerList, diceRoll, isDoubled)
        else:
            question = input(f"Do you want to buy the property? It costs £{board[i].cost} (y/n) ")
            if question == 'y':
                board[i].purchaseCard(self)


    def checkPosition(self, board, playerList, roll, chanceCounter, randomList, moneyFromGo, fastBankruptcy, rentFromJail):
        if self.currentPos >= 40:
            print(f"{self.name} passed Go, and collects £{moneyFromGo}.")
            self.addBalance(moneyFromGo)
            self.currentPos = self.currentPos % 40
        boardProperty = board[self.currentPos]

        if boardProperty.cardName == 'Jail' and not self.inJail:
                print(f"{self.name} is visiting jail.")
        
        elif boardProperty.cardName == 'Jail' and self.inJail:
                print(f"{self.name} is in jail.")

        elif boardProperty.cardName == 'Luxury Tax':
            print(f"{self.name} landed on Luxury Tax and has been fined £75.")
            self.reduceBalance(75, playerList)

        elif boardProperty.cardName == 'Income Tax':
            print(f"{self.name} landed on Income Tax and has been fined £200.")
            self.reduceBalance(200, playerList)

        elif boardProperty.cardName == 'Go To Jail':
            print(f"{self.name} landed on Go to Jail and has been arrested!")
            self.sendToJail()
        
        elif boardProperty.cardName == 'Free Parking':
            print(f"{self.name} landed on Free Parking, and is chilling for this turn.")

        elif boardProperty.cardName == 'Go':
            print(f"{self.name} landed on Go, and is chilling for this turn.")
        
        elif boardProperty.cardName == 'Chance':
            print(f"{self.name} landed on Chance, and will draw a card.")
            chanceCounter = chance.drawChance(self, board, playerList, roll, chanceCounter, randomList, moneyFromGo, fastBankruptcy, rentFromJail)

        else:
            if boardProperty.mortgaged:
                print(f"{self.name} landed on a mortgaged property.")

            elif boardProperty.ownerID != "0":
                if boardProperty.ownerID == str(self.playerID):
                    print(f"{self.name} landed on {boardProperty.cardName}, a property they own.")
                else:

                    print(f"{self.name} landed on {boardProperty.cardName}, a property owned by player{boardProperty.ownerID}")
                    self.payRent(boardProperty, playerList, roll, False)

            else:
                print(f"{self.name} landed on {boardProperty.cardName}")
                question = input(f"Do you want to buy the property? It costs £{boardProperty.cost} (y/n) ")
                if question == 'y':
                    boardProperty.purchaseCard(self)
        
        return chanceCounter


    def playTurn(self, board, playerList, chanceCounter, randomList, moneyFromGo, fastBankruptcy, rentFromJail):
        if self.inJail:
            self.playInJail(board, playerList, chanceCounter, randomList, moneyFromGo, fastBankruptcy, rentFromJail)
        else:
            diceRoll = self.rollDice()
            self.movePlayer(diceRoll)
            chanceCounter = self.checkPosition(board, playerList, diceRoll, chanceCounter, randomList, moneyFromGo, fastBankruptcy, rentFromJail)
        if self.doublesCount > 0:
            self.playTurn(board, playerList, chanceCounter, randomList, moneyFromGo, fastBankruptcy, rentFromJail)
        
        return chanceCounter