import Classes.card as Cards

## cost, cardName, cardSet, houseCost, housesBuilt, mortgaged, mortgageCost, ownerID, owner, rentAmounts. For ownerID, Bank is 0

def defaultCardsAndBoard():
    go = Cards.Card("N/A", "Go", "N/A", "N/A", "N/A", False, "N/A", "Bank", "0", "N/A")
    freeParking = Cards.Card("N/A", "Free Parking", "N/A", "N/A", "N/A", False, "N/A", "Bank", "0", "N/A")
    chance = Cards.Card("N/A", "Chance", "N/A", "N/A", "N/A", False, "N/A", "Bank", "0", "N/A")
    incomeTax = Cards.Card("N/A", "Income Tax", "N/A", "N/A", "N/A", False, "N/A", "Bank", "0", "N/A")
    luxuryTax = Cards.Card("N/A", "Luxury Tax", "N/A", "N/A", "N/A", False, "N/A", "Bank", "0", "N/A")
    jail = Cards.Card("N/A", "Jail", "N/A", "N/A", "N/A", False, "N/A", "Bank", "0", "N/A")
    goToJail = Cards.Card("N/A", "Go To Jail", "N/A", "N/A", "N/A", False, "N/A", "Bank", "0", "N/A")

    rr1 = Cards.Card(200, "Zebra Crossing", "Railroad", "N/A", "N/A", False, 100, "Bank", "0", "N/A")
    rr2 = Cards.Card(200, "Snail Trail", "Railroad", "N/A", "N/A", False, 100, "Bank", "0", "N/A")
    rr3 = Cards.Card(200, "Raccoon Railway", "Railroad", "N/A", "N/A", False, 100, "Bank", "0", "N/A")
    rr4 = Cards.Card(200, "Panda Express", "Railroad", "N/A", "N/A", False, 100, "Bank", "0", "N/A")

    u1 = Cards.Card(150, "Eel Electric", "Utility", "N/A", "N/A", False, 75, "Bank", "0", "N/A")
    u2 = Cards.Card(150, "Turtle Taps", "Utility", "N/A", "N/A", False, 75, "Bank", "0", "N/A")

    brown1 = Cards.Card(60, "Skunk Street", "Brown", 50, 0, False, 30, "Bank", "0", {0: 2, 1: 10, 2: 30, 3: 90, 4: 160, 5: 250})
    brown2 = Cards.Card(60, "Squirrel Square", "Brown", 50, 0, False, 30, "Bank", "0", {0: 4, 1: 20, 2: 60, 3: 180, 4: 320, 5: 450})

    lBlue1 = Cards.Card(100, "Phoenix Heights", "Light Blue", 50, 0, False , 50, "Bank", "0", {0: 6, 1: 30, 2: 90, 3: 270, 4: 400, 5: 550})
    lBlue2 = Cards.Card(100, "Pigeon Street", "Light Blue", 50, 0, False , 50, "Bank", "0", {0: 6, 1: 30, 2: 90, 3: 270, 4: 400, 5: 550})
    lBlue3 = Cards.Card(120, "Polar Bear Park", "Light Blue", 50, 0, False, 60, "Bank", "0", {0: 4, 1: 20, 2: 60, 3: 180, 4: 320, 5: 450})

    pink1 = Cards.Card(140, "Monkey Mall", "Pink", 100, 0, False, 70, "Bank", "0", {0: 10, 1: 50, 2: 150, 3: 450, 4: 625, 5: 750})
    pink2 = Cards.Card(140, "Hedgehog Lane", "Pink", 100, 0, False, 70, "Bank", "0", {0: 10, 1: 50, 2: 150, 3: 450, 4: 625, 5: 750})
    pink3 = Cards.Card(160, "Marmoset Meadows", "Pink", 100, 0, False, 80, "Bank", "0", {0: 12, 1: 60, 2: 180, 3: 500, 4: 700, 5: 900})

    orange1 = Cards.Card(180, "Llama Lane", "Orange", 100, 0, False, 90, "Bank", "0", {0: 14, 1: 70, 2: 200, 3: 550, 4: 750, 5: 950})
    orange2 = Cards.Card(180, "Penguin Place", "Orange", 100, 0, False, 90, "Bank", "0", {0: 14, 1: 70, 2: 200, 3: 550, 4: 750, 5: 950})
    orange3 = Cards.Card(200, "Kangaroo Court", "Orange", 100, 0, False, 100, "Bank", "0", {0: 16, 1: 80, 2: 220, 3: 600, 4: 800, 5: 1000})

    red1 = Cards.Card(220, "The Albatross Inn", "Red", 150, 0, False, 110, "Bank", "0", {0: 18, 1: 90, 2: 250, 3: 700, 4: 875, 5: 1050})
    red2 = Cards.Card(220, "Owl Oasis", "Red", 150, 0, False, 110, "Bank", "0", {0: 18, 1: 90, 2: 250, 3: 700, 4: 875, 5: 1050})
    red3 = Cards.Card(240, "Parakeet Plaza", "Red", 150, 0, False, 120, "Bank", "0", {0: 20, 1: 100, 2: 300, 3: 750, 4: 925, 5: 1100})

    yellow1 = Cards.Card(260, "Tiger Trail", "Yellow", 150, 0, False, 130, "Bank", "0", {0: 22, 1: 110, 2: 330, 3: 800, 4: 975, 5: 1150})
    yellow2 = Cards.Card(260, "Iguana Island", "Yellow", 150, 0, False, 130, "Bank", "0", {0: 22, 1: 110, 2: 330, 3: 800, 4: 975, 5: 1150})
    yellow3 = Cards.Card(280, "Vulture Valley", "Yellow", 150, 0, False, 140, "Bank", "0", {0: 24, 1: 120, 2: 360, 3: 850, 4: 1025, 5: 1200})

    green1 = Cards.Card(300, "Alligator Alley", "Green", 200, 0, False, 130, "Bank", "0", {0: 26, 1: 130, 2: 390, 3: 900, 4: 1100, 5: 1275})
    green2 = Cards.Card(300, "Seal Shores", "Green", 200, 0, False, 130, "Bank", "0", {0: 26, 1: 130, 2: 390, 3: 900, 4: 1100, 5: 1275})
    green3 = Cards.Card(320, "Peacock Promenade", "Green", 200, 0, False, 140, "Bank", "0", {0: 28, 1: 150, 2: 450, 3: 1000, 4: 1200, 5: 1400})

    dBlue1 = Cards.Card(350, "Whale Way", "Dark Blue", 200, 0, False, 130, "Bank", "0", {0: 35, 1: 175, 2: 500, 3: 1100, 4: 1300, 5: 1500})
    dBlue2 = Cards.Card(400, "Elephant Avenue", "Dark Blue", 200, 0, False, 130, "Bank", "0", {0: 50, 1: 200, 2: 600, 3: 1400, 4: 1700, 5: 2000})

    board = [
        go,
        brown1,
        chance,
        brown2,
        incomeTax,
        rr1,
        lBlue1,
        chance,
        lBlue2,
        lBlue3,
        jail,
        pink1,
        u1,
        pink2,
        pink3,
        rr2,
        orange1,
        chance,
        orange2,
        orange3,
        freeParking,
        red1,
        chance,
        red2,
        red3,
        rr3,
        yellow1,
        yellow2,
        u2,
        yellow3,
        goToJail,
        green1,
        green2,
        chance,
        green3,
        rr4,
        chance,
        dBlue1,
        luxuryTax,
        dBlue2
    ]

    return board

board = defaultCardsAndBoard()