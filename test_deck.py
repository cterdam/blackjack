import pytest
from card import Card
from deck import Deck


def test_init():

    # num_full_decks must be positive int
    with pytest.raises(AssertionError):
        Deck(num_full_decks=None)
        Deck(num_full_decks=True)
        Deck(num_full_decks=[2])
        Deck(num_full_decks=(3))
        Deck(num_full_decks='4')
        Deck(num_full_decks='0')
        Deck(num_full_decks=-1)
        Deck(num_full_decks=0)
    Deck(num_full_decks=1)
    Deck(num_full_decks=2)
    Deck(num_full_decks=10)

    # include_special must be boolean
    with pytest.raises(AssertionError):
        Deck(include_special='True')
        Deck(include_special=None)
        Deck(include_special=0)
        Deck(include_special=[False])
        Deck(include_special=(False))
    Deck(include_special=True)
    Deck(include_special=False)

    # ordered must be boolean
    with pytest.raises(AssertionError):
        Deck(ordered='True')
        Deck(ordered=None)
        Deck(ordered=0)
        Deck(ordered=[False])
        Deck(ordered=(False))
    Deck(ordered=True)
    Deck(ordered=False)

    # Length of spawned deck
    assert len(Deck(num_full_decks=1, include_special=False)  # 52
               ) == len(Card.suits) * len(Card.ranks)
    assert len(Deck(num_full_decks=1, include_special=True)  # 54
               ) == len(Card.suits) * len(Card.ranks) + len(Card.special_values)
    assert len(Deck(num_full_decks=2, include_special=False)) == 2 * \
        len(Deck(num_full_decks=1, include_special=False))
    assert len(Deck(num_full_decks=6, include_special=False)) == 3 * \
        len(Deck(num_full_decks=2, include_special=False))
    assert len(Deck(num_full_decks=24, include_special=False)) == 8 * \
        len(Deck(num_full_decks=3, include_special=False))
    assert len(Deck(num_full_decks=2, include_special=True)) == 2 * \
        len(Deck(num_full_decks=1, include_special=True))
    assert len(Deck(num_full_decks=6, include_special=True)) == 3 * \
        len(Deck(num_full_decks=2, include_special=True))
    assert len(Deck(num_full_decks=24, include_special=True)) == 8 * \
        len(Deck(num_full_decks=3, include_special=True))

    # Card counts

    # ordered
    # different card objects
