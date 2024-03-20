def drawChance(self, board, playerList, diceRoll, chanceCounter, randomList, moneyFromGo, fastBankruptcy, rentFromJail):

    currentChance = randomList[chanceCounter % len(randomList)]

    if currentChance == 0:
        print("Oh no, your friend is asking for a loan from you. Pay £50.")
        self.reduceBalance(50)

    elif currentChance == 1:
        print(f"Move directly to Go! Collect £{moneyFromGo}.")
        self.currentPos = 0
        self.addBalance(moneyFromGo)

    elif currentChance == 2:
        print("You win a local raffle and sell the highest prize. Gain £100.")
        self.addBalance(100)

    elif currentChance == 3:
        print("Ouch! You drove into a lampost and have to fix your car. Go back three spaces.")
        self.currentPos = (self.currentPos - 3) % 40
        self.checkPosition(board, playerList, diceRoll, chanceCounter, randomList, moneyFromGo, fastBankruptcy, rentFromJail)

    elif currentChance == 4:
        print(f"Move directly to jail. You may not pass go, or collect £{moneyFromGo}.")
        self.sendToJail()

    elif currentChance == 5:
        print("Advance to the nearest travel square. You may buy it if unowned, but must pay double the normal rent if owned.")
        if (self.currentPos % 40) < 5:
            self.advanceToSquare(board, playerList, diceRoll, True, 5)
        elif (self.currentPos % 40) < 15:
            self.advanceToSquare(board, playerList, diceRoll, True, 15)
        elif (self.currentPos % 40) < 25:
            self.advanceToSquare(board, playerList, diceRoll, True, 25)
        elif (self.currentPos % 40) < 35:
            self.advanceToSquare(board, playerList, diceRoll, True, 35)
        else:
            print(f"{self.name} passed Go, and collects £{moneyFromGo}.")
            self.addBalance(moneyFromGo)
            self.advanceToSquare(board, playerList, diceRoll, True, 5)
    
    elif currentChance == 6:
        print("Advance to the nearest utility. You may buy it if unowned, but must pay double the normal rent if owned.")
        if (self.currentPos % 40) < 12:
            self.advanceToSquare(board, playerList, diceRoll, True, 12)
        elif (self.currentPos % 40) < 28:
            self.advanceToSquare(board, playerList, diceRoll, True, 28)
        else:
            print(f"{self.name} passed Go, and collects £{moneyFromGo}.")
            self.addBalance(moneyFromGo)
            self.advanceToSquare(board, playerList, diceRoll, True, 12)
    
    elif currentChance == 7:
        print(f"Advance to {board[39].cardName}")
        self.advanceToSquare(board, playerList, diceRoll, False, 39)
    
    elif currentChance == 8:
        print(f"Advance to {board[24].cardName}. If you pass go, collect £{moneyFromGo}.")
        if (self.currentPos % 40) < 24:
            self.advanceToSquare(board, playerList, diceRoll, False, 24)
        else:
            print(f"{self.name} passed Go, and collects £{moneyFromGo}.")
            self.addBalance(moneyFromGo)
            self.advanceToSquare(board, playerList, diceRoll, False, 24)
    
    elif currentChance == 9:
        print(f"Advance to {board[11].cardName}. If you pass go, collect £{moneyFromGo}.")
        if (self.currentPos % 40) < 11:
            self.advanceToSquare(board, playerList, diceRoll, False, 11)
        else:
            print(f"{self.name} passed Go, and collects £{moneyFromGo}.")
            self.addBalance(moneyFromGo)
            self.advanceToSquare(board, playerList, diceRoll, False, 11)
    
    elif currentChance == 10:
        print("You've been caught speeding around the board. Pay a fine of £20.")
        self.reduceBalance(20)
    
    elif currentChance == 11:
        print("There was a bank error and you are being compensated. Collect £200.")
        self.addBalance(200)

    elif currentChance == 12:
        print("Get out of jail free card (you can only hold one of these).")
        self.GOOJFC = True
    
    elif currentChance == 13:
        print("You sprained your wrist driving too hard and have to pay £100 of hospital fees.")
        self.reduceBalance(100)
    
    elif currentChance == 14:
        print("It's your birthday! Collect £20.")
        self.addBalance(20)
    
    elif currentChance == 15:
        print("You broke down. Pay £100 for repairs.")
        self.reduceBalance(100)

    elif currentChance == 16:
        print("The tax man is hungry. Pay £15 for each house you own.")
        self.reduceBalance(self.housesOwned * 15)

    
    chanceCounter += 1
    return chanceCounter