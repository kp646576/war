# War

Python 3 implementation of popular card game titled [War](https://en.wikipedia.org/wiki/War_(card_game)).

## Rules

* Each player is given half of the cards in the starting deck
* Each player begins by drawing and revealing the top card in their deck
* The player with the highest card wins the round and takes both cards
* In the case of a tie (same value card, suits are ignored) "War" is initiated
* In "War" each player draws the top 3 cards of their card face down and reveal the 4th card
* The player with the highest 4th card is the winner and takes all of the cards
* In the case of another tie "War" is reinitiated
* This process continues until one player has all of the cards in the starting deck

## Game Details

1. 2 Player Game
2. Aces are high (highest value in game)
2. Standard 52 card deck without Jokers/Wilds
5. If a player runs out of cards, their winning stack will be added back to their deck
6. If a player draws their last card while milling during "War", that player automatically loses
7. Game will automatically be played out until one player wins
