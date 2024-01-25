class Card:
    def __init__(self, cost, cardName, cardSet, houseCost, housesBuilt, mortgaged, mortgageCost, owner, rentAmounts):
        self.cost = cost
        self.cardName = cardName
        self.cardSet = cardSet
        self.houseCost = houseCost
        self.housesBuilt = housesBuilt
        self.mortgaged = mortgaged
        self.mortgageCost = mortgageCost
        self.owner = owner
        self.rentAmounts = rentAmounts
    
    def mortgage(self, player):
        player.addBalance(self.mortgageCost)
        self.mortgaged = True
    
    def sell(self, player):
        player.addBalance(self.cost)
        self.owner = 'Bank'
        self.housesBuilt = 0
    
    def purchaseCard(self, player):
        if self.cost > player.balance:
            print("You do not have enough to purchase this card")
        else:
            player.ownedCards.append(self)
            player.reduceBalance(self.cost)
            self.owner = player.playerID

def locateCard(name, board):

    for card in board:
        if card.cardName == name:
            cardObject = card
            break
    return cardObject