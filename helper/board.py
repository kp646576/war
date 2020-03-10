from .config import *
from .suit import Suit
from .value import Value
from .card import Card
from .deck import Deck
from .player import Player


class Board:
    """
    @type  deck: Deck
    @param deck: Standard 52 card deck used in the game

    @type  num_players: int
    @param num_players: Number of players to create in the game
    """
    def __init__(self, deck=Deck().build(), num_players=NUM_PLAYERS):
        self._game_deck = deck
        self._game_deck.shuffle()
        self._players = []
        self._create_players(num_players)

        self._round_cards = []
        self._round_spoils = []

        print('PRINTING PLAYERS')
        for p in self._players:
            print(p.name, p.deck.size())
    
    def _create_players(self, num_players):
        num_player_cards = int(self._game_deck.size() / num_players)
        for i in range(0, num_players):
            start = i * num_player_cards
            end = (i+1) * num_player_cards

            player_deck = Deck(**{'cards': self._game_deck.cards[start:end]})
            self._players.append(Player('P{}'.format(i+1), player_deck))

    def _continue_game(self):
        cards_in_play = len(self._round_cards) + len(self._round_spoils)
        for p in self._players:
            if p.spoils.size() + len(p.deck.cards) + cards_in_play == NUM_CARDS_IN_DECK * NUM_DECKS:
                print('Player: ' + p.name + ' is the winner!')
                return False
        return True

    # Convenience function used for aggregating cards
    def _get_round_cards(self, round_cards):
        return [rc[1] for rc in round_cards]

    def _get_players_cards(self, is_war):
        if is_war:
            print('----------THIS IS WAR----------')
            for p in self._players:
                for i in range(0, MILL_COUNT):
                    draw_card = p.draw_card()

                    if draw_card == -1:
                        return self._continue_game()
                    # Last card drawn, put card back in deck to use as round card
                    # elif p.deck.size() == 0:
                    #     p.deck.cards.append(draw_card)
                    #     break
                    else:
                        self._round_spoils.append(draw_card)

        # Add cards to card pool to be evaluated
        for p in self._players:
            draw_card = p.draw_card()

            if draw_card == -1:
                return self._continue_game()
            else:
                self._round_cards.append((p, draw_card))

        print('FACEOFF')
        player_card_count = 0
        for rc in self._round_cards:
            player_card_count += rc[0].deck.size() + rc[0].spoils.size()
            print(rc[0].name, rc[1].suit.value, rc[1].value.value, 'deck: ', rc[0].deck.size(), 'spoils: ', rc[0].spoils.size())
        print('round_cards: ', len(self._round_cards), 'round_spoils: ', len(self._round_spoils), 'total_cards: ', len(self._round_cards) + len(self._round_spoils) + player_card_count)
        return True

    # round_cards = [(Player, Card), ...]
    def _check_dups(self, highest_val, round_cards):
        dups = []
        for i in range(0, len(round_cards)):
            if round_cards[i][1].value.value == highest_val:
                dups.append(round_cards[i])
        return dups

    def play_round(self, is_war):
        # End the game if player won
        if not self._get_players_cards(is_war):
            return False

        # Get the highes card in the list
        # self._round_cards = [(Player, Card), ...]
        # highest_card = Card
        highest_card = max(self._round_cards, key=lambda card: card[1].value.value)

        # Check all players for tie with highest card
        # dups = [(Player, Card), ...]
        dups = self._check_dups(highest_card[1].value.value, self._round_cards)

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
            if count > MAX_ROUND:
                print('---------- MAX ROUND REACHED, GAME IS A TIE!!! ----------')
                break
            print('ROUND: ', count)
            play = self.play_round(False)
            count += 1
        return count