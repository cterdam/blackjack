from blackjack.game import Game
from blackjack.card import Card
from blackjack.game_config import GameConfig


def test_constants():

    # Cut card should only appear once in the play deck
    g = Game(GameConfig())
    assert g.deck.deck.count(Game.cut_card) == 1

    # Blackjack value should be int or float
    assert type(Game.blackjack_value) in (int, float)

    # Initial hand size should be nonnegative int
    assert type(Game.initial_hand_size) is int
    assert Game.initial_hand_size >= 0

    # rank2value should send each of 2-K to int or float
    for r in (Card.numbers + Card.faces):
        assert type(Game.rank2value[r]) in (int, float)


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
