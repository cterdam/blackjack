import pytest
from blackjack import Card, GameConfig


def test_num_decks():
    # num_decks must be positive int
    with pytest.raises(AssertionError):
        GameConfig(num_decks=None)
    with pytest.raises(AssertionError):
        GameConfig(num_decks=True)
    with pytest.raises(AssertionError):
        GameConfig(num_decks=[2])
    with pytest.raises(AssertionError):
        GameConfig(num_decks=(3,))
    with pytest.raises(AssertionError):
        GameConfig(num_decks='4')
    with pytest.raises(AssertionError):
        GameConfig(num_decks='0')
    with pytest.raises(AssertionError):
        GameConfig(num_decks=-1)
    with pytest.raises(AssertionError):
        GameConfig(num_decks=-0.5)
    with pytest.raises(AssertionError):
        GameConfig(num_decks=0)
    with pytest.raises(AssertionError):
        GameConfig(num_decks=0.5)
    GameConfig(num_decks=1)
    GameConfig(num_decks=2)
    GameConfig(num_decks=10)


def test_reshuffle_threshold():
    # reshuffle_threshold must be int or float between 0 and 1
    with pytest.raises(AssertionError):
        GameConfig(reshuffle_threshold=None)
    with pytest.raises(AssertionError):
        GameConfig(reshuffle_threshold=True)
    with pytest.raises(AssertionError):
        GameConfig(reshuffle_threshold=[0.2])
    with pytest.raises(AssertionError):
        GameConfig(reshuffle_threshold=(0.3,))
    with pytest.raises(AssertionError):
        GameConfig(reshuffle_threshold='0.4')
    with pytest.raises(AssertionError):
        GameConfig(reshuffle_threshold='0')
    with pytest.raises(AssertionError):
        GameConfig(reshuffle_threshold=-1)
    with pytest.raises(AssertionError):
        GameConfig(reshuffle_threshold=3.14)
    with pytest.raises(AssertionError):
        GameConfig(reshuffle_threshold=2)
    GameConfig(reshuffle_threshold=0)
    GameConfig(reshuffle_threshold=0.25)
    GameConfig(reshuffle_threshold=0.33)
    GameConfig(reshuffle_threshold=0.5)
    GameConfig(reshuffle_threshold=1)


def test_double_after_split():
    # double_after_split must be a boolean
    with pytest.raises(AssertionError):
        GameConfig(double_after_split='True')
    with pytest.raises(AssertionError):
        GameConfig(double_after_split=None)
    with pytest.raises(AssertionError):
        GameConfig(double_after_split=0)
    with pytest.raises(AssertionError):
        GameConfig(double_after_split=[False])
    with pytest.raises(AssertionError):
        GameConfig(double_after_split=(False,))
    GameConfig(double_after_split=True)
    GameConfig(double_after_split=False)


def test_max_hands():
    # max_hands must be positive int
    with pytest.raises(AssertionError):
        GameConfig(max_hands=None)
    with pytest.raises(AssertionError):
        GameConfig(max_hands=True)
    with pytest.raises(AssertionError):
        GameConfig(max_hands=[2])
    with pytest.raises(AssertionError):
        GameConfig(max_hands=(3,))
    with pytest.raises(AssertionError):
        GameConfig(max_hands='4')
    with pytest.raises(AssertionError):
        GameConfig(max_hands='0')
    with pytest.raises(AssertionError):
        GameConfig(max_hands=-1)
    with pytest.raises(AssertionError):
        GameConfig(max_hands=-0.5)
    with pytest.raises(AssertionError):
        GameConfig(max_hands=0)
    with pytest.raises(AssertionError):
        GameConfig(max_hands=0.5)
    GameConfig(max_hands=1)
    GameConfig(max_hands=2)
    GameConfig(max_hands=10)


def test_early_surrender():
    # early_surrender must be a boolean
    with pytest.raises(AssertionError):
        GameConfig(early_surrender='True')
    with pytest.raises(AssertionError):
        GameConfig(early_surrender=None)
    with pytest.raises(AssertionError):
        GameConfig(early_surrender=0)
    with pytest.raises(AssertionError):
        GameConfig(early_surrender=[False])
    with pytest.raises(AssertionError):
        GameConfig(early_surrender=(False,))
    GameConfig(early_surrender=True)
    GameConfig(early_surrender=False)


def test_insurance():
    # insurance must be a boolean
    with pytest.raises(AssertionError):
        GameConfig(insurance='True')
    with pytest.raises(AssertionError):
        GameConfig(insurance=None)
    with pytest.raises(AssertionError):
        GameConfig(insurance=0)
    with pytest.raises(AssertionError):
        GameConfig(insurance=[False])
    with pytest.raises(AssertionError):
        GameConfig(insurance=(False,))
    GameConfig(insurance=True)
    GameConfig(insurance=False)


