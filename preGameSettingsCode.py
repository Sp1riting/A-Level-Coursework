import sys
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

from gameCode import GameWindow as gameWindow

class PreGameSettingsWindow(QDialog):
    def __init__(self, username, fastBankruptcy, rentFromJail):
        super(PreGameSettingsWindow, self).__init__()
        loadUi('C:\\Users\\willj\\OneDrive\\Documents\\Y13\\coursework\\UI\\preGameSettings.ui', self)
        self.preGamePlayButton.clicked.connect(lambda:self.game(username, fastBankruptcy, rentFromJail))
        self.preGameReturnButton.clicked.connect(self.close)
        fastBankruptcy = self.fastBankruptcyCheckBox.clicked.connect(lambda:self.changeFastBankruptcy(fastBankruptcy))
        rentFromJail = self.rentFromJailCheckBox.clicked.connect(lambda:self.changeRentFromJail(rentFromJail))
    
    def game(self, username, fastBankruptcy, rentFromJail):
        startingBalance = self.startingBalanceSpinBox.value()
        moneyFromGo = self.moneyFromGoSpinBox.value()
        numberOfPlayers = self.numberOfPlayersSpinBox.value()

        self._new_window = gameWindow(username, startingBalance, moneyFromGo, numberOfPlayers, fastBankruptcy, rentFromJail)
        self._new_window.show()
        self.close
    
    def changeFastBankruptcy(self, fastBankruptcy):
        if fastBankruptcy:
            fastBankruptcy = False
        else:
            fastBankruptcy = True
    
    def changeRentFromJail(self, rentFromJail):
        if rentFromJail:
            rentFromJail = False
        else:
            rentFromJail = True


