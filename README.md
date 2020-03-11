# War

Python 3 implementation of popular card game titled [War](https://en.wikipedia.org/wiki/War_(card_game)).

## Running Project

All tests and development were done on Python 3.7.4

### Run Game
In project root 

``` python3 main.py ```

### Run Tests
In tests folder

``` python3 unittests.py ```

## Rules

* Each player is given half of the cards in the starting deck
* Each player begins by drawing and revealing the top card in their deck
* The player with the highest card wins the round and takes both cards
* In the case of a tie (same value card, suits are ignored) "War" is initiated
* In "War" each player draws the top 3 cards of their card face down and reveal the 4th card
* The player with the highest 4th card is the winner and takes all of the cards
* In the case of another tie "War" is reinitiated
* This process continues until one player has all of the cards in the starting deck

## Game Details (Assumptions)

1. 2 Player Game
2. Aces are high (highest value in game)
2. Played with 1 standard deck comprised of 52 cards without Jokers/Wilds
5. If a player runs out of cards, their winning stack will be added back to their deck and reshuffled (this is to reduce the likelihood of cyclic formations and infinite/seemingly games)
6. If a player draws their last card while removing cards during "War", that player automatically loses
7. Game will automatically be played out until:

	1. A player wins
	2. The maximum number of game rounds has been reached (by default this value is set to 1,000)

## Improvements (Given More Time)

### Game Mechanics
* Research more into the mathematics behind the game of "War" to determine cyclic formations to end the game as a tie once detected
* Implement the game with different rules and analyze the impact of those changes through methods such as:
	* Immediately adding cards back into deck upon winning
	* Different shuffling algorithms
	* Allowing player to use the last card they drew during war instead of automatically losing if they do not have enough cards

### User Experience
* Implment GUI using a framework like PyQt to make the game more interactive
* Allow user to draw cards and allow options for two people to play the game
* Add ability to set/change player name

### Testing
* Setup coninuous integration tool like Travis CI/ Jenkins to streamline testing process
* Utilize more testing resources such as mock and hypothesis in unittest for scalable testing

### Other
* Research more into Python packages that can be incorporated into the project to simplify code
* Resarch more into venv to consolidate all packages/dependencies within the project

## Reflection

Initially tried to implement the project to be as flexible as possible by not assuming the maximum number of players. For example, making it easy to extend the number of players by creating them based on a passed in parameter rather than just hard coding 2 players or determining the highest value card/ties for any number of active cards in the round.

In retrospect it looked like "War" is only every played with 2 players. Had I known that 2 players would be the maximum number of players, I may have simplified and streamlined the logic to accomodate at most 2 players.

Since Python is a dynamically typed language it was difficult to keep track of the data types inside of \_round\_cards, sorted\_cards, and dups. While writing the code I ran into several errors/bugs involved with \_round\_cards being an array of tuples containing a reference to the player and the card they had in play. I think I would have ran into less errors if I had converted the acive round card be a property of the player and simply keep track of an array of players

I also did not expect for testing to take as long as it did especially for the Board class. If I had to do it over I would allocate more time to testing and either write the tests before implementing the function/class or immediately afterwards. Also add compare functions inside each class to reduce testing verbosity.