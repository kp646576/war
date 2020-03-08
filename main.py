from random import randint
from helper.card import Card
from helper.suit import Suit
from helper.value import Value

# Driver for War Card Game
def main():
     for suit in Suit:
            for value in Value:
                print('Card(' + str(suit) + ', ' + str(value) + '),')
if __name__ == "__main__":
    main()