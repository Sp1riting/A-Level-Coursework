import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox, QStackedWidget
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSlot
import bcrypt

# Connect to SQLite database
conn = sqlite3.connect('users.db')
c = conn.cursor()

# Create table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS users
             (username TEXT PRIMARY KEY, password TEXT)''')
conn.commit()

class CreateAccountWindow(QDialog):
    def __init__(self):
        super(CreateAccountWindow, self).__init__()
        loadUi('C:\\Users\\willj\\OneDrive\\Documents\\Y13\\coursework\\UI\\createAccount.ui', self)
        self.createButton.clicked.connect(self.createAccount)
        self.returnButton.clicked.connect(self.close)

    @pyqtSlot()
    def createAccount(self):
        username = self.usernameInput.text()
        password = self.passwordInput.text()

        if not username or not password:
            self.errorLabel.setText("Please enter a username and password")
            return

        c.execute("SELECT * FROM users WHERE username=?", (username,))
        existingUser = c.fetchone()
        if existingUser:
            self.errorLabel.setText("Username already exists")
            return

        hashedPword = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        try:
            c.execute("INSERT INTO users VALUES (?, ?)", (username, hashedPword.decode('utf-8')))
            conn.commit()
            QMessageBox.information(self, "Success", "Account created successfully")
            self.close()
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    accountWindow = CreateAccountWindow()
    accountWindow.showFullScreen()
    widget = QStackedWidget()
    widget.addWidget(accountWindow)
    widget.show()
    
    app.exec_()