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
    
    def mortgage(self, GameWindow, player, gameValues, houseIndicators, mortgageIndicators, ownershipIndicators):
        if self.cardName in player.ownedCards:
            if self.housesBuilt == 0 or self.housesBuilt == "N/A":
                if self.cardSet == "TravelSquare":
                    player.travelSquaresOwned -= 1
                elif self.cardSet == "Utility":
                    player.utilitiesOwned -= 1
                player.addBalance(GameWindow, self.mortgageCost, gameValues)
                self.mortgaged = True
                #player.ownedCards.remove(self.cardName)
            else:
                GameWindow.mortgageLabel.setText("Sell all houses on this property before mortgaging")
        else:
            GameWindow.mortgageLabel.setText("You have already mortgaged this property.")
    
    
    def unmortgage(self, GameWindow, gameValues, playerList, fastBankruptcy, houseIndicators, mortgageIndicators, ownershipIndicators):
        if self.mortgaged:
            if self.cost > gameValues.currentPlayer.balance:
                GameWindow.mortgageLabel.setText("You do not have enough to unmortgage this card")
            else:
                if self.cardSet == "TravelSquare":
                    gameValues.currentPlayer.travelSquaresOwned += 1
                elif self.cardSet == "Utility":
                    gameValues.currentPlayer.utilitiesOwned += 1
                gameValues.currentPlayer.reduceBalance(GameWindow, self.cost, playerList, fastBankruptcy, True, houseIndicators, mortgageIndicators, ownershipIndicators, gameValues)
                self.mortgaged = False
                #gameValues.currentPlayer.ownedCards.append(self.cardName)
                GameWindow.mortgageLabel.setText("")
        else:
            GameWindow.mortgageLabel.setText("You have already unmortgaged this property")


    def purchaseHouse(self, GameWindow, gameValues, playerList, fastBankruptcy, houseIndicators, mortgageIndicators, ownershipIndicators):
        if int(self.houseCost) > gameValues.currentPlayer.balance:
            GameWindow.housesLabel.setText("You do not have enough to purchase this house")
        elif self.housesBuilt >= 5:
            GameWindow.housesLabel.setText("You have already built the maximum number of houses on this property")
        else:
            GameWindow.housesLabel.setText("")
            self.housesBuilt += 1
            houseIndicators[gameValues.currentPlayer.currentPos].display(houseIndicators[gameValues.currentPlayer.currentPos].value() + 1)
            gameValues.currentPlayer.reduceBalance(GameWindow, int(self.houseCost), playerList, fastBankruptcy, True, houseIndicators, mortgageIndicators, ownershipIndicators, gameValues)
    

    def sellHouse(self, GameWindow, player, gameValues, houseIndicators, mortgageIndicators, ownershipIndicators):
        if self.housesBuilt == 0:
            GameWindow.housesLabel.setText("You cannot sell houses from this property")
        else:
            GameWindow.housesLabel.setText("")
            self.housesBuilt -= 1
            houseIndicators[player.currentPos].display(houseIndicators[player.currentPos].value() - 1)
            player.addBalance(GameWindow, int(self.houseCost / 2), gameValues)

    def purchaseCard(self, GameWindow, player, houseIndicators, mortgageIndicators, ownershipIndicators, playerList, fastBankruptcy, gameValues):
        if self.cost > player.balance:
            GameWindow.displayLabel2.setText("You did not have enough to purchase this card")
        else:
            if self.cardSet == "Travel Square":
                player.travelSquaresOwned += 1
            elif self.cardSet == "Utility":
                player.utilitiesOwned += 1
            player.reduceBalance(GameWindow, self.cost, playerList, fastBankruptcy, True, houseIndicators, mortgageIndicators, ownershipIndicators, gameValues)
            self.owner = player.name
            self.ownerID = str(player.playerID)
            player.ownedCards.append(self.cardName)
            gameValues.propertiesPurchased += 1


def locateCard(name, board):
    for card in board:
        if card.cardName == name:
            cardObject = card
            break
    return cardObject