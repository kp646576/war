from .deck import Deck

class Player:
    """
    @type name: str
    @param name: Player name

    @type deck: Deck
    @param deck: Player's deck (subset of starting deck)

    @type spoils: Deck
    @param spoils: Player's won deck of cards (initially empty)
    """
    def __init__(self, name, deck):
        self.name = name
        self.deck = deck
        self.spoils = Deck()

    def draw_card(self):
        if len(self.deck.cards) > 0:
            return self.deck.cards.pop()
        else:
            return -1