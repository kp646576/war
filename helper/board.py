from .config import *
from .suit import Suit
from .value import Value
from .card import Card
from .deck import Deck
from .player import Player


class Board:
    def __init__(self, deck=Deck().build(), num_players=NUM_PLAYERS):
        self.game_deck = deck
        self.game_deck.shuffle()
        self.players = []
        self._create_players(num_players)

        self._round_cards = []
        self._round_spoils = []

        print('PRINTING PLAYERS')
        for p in self.players:
            print(p.name, p.deck.size())
    
    def _create_players(self, num_players):
        num_player_cards = int(self.game_deck.size() / num_players)
        for i in range(0, num_players):
            start = i * num_player_cards
            end = (i+1) * num_player_cards

            player_deck = Deck(**{'cards': self.game_deck.cards[start:end]})
            self.players.append(Player('P{}'.format(i+1), player_deck))