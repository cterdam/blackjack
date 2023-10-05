from blackjack import Card, Hand
from tests.variables import *
import pytest


def test_constants():
    assert Hand.SOFT != Hand.HARD


def test_init_params():
    with pytest.raises(AssertionError):
        Hand(Card)
    with pytest.raises(AssertionError):
        Hand(Card())
    with pytest.raises(AssertionError):
        Hand((Card(),))
    Hand()
    Hand([])
    Hand([Card()])
    Hand([Card(), Card(), Card()])


def test_add():
    assert Hand(h).add(Card(Card.NUM_2)) == Hand(h2)
    assert Hand(h).add(Card(Card.NUM_6)).add(Card(Card.NUM_6)) == Hand(h66)
    assert Hand(h).add(Card(Card.NUM_6)).add(Card(Card.NUM_7)) == Hand(h67)
    assert Hand(h).add(Card(Card.NUM_5)).add(Card(Card.NUM_5)) == Hand(h55)
    assert Hand(h).add(Card(Card.ACE)) == Hand(A)
    assert Hand(h).add(Card(Card.NUM_7)).add(Card(Card.NUM_7))\
        .add(Card(Card.NUM_7)) == Hand(h777)
    assert Hand(h).add(Card(Card.NUM_7)).add(Card(Card.QUEEN))\
        .add(Card(Card.NUM_5)) == Hand(Q75)
    assert Hand(h).add(Card(Card.KING)).add(Card(Card.ACE)) == Hand(AK)
    assert Hand(h2).add(Card(Card.NUM_3)) == Hand(h23)
    assert Hand(h2).add(Card(Card.NUM_8)).add(Card(Card.KING)) == Hand(K28)
    assert Hand(h23).add(Card(Card.NUM_5)).add(Card(Card.NUM_8)) == Hand(h8352)
    assert Hand(A).add(Card(Card.NUM_6)) == Hand(A6)
    assert Hand(A).add(Card(Card.NUM_4)).add(Card(Card.NUM_5)) == Hand(A45)
    assert Hand(A).add(Card(Card.KING)) == Hand(AK)
    assert Hand(A).add(Card(Card.ACE)) == Hand(AA)
    assert Hand(A).add(Card(Card.NUM_5)).add(Card(Card.KING))\
        .add(Card(Card.JACK)).add(Card(Card.QUEEN)) == Hand(JQK5A)
    assert Hand(AA).add(Card(Card.NUM_3)) == Hand(AA3)
    assert Hand(AA).add(Card(Card.NUM_6)).add(Card(Card.NUM_4)) == Hand(AA64)
    assert Hand(AA).add(Card(Card.ACE)) == Hand(AAA)
    assert Hand(AAA).add(Card(Card.JACK)) == Hand(AAAJ)


def test_str_and_repr():
    for handlist in handlists:
        hand = Hand(handlist)
        assert str(hand) == f'Hand of {len(handlist)} cards'
        r = repr(hand)
        assert r[0:7] == "Hand [ "
        assert r[-1] == "]"
        assert len(r) == 3 * len(handlist) + 8
        for i, s in enumerate(handlist):
            assert r[3*i+7:3*i+10] == str(s) + " "
