from random import randint
from .suit import Suit
from .value import Value
from .card import Card

class Deck:
    # Deck is used for both the starting deck and each player's deck
    def __init__(self, *args, **kwargs):
        self.cards = kwargs.get('cards', [])

    def build(self):
        for suit in Suit:
            for value in Value:
                self.cards.append( Card(suit, value) )
        return self

    # Fisher–Yates Shuffle Algorithm
    # https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle
    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            j = randint(0, i)
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]