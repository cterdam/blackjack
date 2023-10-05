from blackjack import Card
import itertools
import pytest


def test_constants():

    # Constants should all be different
    randoms = (Card.RANDOM,)
    assert len(set().union(Card.suits, Card.ranks, Card.jokers, randoms)) == \
        len(list(itertools.chain(Card.suits, Card.ranks, Card.jokers, randoms)))

    # Ordinary ranks should be the collection of numbers, faces, and Ace
    ranks1 = set(Card.ranks)
    ranks2 = set(itertools.chain((Card.ACE,), Card.numbers, Card.faces))
    assert sorted(str(x) for x in ranks1) == sorted(str(x) for x in ranks2)


def test_init_params():

    # Given rank, given suit
    c = Card(Card.NUM_6, Card.SPADES)
    assert c.rank == Card.NUM_6
    assert c.suit == Card.SPADES
    c = Card(Card.ACE, Card.HEARTS)
    assert c.rank == Card.ACE
    assert c.suit == Card.HEARTS
    c = Card(Card.QUEEN, Card.CLUBS)
    assert c.rank == Card.QUEEN
    assert c.suit == Card.CLUBS

    for r in Card.ranks:
        for s in Card.suits:
            c = Card(r, s)
            assert c.rank == r
            assert c.suit == s

    # Given joker cards
    c = Card(Card.LITTLE_JOKER)
    assert c.rank == Card.LITTLE_JOKER
    c = Card(Card.BIG_JOKER)
    assert c.rank == Card.BIG_JOKER

    # Given rank, random suit
    num_trials = 15
    ranks_to_try = {Card.NUM_3, Card.NUM_5, Card.NUM_10, Card.KING}
    suits_collected = set()
    for r in ranks_to_try:
        for _ in range(num_trials):
            c = Card(r)
            assert c.rank == r
            assert c.suit in Card.suits
            suits_collected.add(c.suit)
        assert len(suits_collected) > 2

    # Random rank, given suit
    num_trials = 25
    suits_to_try = {Card.CLUBS, Card.DIAMONDS, Card.HEARTS, Card.SPADES}
    ranks_collected = set()
    for s in suits_to_try:
        for _ in range(num_trials):
            c = Card(s)
            assert c.rank in Card.ranks
            assert c.suit == s
            ranks_collected.add(c.rank)
        assert len(ranks_collected) > 6

    # Random rank, random suit
    num_trials = 15
    ranks_collected = set()
    suits_collected = set()
    for _ in range(num_trials):
        c = Card()
        assert c.rank in Card.ranks
        assert c.suit in Card.suits
        ranks_collected.add(c.rank)
        suits_collected.add(c.suit)
    assert len(ranks_collected) > 6
    assert len(suits_collected) > 2

    # Illegal params
    with pytest.raises(AssertionError):
        Card(Card.NUM_7, Card.NUM_9)
    with pytest.raises(AssertionError):
        Card(Card.LITTLE_JOKER, Card.NUM_10)
    with pytest.raises(AssertionError):
        Card(Card.HEARTS, Card.SPADES)


def test_is_ace():

    # These are aces
    assert Card(Card.ACE, Card.SPADES).is_ace()
    assert Card(Card.ACE, Card.DIAMONDS).is_ace()
    assert Card(Card.ACE, Card.HEARTS).is_ace()
    assert Card(Card.ACE).is_ace()

    # These are not aces
    assert not Card(Card.NUM_3, Card.CLUBS).is_ace()
    assert not Card(Card.KING, Card.DIAMONDS).is_ace()
    assert not Card(Card.LITTLE_JOKER).is_ace()
    assert not Card(Card.NUM_8).is_ace()


def test_is_number():

    # These are numbers
    assert Card(Card.NUM_2, Card.CLUBS).is_number()
    assert Card(Card.NUM_3, Card.HEARTS).is_number()
    assert Card(Card.NUM_10, Card.SPADES).is_number()
    assert Card(Card.NUM_5).is_number()

    # These are not numbers
    assert not Card(Card.JACK, Card.DIAMONDS).is_number()
    assert not Card(Card.ACE, Card.HEARTS).is_number()
    assert not Card(Card.BIG_JOKER).is_number()
    assert not Card(Card.QUEEN).is_number()


def test_is_face():

    # These are faces
    assert Card(Card.JACK, Card.HEARTS).is_face()
    assert Card(Card.QUEEN, Card.DIAMONDS).is_face()
    assert Card(Card.KING).is_face()

    # These are not faces
    assert not Card(Card.ACE, Card.SPADES).is_face()
    assert not Card(Card.NUM_4, Card.HEARTS).is_face()
    assert not Card(Card.LITTLE_JOKER).is_face()
    assert not Card(Card.NUM_9).is_face()


def test_is_joker():

    # These are jokers
    assert Card(Card.LITTLE_JOKER).is_joker()
    assert Card(Card.BIG_JOKER).is_joker()

    # These are not jokers
    assert not Card(Card.ACE, Card.DIAMONDS).is_joker()
    assert not Card(Card.NUM_8, Card.HEARTS).is_joker()
    assert not Card(Card.QUEEN, Card.HEARTS).is_joker()
    assert not Card(Card.JACK).is_joker()


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


def test_random_rank():
    num_trials = 10
    for _ in range(num_trials):
        if Card._random_rank() != Card._random_rank():
            return
    raise AssertionError(
        f'Card.random_rank() consecutively generated {num_trials} equal pairs')


def test_random_suit():
    num_trials = 10
    for _ in range(num_trials):
        if Card._random_suit() != Card._random_suit():
            return
    raise AssertionError(
        f'Card.random_suit() consecutively generated {num_trials} equal pairs')


def test_random_generation():
    num_trials = 10
    for _ in range(num_trials):
        if Card() != Card():
            return
    raise AssertionError(
        f'Card() consecutively generated {num_trials} equal pairs')
