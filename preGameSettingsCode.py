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
    
    def game(self, username, fastBankruptcy, rentFromJail):
        startingBalance = self.startingBalanceSpinBox.value()
        moneyFromGo = self.moneyFromGoSpinBox.value()
        numberOfPlayers = self.numberOfPlayersSpinBox.value()
        playerNames = []
        if self.fastBankruptcyCheckBox.isChecked():
            fastBankruptcy = True
        else:

            fastBankruptcy = False
        if self.rentFromJailCheckBox.isChecked():
            rentFromJail = True
        else:
            rentFromJail = False

        for i in range (1, numberOfPlayers + 1):
            (userInput, entered) = QInputDialog.getText(self,"Get text",f"Enter the name of player number {i}",QLineEdit.Normal,f"player{i}")
            if entered:
                playerNames.append(userInput)
            else:
                playerNames.append(f"player{i}")

        self._new_window = gameWindow(username, startingBalance, moneyFromGo, numberOfPlayers, fastBankruptcy, rentFromJail, playerNames)
        self.close()
        self._new_window.show()



