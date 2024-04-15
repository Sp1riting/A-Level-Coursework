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

        self.doublesRolledValue.setText(str(instance[2]))
        self.gamesPlayedValue.setText(str(instance[3]))
        self.propertiesPurchasedValue.setText(str(instance[4]))
        self.moneyEarnedValue.setText(f"£{instance[5]}")
        self.rentPaidValue.setText(f"£{instance[6]}")
        self.passedGoValue.setText(str(instance[7]))



        self.gameStatsReturnButton.clicked.connect(self.close)


