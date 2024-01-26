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
    
    def mortgage(self, player):
        player.addBalance(self.mortgageCost)
        self.mortgaged = True
    
    def sell(self, player):
        if self.cardSet == "TravelSquare":
            player.travelSquaresOwned -= 1
        player.addBalance(self.cost)
        self.owner = 'Bank'
        self.ownerID = "0"
        self.housesBuilt = 0
    
    def purchaseCard(self, player):
        if self.cost > player.balance:
            print("You do not have enough to purchase this card")
        else:
            if self.cardSet == "Travel Square":
                player.travelSquaresOwned += 1
            elif self.cardSet == "Utility":
                player.utilitiesOwned += 1
            player.ownedCards.append(self)
            player.reduceBalance(self.cost)
            self.owner = player.name
            self.ownerID = str(player.playerID)


def locateCard(name, board):
    for card in board:
        if card.cardName == name:
            cardObject = card
            break
    return cardObject