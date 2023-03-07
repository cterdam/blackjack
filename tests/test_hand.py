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
    assert Hand._breakdown(h55) == (0, 10)
    assert Hand._breakdown(A) == (1, 0)
    assert Hand._breakdown(h66) == (0, 12)
    assert Hand._breakdown(AA) == (2, 0)
    assert Hand._breakdown(h67) == (0, 13)
    assert Hand._breakdown(AAAJ) == (3, 10)
    assert Hand._breakdown(AAA) == (3, 0)
    assert Hand._breakdown(AA64) == (2, 10)
    assert Hand._breakdown(AA3) == (2, 3)
    assert Hand._breakdown(A6) == (1, 6)
    assert Hand._breakdown(h8352) == (0, 18)
    assert Hand._breakdown(A45) == (1, 9)
    assert Hand._breakdown(K28) == (0, 20)
    assert Hand._breakdown(AK) == (1, 10)
    assert Hand._breakdown(h777) == (0, 21)
    assert Hand._breakdown(Q75) == (0, 22)
    assert Hand._breakdown(JQK5A) == (1, 35)


def test_calc_total():
    assert Hand._calc_total(0, 0) == (Hand.HARD, 0)
    assert Hand._calc_total(0, 2) == (Hand.HARD, 2)
    assert Hand._calc_total(0, 5) == (Hand.HARD, 5)
    assert Hand._calc_total(0, 10) == (Hand.HARD, 10)
    assert Hand._calc_total(1, 0) == (Hand.SOFT, 11)
    assert Hand._calc_total(2, 0) == (Hand.SOFT, 12)
    assert Hand._calc_total(0, 12) == (Hand.HARD, 12)
    assert Hand._calc_total(0, 13) == (Hand.HARD, 13)
    assert Hand._calc_total(3, 10) == (Hand.HARD, 13)
    assert Hand._calc_total(3, 0) == (Hand.SOFT, 13)
    assert Hand._calc_total(2, 10) == (Hand.HARD, 12)
    assert Hand._calc_total(2, 3) == (Hand.SOFT, 15)
    assert Hand._calc_total(1, 6) == (Hand.SOFT, 17)
    assert Hand._calc_total(0, 18) == (Hand.HARD, 18)
    assert Hand._calc_total(1, 9) == (Hand.SOFT, 20)
    assert Hand._calc_total(0, 20) == (Hand.HARD, 20)
    assert Hand._calc_total(0, 21) == (Hand.HARD, 21)
    assert Hand._calc_total(1, 10) == (Hand.SOFT, 21)
    assert Hand._calc_total(0, 22) == (Hand.HARD, 22)
    assert Hand._calc_total(1, 35) == (Hand.HARD, 36)


def test_get_uniform_value():
    assert Hand._get_uniform_value(h) == None
    assert Hand._get_uniform_value(h2) == Card.NUM_2
    assert Hand._get_uniform_value(h23) == None
    assert Hand._get_uniform_value(h55) == Card.NUM_5
    assert Hand._get_uniform_value(A) == Card.ACE
    assert Hand._get_uniform_value(h66) == Card.NUM_6
    assert Hand._get_uniform_value(AA) == Card.ACE
    assert Hand._get_uniform_value(h67) == None
    assert Hand._get_uniform_value(AAAJ) == None
    assert Hand._get_uniform_value(AAA) == Card.ACE
    assert Hand._get_uniform_value(AA64) == None
    assert Hand._get_uniform_value(AA3) == None
    assert Hand._get_uniform_value(A6) == None
    assert Hand._get_uniform_value(h8352) == None
    assert Hand._get_uniform_value(A45) == None
    assert Hand._get_uniform_value(K28) == None
    assert Hand._get_uniform_value(AK) == None
    assert Hand._get_uniform_value(h777) == Card.NUM_7
    assert Hand._get_uniform_value(Q75) == None
    assert Hand._get_uniform_value(JQK5A) == None


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
    assert Hand(AAbA).add(Card(Card.JACK)) == Hand(AAAJ)

def test_explode(): 
    h = Hand([Card("Hearts", "Ace"), Card("Clubs", "Queen"), Card("Diamonds", "10")])
    exploded_hands = h.explode()
    assert len(exploded_hands) == 3
    assert exploded_hands[0] == Hand([Card("Hearts", "Ace")])
    assert exploded_hands[1] == Hand([Card("Clubs", "Queen")])
    assert exploded_hands[2] == Hand([Card("Diamonds", "10")])

    h2 = Hand([Card("Spades", "King"), Card("Hearts", "2")])
    exploded_hands2 = h2.explode()
    assert len(exploded_hands2) == 2
    assert exploded_hands2[0] == Hand([Card("Spades", "King")])
    assert exploded_hands2[1] == Hand([Card("Hearts", "2")])
    
    h3 = Hand([Card("Clubs", "7")])
    exploded_hands3 = h3.explode()
    assert len(exploded_hands3) == 1
    assert exploded_hands3[0] == Hand([Card("Clubs", "7")])

    h4 = Hand([])
    exploded_hands4 = h4.explode()
    assert len(exploded_hands4) == 0

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
