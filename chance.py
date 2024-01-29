def drawChance(self, board, playerList, diceRoll, chanceCounter):

    currentChance = chanceCounter % (4)
    if currentChance == 0:
        print("Oh no, your friend is asking for a loan from you. Pay $50.")
        self.reduceBalance(50)
    elif currentChance == 1:
        print("Move directly to Go! Collect $200.")
        self.currentPos = 0
        self.addBalance(200)
    elif currentChance == 2:
        print("You win a local raffle and sell the highest prize. Gain $100.")
        self.addBalance(100)
    elif currentChance == 3:
        print("Ouch! You drove into a lampost and have to fix your car. Go back three spaces.")
        self.currentPos = (self.currentPos - 3) % 40
        self.checkPosition(board, playerList, diceRoll, chanceCounter)
    
    chanceCounter += 1
    print(chanceCounter)
    return chanceCounter