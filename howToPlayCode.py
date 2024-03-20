import sys
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

class HowToPlayWindow(QDialog):
    def __init__(self):
        super(HowToPlayWindow, self).__init__()
        loadUi('C:\\Users\\willj\\OneDrive\\Documents\\Y13\\coursework\\UI\\howToPlay.ui', self)
        self.howToPlayReturnButton.clicked.connect(self.close)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    accountWindow = HowToPlayWindow()
    accountWindow.showFullScreen()
    widget = QStackedWidget()
    widget.addWidget(accountWindow)
    widget.show()
    
    app.exec_()