import pytest
from blackjack.game_config import GameConfig


def test_init_params():

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

    # min_bet must be non-negative int or float
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

    # max_bet must be non-negative int or float
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

    # blackjack_value must be positive int
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
    with pytest.raises(AssertionError):
        GameConfig(blackjack_value=-1)
    with pytest.raises(AssertionError):
        GameConfig(blackjack_value=-0.5)
    with pytest.raises(AssertionError):
        GameConfig(blackjack_value=0)
    with pytest.raises(AssertionError):
        GameConfig(blackjack_value=0.5)
    GameConfig(blackjack_value=1)
    GameConfig(blackjack_value=2)
    GameConfig(blackjack_value=10)

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
