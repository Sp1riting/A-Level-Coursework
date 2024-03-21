import sys
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi


from howToPlayCode import HowToPlayWindow as howToPlayWindow
from gameStatisticsCode import GameStatisticsWindow as statisticsWindow
from preGameSettingsCode import PreGameSettingsWindow as preGameSettingsWindow

class MainMenuWindow(QDialog):
    def __init__(self, username):
        super(MainMenuWindow, self).__init__()
        loadUi('C:\\Users\\willj\\OneDrive\\Documents\\Y13\\coursework\\UI\\mainMenu.ui', self)
        self.username = username
        self.menuHowToPlayButton.clicked.connect(self.howToPlay)
        self.menuStatisticsButton.clicked.connect(self.statistics)
        self.menuPlayButton.clicked.connect(self.preGame)
        self.menuReturnButton.clicked.connect(self.close)

    def howToPlay(self):
        self._new_window = howToPlayWindow()
        self._new_window.show()
        self.close

    def statistics(self):
        self._new_window = statisticsWindow(self.username)
        self._new_window.show()
        self.close
    
    def preGame(self):
        self._new_window = preGameSettingsWindow(self.username, False, False)
        self._new_window.show()
        self.close


