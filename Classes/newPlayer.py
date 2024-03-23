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
    
    def __init__(self, playerID, name, balance, token, colour):
        self.playerID = playerID
        self.name = name
        self.balance = balance
        self.token = token
        self.colour = colour
    
    def leaveJail(self, GameWindow):
        self.currentPos = 10
        self.turnsInJail = 0
        self.doublesCount = 0
        self.inJail = False
        GameWindow.displayLabel.setText(f"{self.name} has been released from jail.")
    
