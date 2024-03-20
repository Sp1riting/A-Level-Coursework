import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox, QStackedWidget
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSlot
import bcrypt

#Connect to the SQLite database
conn = sqlite3.connect('users.db')
database = conn.cursor()

#Create a new table if one doesn't exist
database.execute('''CREATE TABLE IF NOT EXISTS users
                (username TEXT PRIMARY KEY, password TEXT, 
                rolledDoubles INTEGER, gamesPlayed INTEGER, propertiesBought INTEGER, moneyEarned INTEGER, rentPaid INTEGER, passedGo INTEGER)
                 ''')
conn.commit()

class LoginWindow(QDialog):
    def __init__(self):
        super(LoginWindow, self).__init__()
        loadUi('C:\\Users\\willj\\OneDrive\\Documents\\Y13\\coursework\\UI\\login.ui', self)
        self.loginButton.clicked.connect(self.login)
        self.loginReturnButton.clicked.connect(self.close)

    @pyqtSlot()
    def login(self):
        username = self.loginUsernameInput.text()
        password = self.loginPasswordInput.text()

        if not username or not password:
            self.loginErrorLabel.setText("Please enter a username and password")
            return

        database.execute("SELECT * FROM users WHERE username=?", (username),)
        existingUser = database.fetchone()
        if existingUser:
            self.loginErrorLabel.setText("Username already exists")
            return

        hashedPword = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    accountWindow = LoginWindow()
    accountWindow.showFullScreen()
    widget = QStackedWidget()
    widget.addWidget(accountWindow)
    widget.show()
    
    app.exec_()