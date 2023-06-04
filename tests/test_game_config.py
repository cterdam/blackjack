import pytest
from blackjack.game_config import GameConfig


def test_init_params():

    # num_decks must be positive int
    with pytest.raises(AssertionError):
        GameConfig(num_decks=None)
        GameConfig(num_decks=True)
        GameConfig(num_decks=[2])
        GameConfig(num_decks=(3))
        GameConfig(num_decks='4')
        GameConfig(num_decks='0')
        GameConfig(num_decks=-1)
        GameConfig(num_decks=-0.5)
        GameConfig(num_decks=0)
        GameConfig(num_decks=0.5)
    GameConfig(num_decks=1)
    GameConfig(num_decks=2)
    GameConfig(num_decks=10)

    # reshuffle_threshold must be int or float between 0 and 1
    with pytest.raises(AssertionError):
        GameConfig(reshuffle_threshold=None)
        GameConfig(reshuffle_threshold=True)
        GameConfig(reshuffle_threshold=[0.2])
        GameConfig(reshuffle_threshold=(0.3))
        GameConfig(reshuffle_threshold='0.4')
        GameConfig(reshuffle_threshold='0')
        GameConfig(reshuffle_threshold=-1)
        GameConfig(reshuffle_threshold=3.14)
        GameConfig(reshuffle_threshold=2)
    GameConfig(reshuffle_threshold=0)
    GameConfig(reshuffle_threshold=0.25)
    GameConfig(reshuffle_threshold=0.33)
    GameConfig(reshuffle_threshold=0.5)
    GameConfig(reshuffle_threshold=1)

    # double_after_split must be a boolean
    with pytest.raises(AssertionError):
        GameConfig(double_after_split='True')
        GameConfig(double_after_split=None)
        GameConfig(double_after_split=0)
        GameConfig(double_after_split=[False])
        GameConfig(double_after_split=(False))
    GameConfig(double_after_split=True)
    GameConfig(double_after_split=False)

    # max_hands must be positive int
    with pytest.raises(AssertionError):
        GameConfig(max_hands=None)
        GameConfig(max_hands=True)
        GameConfig(max_hands=[2])
        GameConfig(max_hands=(3))
        GameConfig(max_hands='4')
        GameConfig(max_hands='0')
        GameConfig(max_hands=-1)
        GameConfig(max_hands=-0.5)
        GameConfig(max_hands=0)
        GameConfig(max_hands=0.5)
    GameConfig(max_hands=1)
    GameConfig(max_hands=2)
    GameConfig(max_hands=10)

    # normal_pay must be int or float
    with pytest.raises(AssertionError):
        GameConfig(normal_pay=None)
        GameConfig(normal_pay=True)
        GameConfig(normal_pay=[0.2])
        GameConfig(normal_pay=(0.3))
        GameConfig(normal_pay='0.4')
        GameConfig(normal_pay='0')
    GameConfig(normal_pay=-1)
    GameConfig(normal_pay=0)
    GameConfig(normal_pay=0.25)
    GameConfig(normal_pay=0.33)
    GameConfig(normal_pay=0.5)
    GameConfig(normal_pay=1)
    GameConfig(normal_pay=2)
    GameConfig(normal_pay=3.14)

    # blackjack_pay must be int or float
    with pytest.raises(AssertionError):
        GameConfig(blackjack_pay=None)
        GameConfig(blackjack_pay=True)
        GameConfig(blackjack_pay=[0.2])
        GameConfig(blackjack_pay=(0.3))
        GameConfig(blackjack_pay='0.4')
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

    # natural_blackjack_only must be a boolean
    with pytest.raises(AssertionError):
        GameConfig(natural_blackjack_only='True')
        GameConfig(natural_blackjack_only=None)
        GameConfig(natural_blackjack_only=0)
        GameConfig(natural_blackjack_only=[False])
        GameConfig(natural_blackjack_only=(False))
    GameConfig(natural_blackjack_only=True)
    GameConfig(natural_blackjack_only=False)

    # min_bet must be non-negative int or float
    with pytest.raises(AssertionError):
        GameConfig(min_bet=None)
        GameConfig(min_bet=True)
        GameConfig(min_bet=[0.2])
        GameConfig(min_bet=(0.3))
        GameConfig(min_bet='0.4')
        GameConfig(min_bet='0')
    GameConfig(min_bet=0)
    GameConfig(min_bet=0.25)
    GameConfig(min_bet=0.33)
    GameConfig(min_bet=0.5)
    GameConfig(min_bet=1)
    GameConfig(min_bet=3/2)
    GameConfig(min_bet=2)
    GameConfig(min_bet=3.14)

    # max_bet must be non-negative int or float
    with pytest.raises(AssertionError):
        GameConfig(max_bet=None)
        GameConfig(max_bet=True)
        GameConfig(max_bet=[0.2])
        GameConfig(max_bet=(0.3))
        GameConfig(max_bet='0.4')
        GameConfig(max_bet='0')
    GameConfig(max_bet=0)
    GameConfig(max_bet=0.25)
    GameConfig(max_bet=0.33)
    GameConfig(max_bet=0.5)
    GameConfig(max_bet=1)
    GameConfig(max_bet=3/2)
    GameConfig(max_bet=2)
    GameConfig(max_bet=3.14)

    # int_bet_only must be a boolean
    with pytest.raises(AssertionError):
        GameConfig(int_bet_only='True')
        GameConfig(int_bet_only=None)
        GameConfig(int_bet_only=0)
        GameConfig(int_bet_only=[False])
        GameConfig(int_bet_only=(False))
    GameConfig(int_bet_only=True)
    GameConfig(int_bet_only=False)

    # blackjack_value must be positive int
    with pytest.raises(AssertionError):
        GameConfig(blackjack_value=None)
        GameConfig(blackjack_value=True)
        GameConfig(blackjack_value=[2])
        GameConfig(blackjack_value=(3))
        GameConfig(blackjack_value='4')
        GameConfig(blackjack_value='0')
        GameConfig(blackjack_value=-1)
        GameConfig(blackjack_value=-0.5)
        GameConfig(blackjack_value=0)
        GameConfig(blackjack_value=0.5)
    GameConfig(blackjack_value=1)
    GameConfig(blackjack_value=2)
    GameConfig(blackjack_value=10)

    # max_turns must be positive int
    with pytest.raises(AssertionError):
        GameConfig(max_turns=None)
        GameConfig(max_turns=True)
        GameConfig(max_turns=[2])
        GameConfig(max_turns=(3))
        GameConfig(max_turns='4')
        GameConfig(max_turns='0')
        GameConfig(max_turns=-1)
        GameConfig(max_turns=-0.5)
        GameConfig(max_turns=0)
        GameConfig(max_turns=0.5)
    GameConfig(max_turns=1)
    GameConfig(max_turns=2)
    GameConfig(max_turns=10)

    # init_hand_size must be non-negative int
    with pytest.raises(AssertionError):
        GameConfig(init_hand_size=None)
        GameConfig(init_hand_size=True)
        GameConfig(init_hand_size=[2])
        GameConfig(init_hand_size=(3))
        GameConfig(init_hand_size='4')
        GameConfig(init_hand_size='0')
        GameConfig(init_hand_size=-1)
        GameConfig(init_hand_size=-0.5)
        GameConfig(init_hand_size=0.5)
    GameConfig(init_hand_size=0)
    GameConfig(init_hand_size=1)
    GameConfig(init_hand_size=2)
    GameConfig(init_hand_size=10)
