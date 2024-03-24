class Card:

    mortgaged = False
    owner = "Bank"
    ownerID = "0"

    def __init__(self, cost, cardName, cardSet, houseCost, housesBuilt, mortgageCost, rentAmounts):
        self.cost = cost
        self.cardName = cardName
        self.cardSet = cardSet
        self.houseCost = houseCost
        self.housesBuilt = housesBuilt
        self.mortgageCost = mortgageCost
        self.rentAmounts = rentAmounts
    
    def mortgage(self, GameWindow, player):
        if self.housesBuilt == 0:
            if self.cardSet == "TravelSquare":
                player.travelSquaresOwned -= 1
            elif self.cardSet == "Utility":
                player.utilitiesOwned -= 1
            player.addBalance(self.mortgageCost)
            self.mortgaged = True
            player.ownedCards.remove(self.cardName)
        else:
            print("Sell all houses on this property before mortgaging")
    
    
    def unmortgage(self, GameWindow, player):
        if self.cost > player.balance:
            print("You do not have enough to unmortgage this card")
        else:
            if self.cardSet == "TravelSquare":
                player.travelSquaresOwned += 1
            elif self.cardSet == "Utility":
                player.utilitiesOwned += 1
            player.reduceBalance(GameWindow, self.cost)
            self.mortgaged = False
            player.ownedCards.append(self.cardName)


    def purchaseHouse(self, GameWindow, player):
        if self.cardSet == "Travel Square" or self.cardSet == "Utility":
            print("This property cannot gain houses")
        else:
            if self.houseCost > player.balance:
                print("You do not have enough to purchase this house")
            elif self.housesBuilt >= 5:
                print("You have already built the maximum number of houses on this property")
            else:
                self.housesBuilt += 1
                player.reduceBalance(GameWindow, self.houseCost)
    

    def sellHouse(self, GameWindow, player):
        if self.housesBuilt == 0 or self.housesBuilt == "N/A":
            print("You cannot sell houses from this property")
        else:
            self.housesBuilt -= 1
            player.addBalance(GameWindow, self.houseCost / 2)
                

    def purchaseCard(self, GameWindow, player, houseIndicators, mortgageIndicators, ownershipIndicators, playerList, fastBankruptcy):
        if self.cost > player.balance:
            GameWindow.displayLabel2.setText("You did not have enough to purchase this card")
        else:
            if self.cardSet == "Travel Square":
                player.travelSquaresOwned += 1
            elif self.cardSet == "Utility":
                player.utilitiesOwned += 1
            player.reduceBalance(self, GameWindow, self.cost, playerList, fastBankruptcy, True, houseIndicators, mortgageIndicators, ownershipIndicators)
            self.owner = player.name
            self.ownerID = str(player.playerID)
            player.ownedCards.append(self.cardName)


def locateCard(name, board):
    for card in board:
        if card.cardName == name:
            cardObject = card
            break
    return cardObject