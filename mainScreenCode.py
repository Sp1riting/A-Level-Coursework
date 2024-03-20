import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox, QStackedWidget
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSlot
import bcrypt

class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi('C:\\Users\\willj\\OneDrive\\Documents\\Y13\\coursework\\UI\\mainScreen.ui', self)
        self.openLoginButton.clicked.connect(self.openLogin)
        self.openCreateAccountButton.clicked.connect(self.openCreateAccount)

    def openLogin(self):
        pass

    def openCreateAccount(self):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    accountWindow = MainWindow()
    accountWindow.showFullScreen()
    widget = QStackedWidget()
    widget.addWidget(accountWindow)
    widget.show()
    
    app.exec_()