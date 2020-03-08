import os
import sys
import unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from helper.suit import Suit
from helper.value import Value
from helper.card import Card
from helper.deck import Deck


class Tests(unittest.TestCase):

    # Deck Tests
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

    def test_d_build(self):
        cards = [
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

        deck = Deck().build()
        for index, card in enumerate(deck.cards):
            self.assertEqual(card.suit.value, cards[index].suit.value)
            self.assertEqual(card.value.value, cards[index].value.value)

    def test_d_build_with_cards(self):
        cards = [
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
        
        deck = Deck(None, **{'cards': cards})

        for index, card in enumerate(deck.cards):
            self.assertEqual(card.suit.value, cards[index].suit.value)
            self.assertEqual(card.value.value, cards[index].value.value)

    def test_d_empty(self):
        self.assertEqual(Deck().cards, [])

if __name__ == '__main__':
    unittest.main()