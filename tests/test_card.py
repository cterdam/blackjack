from blackjack.card import Card
import itertools
import pytest


def test_constants():

    # Constants should all be different
    assert len(set(itertools.chain(Card.suits, Card.numbers, Card.faces, Card.jokers))) == len(
        Card.suits) + len(Card.numbers) + len(Card.faces) + len(Card.jokers)

    # Ordinary ranks should be the collection of numbers, faces, and Ace
    ranks1 = set(Card.ranks)
    ranks2 = set(itertools.chain((Card.ACE,), Card.numbers, Card.faces))
    assert sorted(str(x) for x in ranks1) == sorted(str(x) for x in ranks2)


def test_init_params():

    # Ordinary cards
    with pytest.raises(AssertionError):
        # Valid rank, invalid suit
        Card(Card.NUM_2, Card.faces)
        Card(Card.NUM_10, Card.__repr__)
        Card(Card.ACE, Card.ACE)
        # Invalid rank, valid suit
        Card(Card.faces, Card.SPADES)
        Card(Card.DIAMONDS, Card.CLUBS)
        Card(Card.JOKER_SUIT, Card.DIAMONDS)
        # Invalid rank, invalid suit
        Card(Card.CLUBS, Card.NUM_8)
        Card(Card.suits, Card.BIG_JOKER)
        Card(Card.HEARTS, Card.__eq__)
    # Valid rank, valid suit
    Card(Card.NUM_6, Card.SPADES)
    Card(Card.ACE, Card.HEARTS)
    Card(Card.QUEEN, Card.CLUBS)

    # Joker cards
    with pytest.raises(AssertionError):
        # Valid rank, invalid suit
        Card(Card.LITTLE_JOKER, Card.SPADES)
        Card(Card.BIG_JOKER, Card.__doc__)
        Card(Card.BIG_JOKER, Card.numbers)
        # Invalid rank, valid suit
        Card(Card.SPADES, Card.JOKER_SUIT)
        Card(Card.NUM_3)
        Card(Card.JACK, Card.JOKER_SUIT)
        # Invalid rank, invalid suit
        Card(Card.jokers, Card.suits)
        Card(Card.__str__, Card.NUM_5)
        Card(Card.JOKER_SUIT, Card.BIG_JOKER)
    # Valid rank, valid suit
    Card(Card.BIG_JOKER, Card.JOKER_SUIT)
    Card(Card.LITTLE_JOKER)


def test_is_ace():

    # These are aces
    assert Card(Card.ACE, Card.SPADES).is_ace
    assert Card(Card.ACE, Card.DIAMONDS).is_ace
    assert Card(Card.ACE, Card.HEARTS).is_ace

    # These are not aces
    assert not Card(Card.NUM_3, Card.CLUBS).is_ace
    assert not Card(Card.KING, Card.DIAMONDS).is_ace
    assert not Card(Card.LITTLE_JOKER).is_ace


def test_is_number():

    # These are numbers
    assert Card(Card.NUM_2, Card.CLUBS).is_number
    assert Card(Card.NUM_3, Card.HEARTS).is_number
    assert Card(Card.NUM_10, Card.SPADES).is_number

    # These are not numbers
    assert not Card(Card.JACK, Card.DIAMONDS).is_number
    assert not Card(Card.ACE, Card.HEARTS).is_number
    assert not Card(Card.BIG_JOKER).is_number


def test_is_face():

    # These are faces
    assert Card(Card.JACK, Card.HEARTS).is_face
    assert Card(Card.QUEEN, Card.DIAMONDS).is_face
    assert Card(Card.KING, Card.CLUBS).is_face

    # These are not faces
    assert not Card(Card.ACE, Card.SPADES).is_face
    assert not Card(Card.NUM_4, Card.HEARTS).is_face
    assert not Card(Card.LITTLE_JOKER).is_face


def test_is_joker():

    # These are jokers
    assert Card(Card.LITTLE_JOKER).is_joker
    assert Card(Card.BIG_JOKER).is_joker

    # These are not jokers
    assert not Card(Card.ACE, Card.DIAMONDS).is_joker
    assert not Card(Card.NUM_8, Card.HEARTS).is_joker
    assert not Card(Card.QUEEN, Card.HEARTS).is_joker


def test_str():
    assert str(Card(Card.ACE, Card.HEARTS)) == '♥A'
    assert str(Card(Card.NUM_3, Card.CLUBS)) == '♣3'
    assert str(Card(Card.QUEEN, Card.SPADES)) == '♠Q'
    assert str(Card(Card.BIG_JOKER)) == 'Big Joker'


def test_repr():
    assert repr(Card(Card.ACE, Card.SPADES)) == 'Ace of Spades'
    assert repr(Card(Card.NUM_7, Card.CLUBS)) == '7 of Clubs'
    assert repr(Card(Card.KING, Card.DIAMONDS)) == 'King of Diamonds'
    assert repr(Card(Card.LITTLE_JOKER)) == 'Little Joker'


def test_eq_and_hash():

    # These are equal
    c1 = Card(Card.ACE, Card.DIAMONDS)
    c2 = Card(Card.ACE, Card.DIAMONDS)
    assert c1 is not c2
    assert c1 == c2
    assert hash(c1) == hash(c2)

    c1 = Card(Card.NUM_5, Card.HEARTS)
    c2 = Card(Card.NUM_5, Card.HEARTS)
    assert c1 is not c2
    assert c1 == c2
    assert hash(c1) == hash(c2)

    c1 = Card(Card.KING, Card.CLUBS)
    c2 = Card(Card.KING, Card.CLUBS)
    assert c1 is not c2
    assert c1 == c2
    assert hash(c1) == hash(c2)

    c1 = Card(Card.LITTLE_JOKER)
    c2 = Card(Card.LITTLE_JOKER)
    assert c1 is not c2
    assert c1 == c2
    assert hash(c1) == hash(c2)

    # These are not equal

    assert Card(Card.ACE, Card.DIAMONDS) != Card(Card.NUM_9, Card.DIAMONDS)
    assert Card(Card.NUM_6, Card.HEARTS) != Card(Card.NUM_6, Card.SPADES)
    assert Card(Card.JACK, Card.CLUBS) != Card(Card.NUM_10, Card.SPADES)
    assert Card(Card.NUM_4, Card.SPADES) != Card(Card.LITTLE_JOKER)
    assert Card(Card.KING, Card.HEARTS) != Card(Card.BIG_JOKER)
    assert Card(Card.LITTLE_JOKER) != Card(Card.BIG_JOKER)
    assert Card(Card.LITTLE_JOKER) != Card
    assert Card(Card.LITTLE_JOKER) != 'Card'
    assert Card(Card.LITTLE_JOKER) != None


def test_random_init():
    num_trials = 10
    for _ in range(num_trials):
        if Card() != Card():
            return
    raise AssertionError(
        f'Card() consecutively generated {num_trials} equal pairs')


def test_random():
    num_trials = 10
    for _ in range(num_trials):
        if Card.random() != Card.random():
            return
    raise AssertionError(
        f'Card.random() consecutively generated {num_trials} equal pairs')
