from random import randint
from .suit import Suit
from .value import Value
from .card import Card

class Deck:
    """
    @type  cards: Array<Card>
    @param cards: List of cards for either the starting deck or player's deck
    """
    def __init__(self, **kwargs):
        self.cards = kwargs.get('cards', [])

    def build(self):
        for suit in Suit:
            for value in Value:
                self.cards.append( Card(suit, value) )
        return self

    def size(self):
        return len(self.cards)

    # Fisher–Yates Shuffle Algorithm
    # https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle
    def shuffle(self):
        for i in range(self.size()-1, 0, -1):
            j = randint(0, i)
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]

    """
    @type other_deck: Deck
    @param other_deck: Appends cards from other_deck to this deck and
                       empties cards from other_deck
    """
    def transfer(self, other_deck):
        self.cards += other_deck.cards
        other_deck.cards = []
            