def test_late_surrender():
    # late_surrender must be a boolean
    with pytest.raises(AssertionError):
        GameConfig(late_surrender='True')
    with pytest.raises(AssertionError):
        GameConfig(late_surrender=None)
    with pytest.raises(AssertionError):
        GameConfig(late_surrender=0)
    with pytest.raises(AssertionError):
        GameConfig(late_surrender=[False])
    with pytest.raises(AssertionError):
        GameConfig(late_surrender=(False,))
    GameConfig(late_surrender=True)
    GameConfig(late_surrender=False)


def test_normal_pay():
    # normal_pay must be int or float
    with pytest.raises(AssertionError):
        GameConfig(normal_pay=None)
    with pytest.raises(AssertionError):
        GameConfig(normal_pay=True)
    with pytest.raises(AssertionError):
        GameConfig(normal_pay=[0.2])
    with pytest.raises(AssertionError):
        GameConfig(normal_pay=(0.3,))
    with pytest.raises(AssertionError):
        GameConfig(normal_pay='0.4')
    with pytest.raises(AssertionError):
        GameConfig(normal_pay='0')
    GameConfig(normal_pay=-1)
    GameConfig(normal_pay=0)
    GameConfig(normal_pay=0.25)
    GameConfig(normal_pay=0.33)
    GameConfig(normal_pay=0.5)
    GameConfig(normal_pay=1)
    GameConfig(normal_pay=2)
    GameConfig(normal_pay=3.14)


def test_blackjack_pay():
    # blackjack_pay must be int or float
    with pytest.raises(AssertionError):
        GameConfig(blackjack_pay=None)
    with pytest.raises(AssertionError):
        GameConfig(blackjack_pay=True)
    with pytest.raises(AssertionError):
        GameConfig(blackjack_pay=[0.2])
    with pytest.raises(AssertionError):
        GameConfig(blackjack_pay=(0.3,))
    with pytest.raises(AssertionError):
        GameConfig(blackjack_pay='0.4')
    with pytest.raises(AssertionError):
        GameConfig(blackjack_pay='0')
    GameConfig(blackjack_pay=-1)
    GameConfig(blackjack_pay=0)
    GameConfig(blackjack_pay=0.25)
    GameConfig(blackjack_pay=0.33)
    GameConfig(blackjack_pay=0.5)
    GameConfig(blackjack_pay=1)
    GameConfig(blackjack_pay=3/2)
    GameConfig(blackjack_pay=2)
    GameConfig(blackjack_pay=3.14)


def test_natural_blackjack_only():
    # natural_blackjack_only must be a boolean
    with pytest.raises(AssertionError):
        GameConfig(natural_blackjack_only='True')
    with pytest.raises(AssertionError):
        GameConfig(natural_blackjack_only=None)
    with pytest.raises(AssertionError):
        GameConfig(natural_blackjack_only=0)
    with pytest.raises(AssertionError):
        GameConfig(natural_blackjack_only=[False])
    with pytest.raises(AssertionError):
        GameConfig(natural_blackjack_only=(False,))
    GameConfig(natural_blackjack_only=True)
    GameConfig(natural_blackjack_only=False)


def test_min_bet():
    # min_bet must be int or float
    with pytest.raises(AssertionError):
        GameConfig(min_bet=None)
    with pytest.raises(AssertionError):
        GameConfig(min_bet=True)
    with pytest.raises(AssertionError):
        GameConfig(min_bet=[0.2])
    with pytest.raises(AssertionError):
        GameConfig(min_bet=(0.3,))
    with pytest.raises(AssertionError):
        GameConfig(min_bet='0.4')
    with pytest.raises(AssertionError):
        GameConfig(min_bet='0')
    GameConfig(min_bet=0)
    GameConfig(min_bet=0.25)
    GameConfig(min_bet=0.33)
    GameConfig(min_bet=0.5)
    GameConfig(min_bet=1)
    GameConfig(min_bet=3/2)
    GameConfig(min_bet=2)
    GameConfig(min_bet=3.14)


def test_max_bet():
    # max_bet must be int or float
    with pytest.raises(AssertionError):
        GameConfig(max_bet=None)
    with pytest.raises(AssertionError):
        GameConfig(max_bet=True)
    with pytest.raises(AssertionError):
        GameConfig(max_bet=[0.2])
    with pytest.raises(AssertionError):
        GameConfig(max_bet=(0.3,))
    with pytest.raises(AssertionError):
        GameConfig(max_bet='0.4')
    with pytest.raises(AssertionError):
        GameConfig(max_bet='0')
    GameConfig(max_bet=0)
    GameConfig(max_bet=0.25)
    GameConfig(max_bet=0.33)
    GameConfig(max_bet=0.5)
    GameConfig(max_bet=1)
    GameConfig(max_bet=3/2)
    GameConfig(max_bet=2)
    GameConfig(max_bet=3.14)


