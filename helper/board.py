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

    def _continue_game(self):
        cards_in_play = len(self._round_cards) + len(self._round_spoils)
        for p in self.players:
            if p.spoils.size() + len(p.deck.cards) + cards_in_play == NUM_CARDS_IN_DECK * NUM_DECKS:
                print('Player: ' + p.name + ' is the winner!')
                return False
        return True

    # used for combining cards
    def _get_round_cards(self, round_cards):
        return [rc[1] for rc in round_cards]

    def _get_players_cards(self, is_war):
        if is_war:
            print('----------THIS IS WAR----------')
            for p in self.players:
                for i in range(0, MILL_COUNT):
                    draw_card = p.draw_card()

                    if draw_card == -1:
                        self._continue_game()
                        return False
                    # Last card drawn, put card back in deck to use as round card
                    # elif p.deck.size() == 0:
                    #     p.deck.cards.append(draw_card)
                    #     break
                    else:
                        self._round_spoils.append(draw_card)

        # Add cards to card pool to be evaluated
        for p in self.players:
            draw_card = p.draw_card()

            if draw_card == -1:
                self._continue_game()
                print(p.name, ' couldn\'t draw?')
                return False
            else:
                self._round_cards.append((p, draw_card))

        print('FACEOFF')
        print('round_cards: ', len(self._round_cards), 'round_spoils: ', len(self._round_spoils))
        for rc in self._round_cards:
            print(rc[0].name, rc[1].suit.value, rc[1].value.value, 'deck: {}'.format(rc[0].deck.size()), 'spoils: {}'.format(rc[0].spoils.size()))

        return True

    # sorted_cards = [(Player, Card), ...]
    def _check_dups(self, sorted_cards):
        highest = sorted_cards[0][1].value.value
        dups = [sorted_cards[0]]
        for i in range(1, len(self.players)):
            if sorted_cards[i][1].value.value == highest:
                dups.append(sorted_cards[i])
        return dups

    def play_round(self, is_war):
        # End the game if player won
        if not self._get_players_cards(is_war):
            return False

        # Sort cards in play in reverse order (highest cards in the front)
        # self._round_cards = [(Player, Card), ...]
        sorted_cards = sorted(self._round_cards, key=lambda card: card[1].value.value, reverse=True)

        # Check all players for tie with highest card
        # dups = [(Player, Card), ...]
        dups = self._check_dups(sorted_cards)

        # Initiate "War" or determine round winner and start next round
        if len(dups) > 1: 
            self._round_spoils += self._get_round_cards(self._round_cards)
            self._round_cards = []
            return self.play_round(True)
        else:
            winner = dups[0]
            winner[0].spoils.cards += (self._round_spoils + self._get_round_cards(self._round_cards))
            self._round_cards = []
            self._round_spoils = []
            print('ROUND WINNER is PLAYER: ', winner[0].name)
            return self._continue_game()

    def play(self):
        play = True
        count = 1
        while play:
            print('ROUND: ', count)
            play = self.play_round(False)
            count += 1