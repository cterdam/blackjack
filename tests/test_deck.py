import pytest
from blackjack.card import Card
from blackjack.deck import Deck


def test_init_params():

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
        Deck(include_joker='True')
        Deck(include_joker=None)
        Deck(include_joker=0)
        Deck(include_joker=[False])
        Deck(include_joker=(False))
    Deck(include_joker=True)
    Deck(include_joker=False)

    # ordered must be boolean
    with pytest.raises(AssertionError):
        Deck(ordered='True')
        Deck(ordered=None)
        Deck(ordered=0)
        Deck(ordered=[False])
        Deck(ordered=(False))
    Deck(ordered=True)
    Deck(ordered=False)


def test_len():
    # Length of spawned deck
    assert len(Deck(num_full_decks=1, include_joker=False)) == 52
    assert len(Deck(num_full_decks=1, include_joker=True)) == 54
    assert len(Deck(num_full_decks=2, include_joker=False)) == 2 * \
        len(Deck(num_full_decks=1, include_joker=False))
    assert len(Deck(num_full_decks=6, include_joker=False)) == 3 * \
        len(Deck(num_full_decks=2, include_joker=False))
    assert len(Deck(num_full_decks=24, include_joker=False)) == 8 * \
        len(Deck(num_full_decks=3, include_joker=False))
    assert len(Deck(num_full_decks=2, include_joker=True)) == 2 * \
        len(Deck(num_full_decks=1, include_joker=True))
    assert len(Deck(num_full_decks=6, include_joker=True)) == 3 * \
        len(Deck(num_full_decks=2, include_joker=True))
    assert len(Deck(num_full_decks=24, include_joker=True)) == 8 * \
        len(Deck(num_full_decks=3, include_joker=True))


def test_count():
    # Card counts
    one_deck_no_special = Deck(num_full_decks=1, include_joker=False)
    assert one_deck_no_special.count(Card('Spades', 2)) == 1
    assert one_deck_no_special.count(Card('Hearts', 'Ace')) == 1
    assert one_deck_no_special.count(Card('Diamonds', 'Jack')) == 1
    assert one_deck_no_special.count(Card(None, 'Little Joker')) == 0
    assert one_deck_no_special.count(Card(None, 'Big Joker')) == 0
    one_deck_with_special = Deck(num_full_decks=1, include_joker=True)
    assert one_deck_with_special.count(Card('Spades', 2)) == 1
    assert one_deck_with_special.count(Card('Hearts', 'Ace')) == 1
    assert one_deck_with_special.count(Card('Diamonds', 'Jack')) == 1
    assert one_deck_with_special.count(Card(None, 'Little Joker')) == 1
    assert one_deck_with_special.count(Card(None, 'Big Joker')) == 1
    four_deck_no_special = Deck(num_full_decks=4, include_joker=False)
    assert four_deck_no_special.count(Card('Spades', 2)) == 4
    assert four_deck_no_special.count(Card('Hearts', 'Ace')) == 4
    assert four_deck_no_special.count(Card('Diamonds', 'Jack')) == 4
    assert four_deck_no_special.count(Card(None, 'Little Joker')) == 0
    assert four_deck_no_special.count(Card(None, 'Big Joker')) == 0
    four_deck_with_special = Deck(num_full_decks=4, include_joker=True)
    assert four_deck_with_special.count(Card('Spades', 2)) == 4
    assert four_deck_with_special.count(Card('Hearts', 'Ace')) == 4
    assert four_deck_with_special.count(Card('Diamonds', 'Jack')) == 4
    assert four_deck_with_special.count(Card(None, 'Little Joker')) == 4
    assert four_deck_with_special.count(Card(None, 'Big Joker')) == 4


def test_order():
    # Ordered
    assert Deck(ordered=False) != Deck(ordered=False)


def test_eq():
    d1 = Deck(ordered=True)
    d2 = Deck(ordered=True)
    assert d1 == d2
    if d1[-1].suit == 'Clubs':
        d1[-1].suit = 'Hearts'
    else:
        d1[-1].suit = 'Clubs'
    assert d1 != d2
    assert d1 != None
    assert d2 != 3
    assert d1 != len(d1)
    assert d2 != Card('Spades', 3)


def test_different_object_and_iter():
    # Cards should be different objects
    d = Deck(include_joker=False)
    tallysuit = {suit: 0 for suit in Card.suits}
    expectation = {suit: 13 for suit in Card.suits}

    if d[-1].suit == 'Spades':
        d[-1].suit = 'Diamonds'
        for c in d:
            tallysuit[c.suit] += 1
        expectation['Spades'] -= 1
        expectation['Diamonds'] += 1
    else:
        thissuit = d[-1].suit
        d[-1].suit = 'Spades'
        expectation[thissuit] -= 1
        expectation['Spades'] += 1

    for c in d:
        tallysuit[c.suit] += 1
    for suit in ('Clubs', 'Diamonds', 'Hearts', 'Spades'):
        assert tallysuit[suit] == expectation[suit]

    assert len(d) == 0


def test_draw():
    d = Deck(include_joker=True)
    cardpeek = d[-1]
    len1 = len(d)
    c = d.draw()
    assert c == cardpeek
    len2 = len(d)
    assert len2 == len1-1


def test_insert():
    d = Deck()
    special_value = 'SPECIAL'
    assert d[10] != special_value
    d.insert(10, special_value)
    assert d[10] == special_value
    assert d[0] != special_value
    d.insert(0, special_value)
    assert d[0] == special_value
    assert d[-1] != special_value
    d.insert(-1, special_value)
    assert d[-2] == special_value
