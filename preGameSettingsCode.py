import sys
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

from gameCode import GameWindow as gameWindow

class PreGameSettingsWindow(QDialog):
    def __init__(self, username):
        super(PreGameSettingsWindow, self).__init__()
        loadUi('C:\\Users\\willj\\OneDrive\\Documents\\Y13\\coursework\\UI\\preGameSettings.ui', self)
        self.preGamePlayButton.clicked.connect(self.game)
        self.preGameReturnButton.clicked.connect(self.close)
    
    def game(self, username):
        startingBalance = self.startingBalanceSpinBox.value()
        moneyFromGo = self.moneyFromGoSpinBox.value()
        numberOfPlayers = self.numberOfPlayersSpinBox.value()
        fastBankruptcy = self.fastBankruptcyCheckBox.checked()
        rentFromJail = self.rentFromJailCheckBox.checked()
        self._new_window = gameWindow(username, startingBalance, moneyFromGo, numberOfPlayers, fastBankruptcy, rentFromJail)
        self._new_window.show()
        self.close


