import Classes.card as Cards

## cost, cardName, cardSet, houseCost, housesBuilt, mortgageCost, rentAmounts

def defaultCardsAndBoard():
    go = Cards.Card("N/A", "Go", "N/A", "N/A", "N/A", "N/A", "N/A")
    freeParking = Cards.Card("N/A", "Free Parking", "N/A", "N/A", "N/A", "N/A", "N/A")
    chance = Cards.Card("N/A", "Chance", "N/A", "N/A", "N/A", "N/A", "N/A")
    incomeTax = Cards.Card("N/A", "Income Tax", "N/A", "N/A", "N/A", "N/A", "N/A")
    luxuryTax = Cards.Card("N/A", "Luxury Tax", "N/A", "N/A", "N/A", "N/A", "N/A")
    jail = Cards.Card("N/A", "Jail", "N/A", "N/A", "N/A", "N/A", "N/A")
    goToJail = Cards.Card("N/A", "Go To Jail", "N/A", "N/A", "N/A", "N/A", "N/A")

    rr1 = Cards.Card(200, "Zebra Crossing", "Travel Square", "N/A", "N/A", 100, "N/A")
    rr2 = Cards.Card(200, "Snail Trail", "Travel Square", "N/A", "N/A", 100, "N/A")
    rr3 = Cards.Card(200, "Raccoon Railway", "Travel Square", "N/A", "N/A", 100, "N/A")
    rr4 = Cards.Card(200, "Panda Express", "Travel Square", "N/A", "N/A", 100, "N/A")

    u1 = Cards.Card(150, "Eel Electric", "Utility", "N/A", "N/A", 75, "N/A")
    u2 = Cards.Card(150, "Turtle Taps", "Utility", "N/A", "N/A", 75, "N/A")

    brown1 = Cards.Card(60, "Skunk Street", "Brown", 50, 0, 30, [2, 10, 30, 90, 160, 250])
    brown2 = Cards.Card(60, "Squirrel Square", "Brown", 50, 0, 30, [4, 20, 60, 180, 320, 450])

    lBlue1 = Cards.Card(100, "Phoenix Heights", "Light Blue", 50, 0, 50, [6, 30, 90, 270, 400, 550])
    lBlue2 = Cards.Card(100, "Pigeon Street", "Light Blue", 50, 0, 50, [6, 30, 90, 270, 400, 550])
    lBlue3 = Cards.Card(120, "Polar Bear Park", "Light Blue", 50, 0, 60, [4, 20, 60, 180, 320, 450])

    pink1 = Cards.Card(140, "Monkey Mall", "Pink", 100, 0, 70, [10, 50, 150, 450, 625, 750])
    pink2 = Cards.Card(140, "Hedgehog Lane", "Pink", 100, 0, 70, [10, 50, 150, 450, 625, 750])
    pink3 = Cards.Card(160, "Marmoset Meadows", "Pink", 100, 0, 80, [12, 60, 180, 500, 700, 900])

    orange1 = Cards.Card(180, "Llama Lane", "Orange", 100, 0, 90, [14, 70, 200, 550, 750, 950])
    orange2 = Cards.Card(180, "Penguin Place", "Orange", 100, 0, 90, [14, 70, 200, 550, 750, 950])
    orange3 = Cards.Card(200, "Kangaroo Court", "Orange", 100, 0, 100, [16, 80, 220, 600, 800, 1000])

    red1 = Cards.Card(220, "The Albatross Inn", "Red", 150, 0, 110, [18, 90, 250, 700, 875, 1050])
    red2 = Cards.Card(220, "Owl Oasis", "Red", 150, 0, 110, [18, 90, 250, 700, 875, 1050])
    red3 = Cards.Card(240, "Parakeet Plaza", "Red", 150, 0, 120, [20, 100, 300, 750, 925, 1100])

    yellow1 = Cards.Card(260, "Tiger Trail", "Yellow", 150, 0, 130, [22, 110, 330, 800, 975, 1150])
    yellow2 = Cards.Card(260, "Iguana Island", "Yellow", 150, 0, 130, [22, 110, 330, 800, 975, 1150])
    yellow3 = Cards.Card(280, "Vulture Valley", "Yellow", 150, 0, 140, [24, 120, 360, 850, 1025, 1200])

    green1 = Cards.Card(300, "Alligator Alley", "Green", 200, 0, 130, [26, 130, 390, 900, 1100, 1275])
    green2 = Cards.Card(300, "Seal Shores", "Green", 200, 0, 130, [26, 130, 390, 900, 1100, 1275])
    green3 = Cards.Card(320, "Peacock Promenade", "Green", 200, 0, 140, [28, 150, 450, 1000, 1200, 1400])

    dBlue1 = Cards.Card(350, "Whale Way", "Dark Blue", 200, 0, 130, [35, 175, 500, 1100, 1300, 1500])
    dBlue2 = Cards.Card(400, "Elephant Avenue", "Dark Blue", 200, 0, 130, [50, 200, 600, 1400, 1700, 2000])

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
