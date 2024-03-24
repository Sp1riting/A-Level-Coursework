def drawChance(self, GameWindow, board, playerList, diceRoll, chanceCounter, randomList, moneyFromGo, fastBankruptcy, rentFromJail, houseIndicators, mortgageIndicators, ownershipIndicators):

    currentChance = randomList[chanceCounter % len(randomList)]

    if currentChance == 0:
        GameWindow.displayLabel2.setText("Oh no, your friend is asking for a loan from you. Pay £50.")
        self.reduceBalance(GameWindow, 50, playerList, houseIndicators, mortgageIndicators, ownershipIndicators)

    elif currentChance == 1:
        GameWindow.displayLabel2.setText(f"Move directly to Go! Collect £{moneyFromGo}.")
        self.currentPos = 0
        self.addBalance(GameWindow, moneyFromGo)

    elif currentChance == 2:
        GameWindow.displayLabel2.setText("You win a local raffle and sell the highest prize. Gain £100.")
        self.addBalance(GameWindow, 100)

    elif currentChance == 3:
        GameWindow.displayLabel2.setText("Ouch! You drove into a lampost and have to fix your car. Go back three spaces.")
        self.currentPos = (self.currentPos - 3) % 40
        self.checkPosition(GameWindow, board, playerList, diceRoll, chanceCounter, randomList, moneyFromGo, fastBankruptcy, rentFromJail)

    elif currentChance == 4:
        GameWindow.displayLabel2.setText(f"Move directly to jail. You may not pass go, or collect £{moneyFromGo}.")
        self.sendToJail(GameWindow)

    elif currentChance == 5:
        GameWindow.displayLabel2.setText("Advance to the nearest travel square. You may buy it if unowned, but must pay double the normal rent if owned.")
        if (self.currentPos % 40) < 5:
            self.advanceToSquare(GameWindow, board, playerList, diceRoll, True, 5, houseIndicators, mortgageIndicators, ownershipIndicators)
        elif (self.currentPos % 40) < 15:
            self.advanceToSquare(GameWindow, board, playerList, diceRoll, True, 15, houseIndicators, mortgageIndicators, ownershipIndicators)
        elif (self.currentPos % 40) < 25:
            self.advanceToSquare(GameWindow, board, playerList, diceRoll, True, 25, houseIndicators, mortgageIndicators, ownershipIndicators)
        elif (self.currentPos % 40) < 35:
            self.advanceToSquare(GameWindow, board, playerList, diceRoll, True, 35, houseIndicators, mortgageIndicators, ownershipIndicators)
        else:
            GameWindow.displayLabel2.setText(f"{self.name} passed Go, and collects £{moneyFromGo}.")
            self.addBalance(GameWindow, moneyFromGo)
            self.advanceToSquare(GameWindow, board, playerList, diceRoll, True, 5, houseIndicators, mortgageIndicators, ownershipIndicators)
    
    elif currentChance == 6:
        GameWindow.displayLabel2.setText("Advance to the nearest utility. You may buy it if unowned, but must pay double the normal rent if owned.")
        if (self.currentPos % 40) < 12:
            self.advanceToSquare(GameWindow, board, playerList, diceRoll, True, 12, houseIndicators, mortgageIndicators, ownershipIndicators)
        elif (self.currentPos % 40) < 28:
            self.advanceToSquare(GameWindow, board, playerList, diceRoll, True, 28, houseIndicators, mortgageIndicators, ownershipIndicators)
        else:
            GameWindow.displayLabel2.setText(f"{self.name} passed Go, and collects £{moneyFromGo}.")
            self.addBalance(GameWindow, moneyFromGo)
            self.advanceToSquare(GameWindow, board, playerList, diceRoll, True, 12, houseIndicators, mortgageIndicators, ownershipIndicators)
    
    elif currentChance == 7:
        GameWindow.displayLabel2.setText(f"Advance to {board[39].cardName}")
        self.advanceToSquare(GameWindow, board, playerList, diceRoll, False, 39, houseIndicators, mortgageIndicators, ownershipIndicators)
    
    elif currentChance == 8:
        GameWindow.displayLabel2.setText(f"Advance to {board[24].cardName}. If you pass go, collect £{moneyFromGo}.")
        if (self.currentPos % 40) < 24:
            self.advanceToSquare(GameWindow, board, playerList, diceRoll, False, 24, houseIndicators, mortgageIndicators, ownershipIndicators)
        else:
            GameWindow.displayLabel2.setText(f"{self.name} passed Go, and collects £{moneyFromGo}.")
            self.addBalance(GameWindow, moneyFromGo)
            self.advanceToSquare(GameWindow, board, playerList, diceRoll, False, 24, houseIndicators, mortgageIndicators, ownershipIndicators)
    
    elif currentChance == 9:
        GameWindow.displayLabel2.setText(f"Advance to {board[11].cardName}. If you pass go, collect £{moneyFromGo}.")
        if (self.currentPos % 40) < 11:
            self.advanceToSquare(GameWindow, board, playerList, diceRoll, False, 11, houseIndicators, mortgageIndicators, ownershipIndicators)
        else:
            GameWindow.displayLabel2.setText(f"{self.name} passed Go, and collects £{moneyFromGo}.")
            self.addBalance(GameWindow, moneyFromGo)
            self.advanceToSquare(GameWindow, board, playerList, diceRoll, False, 11, houseIndicators, mortgageIndicators, ownershipIndicators)
    
    elif currentChance == 10:
        GameWindow.displayLabel2.setText("You've been caught speeding around the board. Pay a fine of £20.")
        self.reduceBalance(GameWindow, 20, playerList, houseIndicators, mortgageIndicators, ownershipIndicators)
    
    elif currentChance == 11:
        GameWindow.displayLabel2.setText("There was a bank error and you are being compensated. Collect £200.")
        self.addBalance(GameWindow, 200)

    elif currentChance == 12:
        GameWindow.displayLabel2.setText("Get out of jail free card (you can only hold one of these).")
        self.GOOJFC = True
    
    elif currentChance == 13:
        GameWindow.displayLabel2.setText("You sprained your wrist driving too hard and have to pay £100 of hospital fees.")
        self.reduceBalance(GameWindow, 100, playerList, houseIndicators, mortgageIndicators, ownershipIndicators)
    
    elif currentChance == 14:
        GameWindow.displayLabel2.setText("It's your birthday! Collect £20.")
        self.addBalance(GameWindow, 20)
    
    elif currentChance == 15:
        GameWindow.displayLabel2.setText("You broke down. Pay £100 for repairs.")
        self.reduceBalance(GameWindow, 100, playerList, houseIndicators, mortgageIndicators, ownershipIndicators)

    elif currentChance == 16:
        GameWindow.displayLabel2.setText("The tax man is hungry. Pay £15 for each house you own.")
        self.reduceBalance(GameWindow, self.housesOwned * 15, playerList, houseIndicators, mortgageIndicators, ownershipIndicators)

    
    chanceCounter += 1