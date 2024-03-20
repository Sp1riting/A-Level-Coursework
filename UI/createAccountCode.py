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
database.execute('''CREATE TABLE IF NOT EXISTS "users" (
	    "username"	TEXT NOT NULL,
	    "password"	TEXT NOT NULL,
	    "rolledDoubles"	INTEGER NOT NULL DEFAULT 0,
	    "gamesPlayed"	INTEGER NOT NULL DEFAULT 0,
	    "propertiesBought"	NUMERIC NOT NULL DEFAULT 0,
	    "moneyEarned"	INTEGER NOT NULL DEFAULT 0,
	    "rentPaid"	INTEGER NOT NULL DEFAULT 0,
	    "passedGo"	INTEGER NOT NULL DEFAULT 0,
	    PRIMARY KEY("username")
        )
        ''')
conn.commit()

class CreateAccountWindow(QDialog):
    def __init__(self):
        super(CreateAccountWindow, self).__init__()
        loadUi('C:\\Users\\willj\\OneDrive\\Documents\\Y13\\coursework\\UI\\createAccount.ui', self)
        self.createAccountButton.clicked.connect(self.createAccount)
        self.createReturnButton.clicked.connect(self.close)

    def createAccount(self):
        username = self.accountUsernameInput.text()
        password = self.accountPasswordInput.text()

        if not username or not password:
            self.createErrorLabel.setText("Please enter a username and password")
            return

        database.execute("SELECT * FROM users WHERE username=?", (username),)
        existingUser = database.fetchone()
        if existingUser:
            self.createErrorLabel.setText("Username already exists")
            return

        hashedPword = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        try:
            database.execute("INSERT INTO users VALUES (?, ?)", (username, hashedPword.decode('utf-8')))
            conn.commit()
            QMessageBox.information(self, "Success", "Account created successfully")
            self.close()
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

""" if __name__ == '__main__':
    app = QApplication(sys.argv)
    accountWindow = CreateAccountWindow()
    accountWindow.showFullScreen()
    widget = QStackedWidget()
    widget.addWidget(accountWindow)
    widget.show()
    
    app.exec_() """