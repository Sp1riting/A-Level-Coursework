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
        self._new_window = gameWindow
        self._new_window.show(username)
        self.close


if __name__ == '__main__':
    app = QApplication(sys.argv)
    accountWindow = PreGameSettingsWindow()
    accountWindow.showFullScreen()
    widget = QStackedWidget()
    widget.addWidget(accountWindow)
    widget.show()
    
    app.exec_()