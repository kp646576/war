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
    
    def __eq__(self, other):
        if isinstance(other, Card):
            return self.suit == other.suit and self.value == other.value
        return False

    def __gt__(self, other):
        if isinstance(other, Card):
            return self.value.value > other.value.value
        return False