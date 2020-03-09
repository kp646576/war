from .suit import Suit
from .value import Value

NUM_PLAYERS = 2
NUM_DECKS = 1
NUM_CARDS_IN_DECK = len(Suit) * len(Value)
# Number of cards removed from top of deck for each player during "War"
MILL_COUNT = 3