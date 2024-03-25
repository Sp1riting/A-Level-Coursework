import sys
import sqlite3
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

conn = sqlite3.connect('users.db')
database = conn.cursor()

class EndGameWindow(QDialog):
    def __init__(self, gameValues, playerList, username):
        super(EndGameWindow, self).__init__()
        loadUi('C:\\Users\\willj\\OneDrive\\Documents\\Y13\\coursework\\UI\\endGameScreen.ui', self)
        self.winnerDisplayLabel.setText(playerList[0].name)
        self.doublesDisplayLabel.setText(f"£{gameValues.doublesRolled}")
        self.propertiesDisplayLabel.setText(gameValues.propertiesPurchased)
        self.earnedDisplayLabel.setText(f"£{gameValues.moneyEarned}")
        self.rentDisplayLabel.setText(f"£{gameValues.rentPaid}")
        self.goDisplayLabel.setText(gameValues.passedGo)

        query = database.execute("SELECT * FROM users WHERE username = ?",(username,))
        instance = query.fetchone()

        doublesRolledValue = instance[2] + gameValues.doublesRolled
        gamesPlayedValue = instance[3] + 1
        propertiesPurchasedValue = instance[4] + gameValues.propertiesPurchased
        moneyEarnedValue = instance[5] + gameValues.moneyEarned
        rentPaidValue = instance[6] + gameValues.rentPaid
        passedGoValue = instance[7] + gameValues.passedGo

        database.execute(f"""UPDATE users 
                         SET rolledDoubles = {doublesRolledValue}, gamesPlayed = {gamesPlayedValue}, propertiesBought = {propertiesPurchasedValue}, moneyEarned = {moneyEarnedValue}, rentPaid = {rentPaidValue}, passedGo = {passedGoValue} 
                         WHERE username = ?""",(username,)
                         )
        

        self.gameEndReturnButton.clicked.connect(self.close())
