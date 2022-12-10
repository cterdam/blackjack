import pytest
from game import Game


def test_init_params():

    # num_decks must be positive int
    with pytest.raises(AssertionError):
        Game(num_decks=None)
        Game(num_decks=True)
        Game(num_decks=[2])
        Game(num_decks=(3))
        Game(num_decks='4')
        Game(num_decks='0')
        Game(num_decks=-1)
        Game(num_decks=0)
    Game(num_decks=1)
    Game(num_decks=2)
    Game(num_decks=10)

    # reshuffle_threshold must be float or int between 0 and 1
    with pytest.raises(AssertionError):
        Game(reshuffle_threshold=None)
        Game(reshuffle_threshold=True)
        Game(reshuffle_threshold=[0.2])
        Game(reshuffle_threshold=(0.3))
        Game(reshuffle_threshold='0.4')
        Game(reshuffle_threshold='0')
        Game(reshuffle_threshold=-1)
        Game(reshuffle_threshold=3.14)
        Game(reshuffle_threshold=2)
    Game(reshuffle_threshold=0)
    Game(reshuffle_threshold=0.25)
    Game(reshuffle_threshold=0.33)
    Game(reshuffle_threshold=0.5)
    Game(reshuffle_threshold=1)

    # double_after_split must be a boolean
    with pytest.raises(AssertionError):
        Game(double_after_split='True')
        Game(double_after_split=None)
        Game(double_after_split=0)
        Game(double_after_split=[False])
        Game(double_after_split=(False))
    Game(double_after_split=True)
    Game(double_after_split=False)

    # max_hands must be positive int
    with pytest.raises(AssertionError):
        Game(max_hands=None)
        Game(max_hands=True)
        Game(max_hands=[2])
        Game(max_hands=(3))
        Game(max_hands='4')
        Game(max_hands='0')
        Game(max_hands=-1)
        Game(max_hands=0)
    Game(max_hands=1)
    Game(max_hands=2)
    Game(max_hands=10)

    # late_surrender must be a boolean
    with pytest.raises(AssertionError):
        Game(late_surrender='True')
        Game(late_surrender=None)
        Game(late_surrender=0)
        Game(late_surrender=[False])
        Game(late_surrender=(False))
    Game(late_surrender=True)
    Game(late_surrender=False)


def test_reshuffle_threshold():

    g = Game(num_decks=8, reshuffle_threshold=0.33)
    original_len = len(g.deck)
    counter = 0
    while g.deck.draw() != Game.cut_card:
        counter += 1
    assert 0.66 < (counter / original_len) < 0.68

    g = Game(num_decks=8, reshuffle_threshold=0.25)
    original_len = len(g.deck)
    counter = 0
    while g.deck.draw() != Game.cut_card:
        counter += 1
    assert 0.74 < (counter / original_len) < 0.76

    g = Game(num_decks=8, reshuffle_threshold=0)
    original_len = len(g.deck)
    counter = 0
    while g.deck.draw() != Game.cut_card:
        counter += 1
    assert counter == original_len - 1

    g = Game(num_decks=8, reshuffle_threshold=1)
    original_len = len(g.deck)
    counter = 0
    while g.deck.draw() != Game.cut_card:
        counter += 1
    assert counter == 0
