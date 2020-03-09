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
        if self.deck.size() == 0:
            self.deck.transfer(self.spoils)
            # Shuffle deck after transfer to reduce likelihood of cyclic formations
            self.deck.shuffle()

        if self.deck.size() > 0:
            return self.deck.cards.pop()
        else:
            return -1