import sys
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

class GameWindow(QDialog):
    def __init__(self, username):
        super(GameWindow, self).__init__()
        loadUi('C:\\Users\\willj\\OneDrive\\Documents\\Y13\\coursework\\UI\\game.ui', self)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    accountWindow = GameWindow()
    accountWindow.showFullScreen()
    widget = QStackedWidget()
    widget.addWidget(accountWindow)
    widget.show()
    
    app.exec_()