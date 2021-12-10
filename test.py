import numpy as np
deck = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
suit = ["Spades", "Hearts", "Clubs", "Diamonds"]

picked = []
for x in range(2):
    firstCard = np.random.choice(deck) + " " + np.random.choice(suit)
    while firstCard in picked:
        firstCard = np.random.choice(deck) + " " + np.random.choice(suit)
    picked.append(firstCard)

#print(picked)