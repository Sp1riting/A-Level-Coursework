import sys
import sqlite3
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

conn = sqlite3.connect('users.db')
database = conn.cursor()

class GameStatisticsWindow(QDialog):
    def __init__(self, username):
        super(GameStatisticsWindow, self).__init__()
        loadUi('C:\\Users\\willj\\OneDrive\\Documents\\Y13\\coursework\\UI\\gameStatistics.ui', self)
        
        query = database.execute("SELECT * FROM users WHERE username = ?",(username,))
        instance = query.fetchone()

        self.doublesRolledValue = instance[2]
        self.gamesPlayedValue = instance[3]
        self.propertiesPurchasedValue = instance[4]
        self.moneyEarnedValue = instance[5]
        self.rentPaidValue = instance[6]
        self.passedGoValue = instance[7]
        
        self.gameStatsReturnButton.clicked.connect(self.close)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    accountWindow = GameStatisticsWindow()
    accountWindow.showFullScreen()
    widget = QStackedWidget()
    widget.addWidget(accountWindow)
    widget.show()
    
    app.exec_()