from blackjack.hand import Hand
from blackjack.card import Card
from tests.variables import *
import pytest


def test_constants():
    assert Hand.SOFT != Hand.HARD


def test_init_params():
    with pytest.raises(AssertionError):
        Hand(Card)
        Hand(Card())
        Hand((Card()))
    Hand()
    Hand([])
    Hand([Card()])
    Hand([Card(), Card(), Card()])


def test_breakdown():
    assert Hand._breakdown(h) == (0, 0)
    assert Hand._breakdown(h2) == (0, 2)
    assert Hand._breakdown(h23) == (0, 5)
    assert Hand._breakdown(A) == (1, 0)
    assert Hand._breakdown(AA) == (2, 0)
    assert Hand._breakdown(h67) == (0, 13)
    assert Hand._breakdown(AAAJ) == (3, 10)
    assert Hand._breakdown(AAAJ) == (3, 10)
    assert Hand._breakdown(AAA) == (3, 0)
    assert Hand._breakdown(AA64) == (2, 10)
    assert Hand._breakdown(AA3) == (2, 3)
    assert Hand._breakdown(A6) == (1, 6)
    assert Hand._breakdown(h8352) == (0, 18)
    assert Hand._breakdown(A45) == (1, 9)
    assert Hand._breakdown(K28) == (0, 20)
    assert Hand._breakdown(AK) == (1, 10)
    assert Hand._breakdown(Q75) == (0, 22)
    assert Hand._breakdown(JQK5A) == (1, 35)


def test_calc_total():
    assert Hand._calc_total(0, 0) == (Hand.HARD, 0)
    assert Hand._calc_total(0, 2) == (Hand.HARD, 2)
    assert Hand._calc_total(0, 5) == (Hand.HARD, 5)
    assert Hand._calc_total(1, 0) == (Hand.SOFT, 11)
    assert Hand._calc_total(2, 0) == (Hand.SOFT, 12)
    assert Hand._calc_total(0, 13) == (Hand.HARD, 13)
    assert Hand._calc_total(3, 10) == (Hand.HARD, 13)
    assert Hand._calc_total(3, 0) == (Hand.SOFT, 13)
    assert Hand._calc_total(2, 10) == (Hand.HARD, 12)
    assert Hand._calc_total(2, 3) == (Hand.SOFT, 15)
    assert Hand._calc_total(1, 6) == (Hand.SOFT, 17)
    assert Hand._calc_total(0, 18) == (Hand.HARD, 18)
    assert Hand._calc_total(1, 9) == (Hand.SOFT, 20)
    assert Hand._calc_total(0, 20) == (Hand.HARD, 20)
    assert Hand._calc_total(1, 10) == (Hand.SOFT, 21)
    assert Hand._calc_total(0, 22) == (Hand.HARD, 22)
    assert Hand._calc_total(1, 35) == (Hand.HARD, 36)


def test_init():
    for handlist in handlists:
        h = Hand(handlist)
        assert (h.num_aces, h.hard_total) == Hand._breakdown(handlist)
        assert h.total == Hand._calc_total(h.num_aces, h.hard_total)
