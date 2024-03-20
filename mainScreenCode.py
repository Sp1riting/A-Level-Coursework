import sys
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

from UI.loginCode import LoginWindow as loginWindow
from UI.createAccountCode import CreateAccountWindow as createAccountWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi('C:\\Users\\willj\\OneDrive\\Documents\\Y13\\coursework\\UI\\mainScreen.ui', self)
        self.openLoginButton.clicked.connect(self.openLogin)
        self.openCreateAccountButton.clicked.connect(self.openCreateAccount)

    def openLogin(self):
        self._new_window = loginWindow()
        self._new_window.show()

    def openCreateAccount(self):
        self._new_window = createAccountWindow()
        self._new_window.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    accountWindow = MainWindow()
    accountWindow.showFullScreen()
    widget = QStackedWidget()
    widget.addWidget(accountWindow)
    widget.show()
    
    app.exec_()