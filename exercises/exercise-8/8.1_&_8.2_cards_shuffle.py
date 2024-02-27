#52 card deck

suites = ['hearts', 'diamonds', 'spades', 'clubs']
values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

deck = [[v + ' of ' + s] for v in values for s in suites]

print(*deck, sep= "\n")

# 8.2 

import random

def shuffle():
    random.shuffle(deck)
    return deck

print(shuffle())