def test_int_bet_only():
    # int_bet_only must be a boolean
    with pytest.raises(AssertionError):
        GameConfig(int_bet_only='True')
    with pytest.raises(AssertionError):
        GameConfig(int_bet_only=None)
    with pytest.raises(AssertionError):
        GameConfig(int_bet_only=0)
    with pytest.raises(AssertionError):
        GameConfig(int_bet_only=[False])
    with pytest.raises(AssertionError):
        GameConfig(int_bet_only=(False,))
    GameConfig(int_bet_only=True)
    GameConfig(int_bet_only=False)


def test_blackjack_value():
    # blackjack_value must be int or float
    with pytest.raises(AssertionError):
        GameConfig(blackjack_value=None)
    with pytest.raises(AssertionError):
        GameConfig(blackjack_value=True)
    with pytest.raises(AssertionError):
        GameConfig(blackjack_value=[2])
    with pytest.raises(AssertionError):
        GameConfig(blackjack_value=(3,))
    with pytest.raises(AssertionError):
        GameConfig(blackjack_value='4')
    with pytest.raises(AssertionError):
        GameConfig(blackjack_value='0')
    GameConfig(blackjack_value=-1)
    GameConfig(blackjack_value=-0.5)
    GameConfig(blackjack_value=0)
    GameConfig(blackjack_value=0.5)
    GameConfig(blackjack_value=1)
    GameConfig(blackjack_value=2)
    GameConfig(blackjack_value=10)


def test_max_turns():
    # max_turns must be positive int
    with pytest.raises(AssertionError):
        GameConfig(max_turns=None)
    with pytest.raises(AssertionError):
        GameConfig(max_turns=True)
    with pytest.raises(AssertionError):
        GameConfig(max_turns=[2])
    with pytest.raises(AssertionError):
        GameConfig(max_turns=(3,))
    with pytest.raises(AssertionError):
        GameConfig(max_turns='4')
    with pytest.raises(AssertionError):
        GameConfig(max_turns='0')
    with pytest.raises(AssertionError):
        GameConfig(max_turns=-1)
    with pytest.raises(AssertionError):
        GameConfig(max_turns=-0.5)
    with pytest.raises(AssertionError):
        GameConfig(max_turns=0)
    with pytest.raises(AssertionError):
        GameConfig(max_turns=0.5)
    GameConfig(max_turns=1)
    GameConfig(max_turns=2)
    GameConfig(max_turns=10)


def test_init_hand_size():
    # init_hand_size must be non-negative int
    with pytest.raises(AssertionError):
        GameConfig(init_hand_size=None)
    with pytest.raises(AssertionError):
        GameConfig(init_hand_size=True)
    with pytest.raises(AssertionError):
        GameConfig(init_hand_size=[2])
    with pytest.raises(AssertionError):
        GameConfig(init_hand_size=(3,))
    with pytest.raises(AssertionError):
        GameConfig(init_hand_size='4')
    with pytest.raises(AssertionError):
        GameConfig(init_hand_size='0')
    with pytest.raises(AssertionError):
        GameConfig(init_hand_size=-1)
    with pytest.raises(AssertionError):
        GameConfig(init_hand_size=-0.5)
    with pytest.raises(AssertionError):
        GameConfig(init_hand_size=0.5)
    GameConfig(init_hand_size=0)
    GameConfig(init_hand_size=1)
    GameConfig(init_hand_size=2)
    GameConfig(init_hand_size=10)


def test_valuation():

    # The default valuation dict should send each possible Card rank
    # (excluding jokers) to either a number (int or float), or a tuple of
    # numbers with length greater than 1

    assert isinstance(GameConfig.Defaults.valuation, dict)
    for rank in Card.ranks:
        assert rank in GameConfig.Defaults.valuation.keys()
        if type(GameConfig.Defaults.valuation[rank]) is tuple:
            assert len(GameConfig.Defaults.valuation[rank]) > 1
            for val in GameConfig.Defaults.valuation[rank]:
                assert type(val) in (int, float)
        else:
            assert type(GameConfig.Defaults.valuation[rank]) in (int, float)

    # Test illegal params
    with pytest.raises(AssertionError):
        GameConfig(valuation=dict())
    with pytest.raises(AssertionError):
        GameConfig(valuation={Card.NUM_2: 2})
    with pytest.raises(AssertionError):
        GameConfig(valuation={rank: None for rank in Card.ranks})
    with pytest.raises(AssertionError):
        this_valuation = {rank: 0 for rank in Card.ranks}
        this_valuation[Card.NUM_7] = '0'
        GameConfig(valuation=this_valuation)

    # Test legal params
    this_valuation = {rank: 0 for rank in Card.ranks}
    this_valuation[Card.NUM_7] = (0,)
    GameConfig(valuation=this_valuation)
    GameConfig(valuation={rank: (10, 100) for rank in Card.ranks})
