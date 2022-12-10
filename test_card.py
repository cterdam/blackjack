from card import Card
import pytest


def test_init():

    # Ordinary cards
    with pytest.raises(AssertionError):
        # Invalid suit, valid rank
        Card(2, 2)
        Card('s', 10)
        Card('hearts', 'Ace')
        # Valid suit, invalid rank
        Card('Spades', 'Spades')
        Card('Clubs', '5')
        Card('Diamonds', 12)
        # Invalid suit, invalid rank
        Card(13, 13)
        Card('hello', 'big joker')
        Card(12, 'Hearts')
    # Valid suit, valid rank
    Card('Spades', 6)
    Card('Hearts', 'Ace')
    Card('Clubs', 'Queen')

    # Joker cards
    with pytest.raises(AssertionError):
        # Invalid suit, valid rank
        Card('Spades', 'Little Joker')
        Card('s', 'Big Joker')
        Card('hearts', 'Big Joker')
        # Valid suit, invalid rank
        Card(None, 'Spades')
        Card(None, 3)
        Card(None, 12)
        # Invalid suit, invalid rank
        Card(13, 5)
        Card('hello', 'big joker')
        Card(12, 'Hearts')
    # Valid suit, valid rank
    Card(None, 'Big Joker')
    Card(None, 'Little Joker')


def test_is_ace():

    # These are aces
    assert Card('Spades', 'Ace').is_ace()
    assert Card('Diamonds', 'Ace').is_ace()
    assert Card('Hearts', 'Ace').is_ace()

    # These are not aces
    assert not Card('Clubs', 3).is_ace()
    assert not Card('Diamonds', 'King').is_ace()
    assert not Card(None, 'Little Joker').is_ace()


def test_is_number():

    # These are numbers
    assert Card('Clubs', 2).is_number()
    assert Card('Hearts', 3).is_number()
    assert Card('Spades', 10).is_number()

    # These are not numbers
    assert not Card('Diamonds', 'Jack').is_number()
    assert not Card('Hearts', 'Ace').is_number()
    assert not Card(None, 'Big Joker').is_number()


def test_is_face():

    # These are faces
    assert Card('Hearts', 'Jack').is_face()
    assert Card('Diamonds', 'Queen').is_face()
    assert Card('Clubs', 'King').is_face()

    # These are not faces
    assert not Card('Spades', 'Ace').is_face()
    assert not Card('Hearts', 4).is_face()
    assert not Card(None, 'Little Joker').is_face()


def test_is_joker():

    # These are jokers
    assert Card(None, 'Little Joker').is_joker()
    assert Card(None, 'Big Joker').is_joker()

    # These are not jokers
    assert not Card('Diamonds', 'Ace').is_joker()
    assert not Card('Hearts', 8).is_joker()
    assert not Card('Clubs', 'Queen').is_joker()


def test_str():
    assert str(Card('Hearts', 'Ace')) == '♥A'
    assert str(Card('Clubs', 3)) == '♣3'
    assert str(Card('Spades', 'Queen')) == '♠Q'
    assert str(Card(None, 'Big Joker')) == 'Big Joker'


def test_repr():
    assert repr(Card('Spades', 'Ace')) == 'Ace of Spades'
    assert repr(Card('Clubs', 7)) == '7 of Clubs'
    assert repr(Card('Diamonds', 'King')) == 'King of Diamonds'
    assert repr(Card(None, 'Little Joker')) == 'Little Joker'


def test_eq_and_hash():

    # These are equal

    c1 = Card('Diamonds', 'Ace')
    c2 = Card('Diamonds', 'Ace')
    assert c1 is not c2
    assert c1 == c2
    assert hash(c1) == hash(c2)

    c1 = Card('Hearts', 5)
    c2 = Card('Hearts', 5)
    assert c1 is not c2
    assert c1 == c2
    assert hash(c1) == hash(c2)

    c1 = Card('Clubs', 'King')
    c2 = Card('Clubs', 'King')
    assert c1 is not c2
    assert c1 == c2
    assert hash(c1) == hash(c2)

    c1 = Card(None, 'Little Joker')
    c2 = Card(None, 'Little Joker')
    assert c1 is not c2
    assert c1 == c2
    assert hash(c1) == hash(c2)

    # These are not equal

    assert Card('Diamonds', 'Ace') != Card('Diamonds', 9)
    assert Card('Hearts', 6) != Card('Spades', 6)
    assert Card('Clubs', 'Jack') != Card('Spades', 10)
    assert Card('Spades', 4) != Card(None, 'Little Joker')
    assert Card('Hearts', 'King') != Card(None, 'Big Joker')
    assert Card(None, 'Little Joker') != Card(None, 'Big Joker')
    assert Card(None, 'Little Joker') != Card
    assert Card(None, 'Little Joker') != 'Card'
    assert Card(None, 'Little Joker') != None


def test_random():

    num_trials = 10
    for _ in range(num_trials):
        if Card.random() != Card.random():
            return
    raise AssertionError(
        f'Card.random() consecutively generated {num_trials} equal pairs')
