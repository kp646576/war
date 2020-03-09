import os
import sys
import unittest
from copy import deepcopy
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from helper.config import *
from helper.suit import Suit
from helper.value import Value
from helper.card import Card
from helper.deck import Deck
from helper.player import Player
from helper.board import Board


class Tests(unittest.TestCase):
    def setUp(self):
        self.full_cards = [
            Card(Suit.DIAMONDS, Value.TWO),
            Card(Suit.DIAMONDS, Value.THREE),
            Card(Suit.DIAMONDS, Value.FOUR),
            Card(Suit.DIAMONDS, Value.FIVE),
            Card(Suit.DIAMONDS, Value.SIX),
            Card(Suit.DIAMONDS, Value.SEVEN),
            Card(Suit.DIAMONDS, Value.EIGHT),
            Card(Suit.DIAMONDS, Value.NINE),
            Card(Suit.DIAMONDS, Value.TEN),
            Card(Suit.DIAMONDS, Value.JACK),
            Card(Suit.DIAMONDS, Value.QUEEN),
            Card(Suit.DIAMONDS, Value.KING),
            Card(Suit.DIAMONDS, Value.ACE),
            Card(Suit.CLUBS, Value.TWO),
            Card(Suit.CLUBS, Value.THREE),
            Card(Suit.CLUBS, Value.FOUR),
            Card(Suit.CLUBS, Value.FIVE),
            Card(Suit.CLUBS, Value.SIX),
            Card(Suit.CLUBS, Value.SEVEN),
            Card(Suit.CLUBS, Value.EIGHT),
            Card(Suit.CLUBS, Value.NINE),
            Card(Suit.CLUBS, Value.TEN),
            Card(Suit.CLUBS, Value.JACK),
            Card(Suit.CLUBS, Value.QUEEN),
            Card(Suit.CLUBS, Value.KING),
            Card(Suit.CLUBS, Value.ACE),
            Card(Suit.HEARTS, Value.TWO),
            Card(Suit.HEARTS, Value.THREE),
            Card(Suit.HEARTS, Value.FOUR),
            Card(Suit.HEARTS, Value.FIVE),
            Card(Suit.HEARTS, Value.SIX),
            Card(Suit.HEARTS, Value.SEVEN),
            Card(Suit.HEARTS, Value.EIGHT),
            Card(Suit.HEARTS, Value.NINE),
            Card(Suit.HEARTS, Value.TEN),
            Card(Suit.HEARTS, Value.JACK),
            Card(Suit.HEARTS, Value.QUEEN),
            Card(Suit.HEARTS, Value.KING),
            Card(Suit.HEARTS, Value.ACE),
            Card(Suit.SPADES, Value.TWO),
            Card(Suit.SPADES, Value.THREE),
            Card(Suit.SPADES, Value.FOUR),
            Card(Suit.SPADES, Value.FIVE),
            Card(Suit.SPADES, Value.SIX),
            Card(Suit.SPADES, Value.SEVEN),
            Card(Suit.SPADES, Value.EIGHT),
            Card(Suit.SPADES, Value.NINE),
            Card(Suit.SPADES, Value.TEN),
            Card(Suit.SPADES, Value.JACK),
            Card(Suit.SPADES, Value.QUEEN),
            Card(Suit.SPADES, Value.KING),
            Card(Suit.SPADES, Value.ACE)
        ]

        self.subset_cards = [
            Card(Suit.DIAMONDS, Value.TWO),
            Card(Suit.DIAMONDS, Value.THREE),
            Card(Suit.DIAMONDS, Value.FOUR),
            Card(Suit.DIAMONDS, Value.FIVE),
            Card(Suit.DIAMONDS, Value.SIX),
            Card(Suit.DIAMONDS, Value.SEVEN),
            Card(Suit.DIAMONDS, Value.EIGHT),
            Card(Suit.DIAMONDS, Value.NINE),
            Card(Suit.DIAMONDS, Value.TEN),
            Card(Suit.DIAMONDS, Value.JACK),
            Card(Suit.DIAMONDS, Value.QUEEN),
            Card(Suit.DIAMONDS, Value.KING),
            Card(Suit.DIAMONDS, Value.ACE)
        ]

        self.card = Card(Suit.SPADES, Value.ACE)

        self.empty_deck = Deck(**{'cards': []})
        self.one_card_deck = Deck(**{'cards': [self.card]})
        self.full_deck = Deck(**{'cards': self.full_cards})
        self.subset_deck = Deck(**{'cards': self.subset_cards})

        self.player_empty = Player('Player ', self.empty_deck)
        self.player1 = Player('Player 1', self.subset_deck)

    # Board Test
    def test_b_last_4_war2(self):
        board = Board(self.empty_deck)

        player1 = board.players[0]
        player2 = board.players[1]

        player1.deck.cards = [
            Card(Suit.DIAMONDS, Value.TWO),
            Card(Suit.CLUBS, Value.TWO), 
        ]
        player1.spoils.cards = [
            Card(Suit.HEARTS, Value.TWO), 
            Card(Suit.SPADES, Value.TWO)
        ]

        player2.deck.cards = [
            Card(Suit.DIAMONDS, Value.THREE),
            Card(Suit.DIAMONDS, Value.FOUR),
            Card(Suit.DIAMONDS, Value.FIVE),
            Card(Suit.DIAMONDS, Value.SIX),
            Card(Suit.DIAMONDS, Value.SEVEN),
            Card(Suit.DIAMONDS, Value.EIGHT),
            Card(Suit.DIAMONDS, Value.NINE),
            Card(Suit.DIAMONDS, Value.TEN),
            Card(Suit.DIAMONDS, Value.JACK),
            Card(Suit.DIAMONDS, Value.QUEEN),
            Card(Suit.DIAMONDS, Value.KING),
            Card(Suit.DIAMONDS, Value.ACE),
            Card(Suit.CLUBS, Value.THREE),
            Card(Suit.CLUBS, Value.FOUR),
            Card(Suit.CLUBS, Value.FIVE),
            Card(Suit.CLUBS, Value.SIX),
            Card(Suit.CLUBS, Value.SEVEN),
            Card(Suit.CLUBS, Value.EIGHT),
            Card(Suit.CLUBS, Value.NINE),
            Card(Suit.CLUBS, Value.TEN),
            Card(Suit.CLUBS, Value.JACK),
            Card(Suit.CLUBS, Value.QUEEN),
            Card(Suit.CLUBS, Value.KING),
            Card(Suit.CLUBS, Value.ACE),
            Card(Suit.HEARTS, Value.THREE),
            Card(Suit.HEARTS, Value.FOUR),
            Card(Suit.HEARTS, Value.FIVE),
            Card(Suit.HEARTS, Value.SIX),
            Card(Suit.HEARTS, Value.SEVEN),
            Card(Suit.HEARTS, Value.EIGHT),
            Card(Suit.HEARTS, Value.NINE),
            Card(Suit.HEARTS, Value.TEN),
            Card(Suit.HEARTS, Value.JACK),
            Card(Suit.HEARTS, Value.QUEEN),
            Card(Suit.HEARTS, Value.KING)
        ]
        player2.spoils.cards = [
            Card(Suit.HEARTS, Value.ACE),
            Card(Suit.SPADES, Value.THREE),
            Card(Suit.SPADES, Value.FOUR),
            Card(Suit.SPADES, Value.FIVE),
            Card(Suit.SPADES, Value.SIX),
            Card(Suit.SPADES, Value.SEVEN),
            Card(Suit.SPADES, Value.EIGHT),
            Card(Suit.SPADES, Value.NINE),
            Card(Suit.SPADES, Value.TEN),
            Card(Suit.SPADES, Value.JACK),
            Card(Suit.SPADES, Value.QUEEN),
            Card(Suit.SPADES, Value.KING),
            Card(Suit.SPADES, Value.ACE)
        ]
        
        self.assertNotEqual(player1.deck.cards, [])
        self.assertGreater(player1.deck.size(), 0)
        self.assertNotEqual(player1.spoils.cards, [])
        self.assertGreaterEqual(player1.spoils.size(), 0)

        self.assertNotEqual(player2.deck.cards, [])
        self.assertGreater(player2.deck.size(), 0)
        self.assertNotEqual(player2.spoils.cards, [])
        self.assertGreater(player2.spoils.size(), 0)

        self.assertTrue(board._get_players_cards(True))

    def test_b_last_4_war(self):
        board = Board(self.empty_deck)

        player1 = board.players[0]
        player2 = board.players[1]

        player1.deck.cards = [
            Card(Suit.DIAMONDS, Value.TWO), 
            Card(Suit.CLUBS, Value.TWO), 
            Card(Suit.HEARTS, Value.TWO), 
            Card(Suit.SPADES, Value.TWO)
        ]
        player1.spoils.cards = []

        player2.deck.cards = [
            Card(Suit.DIAMONDS, Value.THREE),
            Card(Suit.DIAMONDS, Value.FOUR),
            Card(Suit.DIAMONDS, Value.FIVE),
            Card(Suit.DIAMONDS, Value.SIX),
            Card(Suit.DIAMONDS, Value.SEVEN),
            Card(Suit.DIAMONDS, Value.EIGHT),
            Card(Suit.DIAMONDS, Value.NINE),
            Card(Suit.DIAMONDS, Value.TEN),
            Card(Suit.DIAMONDS, Value.JACK),
            Card(Suit.DIAMONDS, Value.QUEEN),
            Card(Suit.DIAMONDS, Value.KING),
            Card(Suit.DIAMONDS, Value.ACE),
            Card(Suit.CLUBS, Value.THREE),
            Card(Suit.CLUBS, Value.FOUR),
            Card(Suit.CLUBS, Value.FIVE),
            Card(Suit.CLUBS, Value.SIX),
            Card(Suit.CLUBS, Value.SEVEN),
            Card(Suit.CLUBS, Value.EIGHT),
            Card(Suit.CLUBS, Value.NINE),
            Card(Suit.CLUBS, Value.TEN),
            Card(Suit.CLUBS, Value.JACK),
            Card(Suit.CLUBS, Value.QUEEN),
            Card(Suit.CLUBS, Value.KING),
            Card(Suit.CLUBS, Value.ACE),
            Card(Suit.HEARTS, Value.THREE),
            Card(Suit.HEARTS, Value.FOUR),
            Card(Suit.HEARTS, Value.FIVE),
            Card(Suit.HEARTS, Value.SIX),
            Card(Suit.HEARTS, Value.SEVEN),
            Card(Suit.HEARTS, Value.EIGHT),
            Card(Suit.HEARTS, Value.NINE),
            Card(Suit.HEARTS, Value.TEN),
            Card(Suit.HEARTS, Value.JACK),
            Card(Suit.HEARTS, Value.QUEEN),
            Card(Suit.HEARTS, Value.KING),
            Card(Suit.HEARTS, Value.ACE),
            Card(Suit.SPADES, Value.THREE),
            Card(Suit.SPADES, Value.FOUR),
            Card(Suit.SPADES, Value.FIVE),
            Card(Suit.SPADES, Value.SIX),
            Card(Suit.SPADES, Value.SEVEN),
            Card(Suit.SPADES, Value.EIGHT),
            Card(Suit.SPADES, Value.NINE),
            Card(Suit.SPADES, Value.TEN),
            Card(Suit.SPADES, Value.JACK),
            Card(Suit.SPADES, Value.QUEEN),
            Card(Suit.SPADES, Value.KING),
            Card(Suit.SPADES, Value.ACE)
        ]
        player2.spoils.cards = []
        
        self.assertNotEqual(player1.deck.cards, [])
        self.assertGreater(player1.deck.size(), 0)
        self.assertEqual(player1.spoils.cards, [])
        self.assertEqual(player1.spoils.size(), 0)
        self.assertNotEqual(player2.deck.cards, [])
        self.assertGreater(player2.deck.size(), 0)
        self.assertEqual(player2.spoils.cards, [])
        self.assertEqual(player2.spoils.size(), 0)

        self.assertTrue(board._get_players_cards(True))

    def test_b_create_players(self):
        board = Board(deepcopy(self.full_deck))
        cards = self.full_deck.cards
        offset = int(self.full_deck.size() / 2)
        count = 0

        for i, player in enumerate(board.players):
            for j, card in enumerate(player.deck.cards):
                self.assertEqual(type(card), Card)
                if card.value == cards[j+i*offset].value and card.suit == cards[j+i*offset].suit:
                    count += 1

            # test shuffle & number of cards in each players deck
            self.assertLess(count, player.deck.size())
            self.assertEqual(player.deck.size(), self.full_deck.size() / NUM_PLAYERS)

    # Player Tests
    def test_p_transfer_spoils(self):
        player = Player("P1", self.one_card_deck)
        card = Card(Suit.HEARTS, Value.ACE)
        player.spoils.cards = [card]

        self.assertNotEqual(player.deck.cards, [])
        self.assertGreater(player.deck.size(), 0)
        self.assertNotEqual(player.spoils.cards, [])
        self.assertGreater(player.spoils.size(), 0)

        draw_card = player.draw_card()
        self.assertEqual(draw_card, self.card)
        self.assertEqual(player.deck.cards, [])
        self.assertEqual(player.deck.size(), 0)
        self.assertNotEqual(player.spoils.cards, [])
        self.assertGreater(player.spoils.size(), 0)
        
        draw_card = player.draw_card()
        self.assertEqual(draw_card, card)
        self.assertEqual(player.deck.cards, [])
        self.assertEqual(player.deck.size(), 0)
        self.assertEqual(player.spoils.cards, [])
        self.assertEqual(player.spoils.size(), 0)

        draw_card = player.draw_card()
        self.assertEqual(player.deck.cards, [])
        self.assertEqual(player.deck.size(), 0)
        self.assertEqual(player.spoils.cards, [])
        self.assertEqual(player.spoils.size(), 0)
        self.assertEqual(draw_card, -1)

    def test_p_deck(self):
        top_card = self.player1.deck.cards[self.player1.deck.size()-1]
        drawn_card = self.player1.draw_card()
        spoils = self.player1.spoils

        self.assertEqual(drawn_card, top_card)
        self.assertTrue(type(drawn_card) == Card)

        self.assertEqual(spoils.size(), 0)
        self.assertEqual(spoils.cards, [])

    def test_p_empty_deck(self):
        drawn_card = self.player_empty.draw_card()
        spoils = self.player_empty.spoils

        self.assertEqual(drawn_card, -1)
        self.assertTrue(type(drawn_card) == int)

        self.assertEqual(spoils.size(), 0)
        self.assertEqual(spoils.cards, [])

    # Deck Tests
    def test_d_transfer(self):
        deck1 = Deck().build()
        deck2 = Deck().build()
        cards = self.full_deck.cards + self.full_deck.cards

        deck1.transfer(deck2)
        for index, card in enumerate(deck1.cards):
            self.assertEqual(card.suit.value, cards[index].suit.value)
            self.assertEqual(card.value.value, cards[index].value.value)
        self.assertEqual(deck2.cards, [])

    def test_d_shuffle(self):
        pre_shuffle = []
        count = 0

        deck = Deck().build()

        for c in deck.cards:
            pre_shuffle.append(c)

        deck.shuffle()

        for i, c in enumerate(deck.cards):
            if c.value == pre_shuffle[i].value and c.suit == pre_shuffle[i].suit:
                count += 1

        self.assertLess(count, len(deck.cards))

    def test_d_empty_shuffle(self):
        deck = self.empty_deck
        exception = False

        self.assertEqual(deck.cards, [])
        self.assertEqual(deck.size(), 0)
        try:
            deck.shuffle()
        except:
            exception = True
        self.assertFalse(exception)

    def test_d_build(self):
        deck = Deck().build()
        for index, card in enumerate(deck.cards):
            self.assertEqual(card.suit.value, self.full_cards[index].suit.value)
            self.assertEqual(card.value.value, self.full_cards[index].value.value)
        self.assertEqual(deck.size(), len(self.full_cards))

    def test_d_build_with_cards(self):
        for index, card in enumerate(self.subset_deck.cards):
            self.assertEqual(card.suit.value, self.subset_cards[index].suit.value)
            self.assertEqual(card.value.value, self.subset_cards[index].value.value)
        self.assertEqual(self.subset_deck.size(), len(self.subset_cards))

    def test_d_empty(self):
        self.assertEqual(self.empty_deck.cards, [])
        self.assertEqual(self.empty_deck.size(), 0)

if __name__ == '__main__':
    unittest.main()