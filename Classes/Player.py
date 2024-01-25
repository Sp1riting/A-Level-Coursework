import random
import GameStart as gameStart
import Classes.card as Cards
from GameStart import board as board

counter = 0

class Player:
    def __init__(self, playerID, name, balance, ownedCards, currentPos, doublesCount, travelSquaresOwned, bankrupt, inJail, housesOwned, gamesPlayed, wins, losses):
        self.playerID = playerID
        self.name = name
        self.balance = balance
        self.ownedCards = ownedCards
        self.currentPos = currentPos
        self.doublesCount = doublesCount
        self.travelSquaresOwned = travelSquaresOwned
        self.bankrupt = bankrupt
        self.inJail = inJail
        self.housesOwned = housesOwned
        self.gamesPlayed = gamesPlayed
        self.wins = wins
        self.losses = losses
    
    def rollDice(self):
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
        self.doublesCount = 0
        self.inJail = True
    
    def playInJail(self):
        self.doublesCount = 0
        bail = input("Would you like to pay the $50 bail? (y/n) ")
        if bail == "y":
            self.reduceBalance(50)
            self.inJail = False
            self.playTurn(board)
        else:
            self.rollDice()
            if self.doublesCount == 1:
                self.doublesCount = 0
                diceRoll = self.rollDice()
                self.movePlayer(diceRoll)
                self.checkPosition(board)
    
    def movePlayer(self, amount):
        self.currentPos += amount
        return self.currentPos
    
    
    def addBalance(self, amount):
        self.balance += amount
        return self.balance
    
    def reduceBalance(self, amount):
        if self.balance < amount:
            bankruptCheck = self.checkBankruptcy(amount)
            if not bankruptCheck:
                sell = input("Do you want to sell houses and properties to avoid going bankrupt? (y/n)") 
                #Add option to sell/mortgage houses and properties.
            else:
                self.bankruptPlayer()
        else:
            self.balance -= amount
            return self.balance
    
    def bankruptPlayer(self):
        self.balance = 0
        self.travelSquaresOwned = 0
        self.bankrupt = True
        
        if len(self.cardsOwned) > 0:
            for card in self.cardsOwned:
                card.owner = "Bank"
    
    def checkBankruptcy(self, amount):
        worth = 0

        for card in self.cardsOwned:
            if card.mortgaged == True:
                worth -= card.mortgageCost
                worth += card.cost
            else:
                worth += card.cost

        if (self.balance + worth) < amount:
            print(f"Unfortunately, {self.name} is now bankrupt! It's game over for them!")
            self.bankruptPlayer()
            return True
        else:
            return False

    def drawChance(self,counter):
        currentChance = counter % (4)
        counter += 1
        if currentChance == 0:
            print("Oh no, your friend is asking for a loan from you. Pay $50.")
            self.reduceBalance(50)
        elif currentChance == 1:
            print("Move directly to Go! Collect $200.")
            self.currentPos = 0
            self.addBalance(200)
        elif currentChance == 2:
            print("You win a local raffle and sell the highest prize. Gain $100.")
            self.addBalance(100)
        elif currentChance == 3:
            print("Ouch! You drive into a lampost and have to fix your car. Go back three spaces.")
            self.currentPos = (self.currentPos - 3) % 40
            self.checkPosition(board)
        
    def payRent(self, card):
        if card.cardSet == "Travel Square":
            if card.owner.travelSquaresOwned == 1:
                rent = 25
            if card.owner.travelSquaresOwned == 2:
                rent = 50
            if card.owner.travelSquaresOwned == 3:
                rent = 100
            if card.owner.travelSquaresOwned == 4:
                rent = 200
        else:
            rent = card.rentAmounts[card.housesBuilt]
        print(f"{self.name} is paying ${rent} to {card.owner.name} for rent.")
        self.reduceBalance(rent)
        card.owner.addBalance(rent)

    def checkPosition(self, board):
        if self.currentPos >= 40:
            print(f"{self.name} passed Go, and collects $200.")
            self.addBalance(200)
            self.currentPos = self.currentPos % 40
        boardProperty = board[self.currentPos]

        if boardProperty.cardName == 'Jail' and self.inJail == False:
                print(f"{self.name} is visiting jail.")
        
        elif boardProperty.cardName == 'Jail' and self.inJail == True:
                print(f"{self.name} is in jail.")

        elif boardProperty.cardName == 'Luxury Tax':
            print(f"{self.name} landed on Luxury Tax and has been fined $75.")
            self.reduceBalance(75)

        elif boardProperty.cardName == 'Income Tax':
            print(f"{self.name} landed on Income Tax and has been fined $200.")
            self.reduceBalance(200)

        elif boardProperty.cardName == 'Go To Jail':
            print(f"{self.name} landed on Go to Jail and has been arrested!")
            self.sendToJail()
        
        elif boardProperty.cardName == 'Free Parking':
            print(f"{self.name} landed on Free Parking, and is chilling for this turn.")

        elif boardProperty.cardName == 'Go':
            print(f"{self.name} landed on Go, and is chilling for this turn.")
        
        elif boardProperty.cardName == 'Chance':
            print(f"{self.name} landed on Chance, and will draw a card.")
            self.drawChance(counter)
    
        else:
            #print(f"{self.name} landed on {boardProperty.cardName}")
            
            if boardProperty.mortgaged:
                print(f"{self.name} landed on a mortgaged property.")

            elif boardProperty.owner != 'Bank':
                if boardProperty.owner.name == self.name:
                    print(f"{self.name} landed on {boardProperty.cardName}, a property they own.")
                else:
                    print(f"{self.name} landed on {boardProperty.cardName}, a property owned by {boardProperty.owner.name}")
                    self.payRent(boardProperty)

            else:
                print(f"{self.name} landed on {boardProperty.cardName}")
                Question = input("Do you want to buy the property? (y/n) ")
                if Question == 'y':
                    boardProperty.purchaseCard(self)
        

        
    def trade(self, playerReference, playerList, board):

        for player in playerList:
            if player.name == playerReference:
                otherPlayer = player

        cashGiven = int(input("How much cash are you giving away? "))
        propertiesToOffer = input("Enter the properties do you want to offer separated by commas\n").split(',')

        cashReceived = int(input(f"How much cash is {otherPlayer.name} giving you?"))
        propertiesReceived = input(f"Which properties is {otherPlayer.name} giving you?\n").split(',')

        if propertiesToOffer[0] == '':
            pass
        else:
            for card in propertiesToOffer:
                cardObject = Cards.locateCard(card, board)
                otherPlayer.ownedCards.append(cardObject)

        self.reduceBalance(cashGiven)
        otherPlayer.addBalance(cashGiven)

        if propertiesReceived[0] == '':
            pass
        else:
            for card in propertiesReceived:
                cardObject = Cards.locateCard(card, board)
                self.ownedCards.append(cardObject)

        otherPlayer.reduceBalance(cashReceived)
        self.addBalance(cashReceived)

        print(f"{self.name} has given ${cashGiven} and the following properties: {propertiesToOffer}")
        print(f"{otherPlayer.name} has received ${cashReceived} and the following properties: {propertiesReceived}")

    def playTurn(self,board):
        if self.inJail:
            self.playInJail(diceRoll)
        else:
            diceRoll = self.rollDice()
            self.movePlayer(diceRoll)
            self.checkPosition(board)
        if self.doublesCount > 0:
            playTurn(self,board)
            



#
#Do trading properly later