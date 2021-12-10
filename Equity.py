import numpy as np
import itertools

def build_deck():
    numbers = list(range(2, 15))
    suits = ['H', 'S', 'C', 'D']
    deck = []
    for i in numbers:
        for s in suits:
            card = s+str(i)
            deck.append(card)
    return deck

def combinations(arr, n):
    arr = np.asaray(arr)
    t = np.dtype([('', arr.dtype)]*n)
    result = np.fromiter(itertools.combinations(arr, n), t)
    return result.view(arr.dtype).reshape(-1, n)
