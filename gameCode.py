import sys
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import main as main

class GameWindow(QDialog):
    def __init__(self, username, startingBalance, moneyFromGo, numberOfPlayers, fastBankruptcy, rentFromJail):
        super(GameWindow, self).__init__()
        loadUi('C:\\Users\\willj\\OneDrive\\Documents\\Y13\\coursework\\UI\\game.ui', self)

