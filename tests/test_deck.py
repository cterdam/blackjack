import pytest
from blackjack.card import Card
from blackjack.deck import Deck


def test_init_params():

    # num_full_decks must be positive int
    with pytest.raises(AssertionError):
        Deck(num_full_decks=None)
    with pytest.raises(AssertionError):
        Deck(num_full_decks=True)
    with pytest.raises(AssertionError):
        Deck(num_full_decks=[2])
    with pytest.raises(AssertionError):
        Deck(num_full_decks=(3,))
    with pytest.raises(AssertionError):
        Deck(num_full_decks='4')
    with pytest.raises(AssertionError):
        Deck(num_full_decks='0')
    with pytest.raises(AssertionError):
        Deck(num_full_decks=-1)
    with pytest.raises(AssertionError):
        Deck(num_full_decks=0)
    Deck(num_full_decks=1)
    Deck(num_full_decks=2)
    Deck(num_full_decks=10)

    # include_special must be boolean
    with pytest.raises(AssertionError):
        Deck(include_joker='True')
    with pytest.raises(AssertionError):
        Deck(include_joker=None)
    with pytest.raises(AssertionError):
        Deck(include_joker=0)
    with pytest.raises(AssertionError):
        Deck(include_joker=[False])
    with pytest.raises(AssertionError):
        Deck(include_joker=(False,))
    Deck(include_joker=True)
    Deck(include_joker=False)

    # ordered must be boolean
    with pytest.raises(AssertionError):
        Deck(ordered='True')
    with pytest.raises(AssertionError):
        Deck(ordered=None)
    with pytest.raises(AssertionError):
        Deck(ordered=0)
    with pytest.raises(AssertionError):
        Deck(ordered=[False])
    with pytest.raises(AssertionError):
        Deck(ordered=(False,))
    Deck(ordered=True)
    Deck(ordered=False)


def test_len():
    single_deck_no_joker_len = len(Card.ranks) * len(Card.suits)
    single_deck_with_joker_len = single_deck_no_joker_len + len(Card.jokers)

    # Length of spawned deck
    assert len(Deck(num_full_decks=1, include_joker=False)
               ) == single_deck_no_joker_len
    assert len(Deck(num_full_decks=1, include_joker=True)
               ) == single_deck_with_joker_len
    assert len(Deck(num_full_decks=2, include_joker=False)
               ) == 2 * single_deck_no_joker_len
    assert len(Deck(num_full_decks=6, include_joker=False)
               ) == 6 * single_deck_no_joker_len
    assert len(Deck(num_full_decks=24, include_joker=False)
               ) == 24 * single_deck_no_joker_len
    assert len(Deck(num_full_decks=2, include_joker=True)
               ) == 2 * single_deck_with_joker_len
    assert len(Deck(num_full_decks=6, include_joker=True)
               ) == 6 * single_deck_with_joker_len
    assert len(Deck(num_full_decks=24, include_joker=True)
               ) == 24 * single_deck_with_joker_len


def test_order():
    assert Deck(ordered=True) == Deck(ordered=True)
    num_trials = 10
    for _ in range(num_trials):
        assert Deck(ordered=False) != Deck(ordered=False)


def test_eq():
    d1 = Deck(ordered=True)
    d2 = Deck(ordered=True)
    assert d1 == d2
    if d1.deck[-1].suit == Card.CLUBS:
        d1.deck[-1].suit = Card.HEARTS
    else:
        d1.deck[-1].suit = Card.CLUBS
    assert d1 != d2
    assert d1 != None
    assert d2 != 3
    assert d1 != len(d1)
    assert d2 != Card(Card.NUM_3, Card.SPADES)


def test_different_objects():

    # Cards should be different objects
    d = Deck(include_joker=False)
    tallysuit = {suit: 0 for suit in Card.suits}
    expectation = {suit: len(Card.ranks) for suit in Card.suits}

    if d.deck[-1].suit == Card.SPADES:
        d.deck[-1].suit = Card.DIAMONDS
        expectation[Card.SPADES] -= 1
        expectation[Card.DIAMONDS] += 1
    else:
        thissuit = d.deck[-1].suit
        d.deck[-1].suit = Card.SPADES
        expectation[thissuit] -= 1
        expectation[Card.SPADES] += 1

    for c in d.deck:
        tallysuit[c.suit] += 1
    for suit in Card.suits:
        assert tallysuit[suit] == expectation[suit]


def test_draw():
    d = Deck(include_joker=True)

    while(len(d) > 0):
        len1 = len(d)
        cardpeek = d.deck[-1]
        c = d.draw()
        assert c == cardpeek
        len2 = len(d)
        assert len2 == len1-1

    num_trials = 10
    for _ in range(num_trials):
        assert d.draw() == None


def test_insert():

    d = Deck()
    special_value = Card(Card.BIG_JOKER)

    assert d.deck[10] != special_value
    d.insert(10, special_value)
    assert d.deck[10] == special_value

    assert d.deck[0] != special_value
    d.insert(0, special_value)
    assert d.deck[0] == special_value

    assert d.deck[-1] != special_value
    d.insert(-1, special_value)
    assert d.deck[-2] == special_value

    assert d.deck[-1] != special_value
    d.insert(len(d), special_value)
    assert d.deck[-1] == special_value

    # Test illegal insert params
    with pytest.raises(AssertionError):
        d.insert('1', special_value)
        d.insert(0.5, special_value)
        d.insert(0, 'special')


def test_str_and_repr():
    d = Deck()
    bottom = str(d.deck[0])

    while len(d) > 3:
        assert str(d) == f'Deck of {len(d)} cards'
        r = repr(d)
        assert r[0:7] == 'Deck [ '
        assert r.count(' ... ') == 1
        assert r[-2:len(r)] == ' ]'
        assert bottom == r.split(' ')[-2]
        assert str(d.draw()) == r.split(' ')[2]

    # Now the deck contains 3 cards
    for num_cards_left in range(3, 0, -1):
        assert str(d) == f'Deck of {len(d)} cards'
        r = repr(d)
        assert r[0:7] == 'Deck [ '
        assert r[-2:len(r)] == ' ]'
        assert len(r.split(' ')) == num_cards_left + 3
        assert bottom == r.split(' ')[-2]
        assert str(d.draw()) == r.split(' ')[2]

    # Empty deck
    assert str(d) == 'Deck of 0 cards'
    assert repr(d) == 'Deck [ ]'
