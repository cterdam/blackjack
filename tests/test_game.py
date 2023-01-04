from blackjack.game import Game
from blackjack.game_config import GameConfig

"""
TODO

- cut_card only appears once in the playing deck
- initial_hand_size (int) >= 0
- rank2value sends each of 2-K to an int
"""


def test_reshuffle_threshold():

    g = Game(GameConfig(num_decks=8, reshuffle_threshold=0.33))
    original_len = len(g.deck)
    counter = 0
    while g.deck.draw() != Game.cut_card:
        counter += 1
    assert 0.66 < (counter / original_len) < 0.68

    g = Game(GameConfig(num_decks=8, reshuffle_threshold=0.25))
    original_len = len(g.deck)
    counter = 0
    while g.deck.draw() != Game.cut_card:
        counter += 1
    assert 0.74 < (counter / original_len) < 0.76

    g = Game(GameConfig(num_decks=8, reshuffle_threshold=0))
    original_len = len(g.deck)
    counter = 0
    while g.deck.draw() != Game.cut_card:
        counter += 1
    assert counter == original_len - 1

    g = Game(GameConfig(num_decks=8, reshuffle_threshold=1))
    original_len = len(g.deck)
    counter = 0
    while g.deck.draw() != Game.cut_card:
        counter += 1
    assert counter == 0
