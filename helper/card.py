class Card:
    """
    @type  suit: Enum<Suit>
    @param suit: Card suit

    @type  value: Enum<Value>
    @param value: Card value
    """
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value