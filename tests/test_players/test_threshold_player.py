import pytest
from blackjack import Card, Deck, Hand, GameConfig
from blackjack.players import ThresholdPlayer


def parametrize_test(inputs, f):
    # Runs f(input) for all input in inputs
    for input in inputs:
        f(input)


def test_init_params():

    # name must be string
    def invalid_name(name):
        with pytest.raises(AssertionError):
            ThresholdPlayer(name=name)
    parametrize_test([None, True, 0, 0.5, [2]], invalid_name)
    ThresholdPlayer(name="")
    ThresholdPlayer(name="Alice")
    ThresholdPlayer(name="0")

    # bankroll must be non-negative int or float
    def invalid_bankroll(b):
        with pytest.raises(AssertionError):
            ThresholdPlayer(bankroll=b)
    parametrize_test([None, True, "0", [3], -0.5, -1], invalid_bankroll)
    ThresholdPlayer(bankroll=0)
    ThresholdPlayer(bankroll=5)
    ThresholdPlayer(bankroll=12.5)
    ThresholdPlayer(bankroll=float('inf'))

    # hard_threshold must be non-negative int
    def invalid_soft(t):
        with pytest.raises(AssertionError):
            ThresholdPlayer(hard_threshold=t)
    parametrize_test([None, True, "0", [3], 3.5, -1], invalid_soft)
    ThresholdPlayer(hard_threshold=0)
    ThresholdPlayer(hard_threshold=5)

    # soft_threshold must be non-negative int
    def invalid_hard(t):
        with pytest.raises(AssertionError):
            ThresholdPlayer(soft_threshold=t)
    parametrize_test([None, True, "0", [3], 3.5, -1], invalid_hard)
    ThresholdPlayer(soft_threshold=0)
    ThresholdPlayer(soft_threshold=5)

    # bet must be non-negative int or float
    def invalid_bet(b):
        with pytest.raises(AssertionError):
            ThresholdPlayer(bet=b)
    parametrize_test([None, True, "0", [3], -0.5, -1], invalid_bet)
    ThresholdPlayer(bet=0)
    ThresholdPlayer(bet=5)
    ThresholdPlayer(bet=12.5)
    ThresholdPlayer(bet=float('inf'))

    # Test various instantiations
    threshold1 = ThresholdPlayer()
    threshold2 = ThresholdPlayer(name="Bob", hard_threshold=0)
    threshold3 = ThresholdPlayer(
        name="a", bankroll=2.5, hard_threshold=12, soft_threshold=26, bet=3.14)

    for t in [threshold1, threshold2, threshold3]:
        assert type(t.name) is str
        assert type(t.bankroll) in (int, float)
        assert t.bankroll >= 0
        assert type(t.hard_threshold) is int
        assert t.hard_threshold >= 0
        assert type(t.soft_threshold) is int
        assert t.soft_threshold >= 0
        assert type(t.bet) in (int, float)
        assert t.bet >= 0
        assert t.dealer == False
        assert t._game_config == None
        assert t._hands == None
        assert t._hand_index == None
    assert threshold2.name == "Bob"
    assert threshold2.hard_threshold == 0
    assert threshold3.name == "a"
    assert threshold3.bankroll == 2.5
    assert threshold3.hard_threshold == 12
    assert threshold3.soft_threshold == 26
    assert threshold3.bet == 3.14


def test_sit_down():

    # Test Illegal Params
    def invalid_gc(gc):
        with pytest.raises(AssertionError):
            ThresholdPlayer().sit_down(gc)
    parametrize_test([None, True, 0, 0.5, [2], "game_config"], invalid_gc)

    # Test updating game_config
    gc1 = GameConfig()
    gc2 = GameConfig(num_decks=2)
    t = ThresholdPlayer()

    t.sit_down(gc1)
    assert t._game_config == gc1
    t.sit_down(gc2)
    assert t._game_config == gc2

    # Test resetting hand
    t.place_bet()
    t.sit_down(gc1)
    assert t._game_config == gc1
    assert t._hands == None
    assert t._hand_index == None


def test_place_bet():

    def initialized_hands(t):
        assert type(t._hands) is list
        assert len(t._hands) == 1
        assert type(t._hand_index) is int
        assert t._hand_index == 0
        assert type(t._hands[t._hand_index]) is Hand
        assert t._hands[t._hand_index].cards == []

    # Test Illegal Calls
    t = ThresholdPlayer()
    with pytest.raises(AssertionError):
        t.place_bet()

    # Test Updating Bankroll and Hands
    t1 = ThresholdPlayer(bankroll=100, bet=5)
    gc_int_bet = GameConfig(int_bet_only=True)
    gc_all_bet = GameConfig(int_bet_only=False)
    gc_min_max = GameConfig(min_bet=10, max_bet=20)

    t1.sit_down(gc_int_bet)
    assert t1.place_bet() == 5
    assert t1.bankroll == 95
    initialized_hands(t1)
    t1.sit_down(gc_all_bet)
    assert t1.place_bet() == 5
    assert t1.bankroll == 90
    initialized_hands(t1)

    # Test respecting gameConfig.int_bet_only
    t2 = ThresholdPlayer(bankroll=3, bet=4.01)
    t2.sit_down(gc_int_bet)
    assert t2.place_bet() == 3
    initialized_hands(t2)
    assert t2.place_bet() == 0
    assert t._hands == None
    assert t._hand_index == None

    t3 = ThresholdPlayer(bankroll=4.9, bet=1.1)
    t3.sit_down(gc_all_bet)
    assert t3.place_bet() == 1.1
    assert round(t3.bankroll, 5) == 3.8
    initialized_hands(t3)
    t3.sit_down(gc_int_bet)
    assert t3.place_bet() == 1
    assert round(t3.bankroll, 5) == 2.8
    initialized_hands(t3)

    # Test respecting gameConfig.min_bet and max_bet
    tlow = ThresholdPlayer(bankroll=100, bet=5)
    tmiddle = ThresholdPlayer(bankroll=100, bet=15)
    thigh = ThresholdPlayer(bankroll=100, bet=25)
    tlow.sit_down(gc_min_max)
    tmiddle.sit_down(gc_min_max)
    thigh.sit_down(gc_min_max)
    assert tlow.place_bet() == 10
    assert tlow.bankroll == 90
    assert tmiddle.place_bet() == 15
    assert tmiddle.bankroll == 85
    assert thigh.place_bet() == 20
    assert thigh.bankroll == 80


def test_observe_card():

    # Test Illegal Params
    t = ThresholdPlayer()
    c = Card()
    with pytest.raises(AssertionError):
        t.observe_card(c, 1)

    t.sit_down(GameConfig())

    # card must be of type Card
    def invalid_card(card):
        with pytest.raises(AssertionError):
            t.observe_card(card, 1)
    parametrize_test([None, True, "Big Joker", 3, [-2]], invalid_card)

    # player must be non-negative int
    def invalid_player(player):
        with pytest.raises(AssertionError):
            t.observe_card(c, player)
    parametrize_test([None, True, "0", -1, [2], 0.5], invalid_player)

    t.observe_card(c, 1)
    t.observe_card(c, 0)


def test_has_hand():

    # Test Normal Game Loop
    t = ThresholdPlayer()
    gc = GameConfig()
    assert t.has_hand() == False
    t.sit_down(gc)
    assert t.has_hand() == False
    t.place_bet()
    assert t.has_hand() == True
    t.observe_card(Card(), 0)
    t.decide_split()
    t.decide_hit()
    assert t.has_hand() == True
    t.final_payout([3.75])
    assert t.has_hand() == False

    # Test Edge Cases
    t.place_bet()
    assert t.has_hand() == True
    for index in [-1, 0.5, 1]:
        t._hand_index = index
        assert t.has_hand() == False
    t._hand_index = 0
    t._hands[t._hand_index] = Hand([Card(), Card()])
    assert t.has_hand() == True
    t._hands[t._hand_index] = 4
    assert t.has_hand() == False


def test_cur_hand():

    # Test Normal Game Loop
    t = ThresholdPlayer()
    gc = GameConfig()
    assert t.curr_hand() == None
    t.sit_down(gc)
    assert t.curr_hand() == None
    t.place_bet()
    assert t.curr_hand() == t._hands[t._hand_index]
    assert t.curr_hand() == Hand()
    card1, card2 = Card(), Card()
    t.curr_hand().add(card1).add(card2)
    assert t.curr_hand() == t._hands[t._hand_index]
    assert t.curr_hand() == Hand().add(card1).add(card2)
    t.final_payout([5])
    assert t.curr_hand() == None
    t.place_bet()
    assert t.curr_hand() == t._hands[t._hand_index]
    assert t.curr_hand() == Hand()
    t._hands = [Hand([card1]), Hand([card2])]
    assert t.curr_hand() == Hand([card1])
    t.next_hand()
    assert t.curr_hand() == Hand([card2])
    t.next_hand()
    assert t.curr_hand() == None


def test_next_hand():

    # Test Normal Game Loop
    t = ThresholdPlayer()
    gc = GameConfig()
    assert t._hand_index == None
    t.next_hand()
    assert t._hand_index == None
    t.sit_down(gc)
    t.place_bet()
    assert t._hand_index == 0
    t.next_hand()
    assert t._hand_index == 1
    k = 547
    for i in range(1, k):
        t.next_hand()
        assert t._hand_index == 1 + i
    t.final_payout([0])
    assert t._hand_index == None


def test_insurance():

    # Test Invalid Calls
    t = ThresholdPlayer(bankroll=5, bet=1)
    gc = GameConfig(int_bet_only=False)
    with pytest.raises(AssertionError):
        t.decide_insurance()
    with pytest.raises(AssertionError):
        t.insurance_payout(2)
    t.sit_down(gc)
    with pytest.raises(AssertionError):
        t.decide_insurance()
    with pytest.raises(AssertionError):
        t.insurance_payout(3)

    # Test Decide Insurance
    t.place_bet()
    assert t.decide_insurance() == False
    t.observe_card(Card(rank=Card.ACE), 0)
    assert t.decide_insurance() == False
    t.observe_card(Card(rank=Card.KING), 0)
    assert t.decide_insurance() == False

    # Test Insurance Payout
    def invalid_payout(p):
        with pytest.raises(AssertionError):
            t.insurance_payout(p)
    parametrize_test([None, False, "0", [2], -2], invalid_payout)
    t.insurance_payout(5)
    assert t.bankroll == 9

    t.insurance_payout(0)
    assert t.bankroll == 9

    t.insurance_payout(0.5)
    assert round(t.bankroll, 5) == 9.5


def test_decide_split_surrender_double():

    # Test Invalid Call
    t = ThresholdPlayer()
    gc = GameConfig()

    def invalid_setting(f):
        with pytest.raises(AssertionError):
            f()
    parametrize_test([t.decide_split, t.decide_double,
                     t.decide_surrender], invalid_setting)

    t.sit_down(gc)

    parametrize_test([t.decide_split, t.decide_double,
                     t.decide_surrender], invalid_setting)

    # Threshold Player Must Never Split, Surrender, or Double
    cards = Deck(num_full_decks=1)
    for card1 in cards.deck:
        for card2 in cards.deck:
            t.place_bet()
            t.curr_hand().add(card1).add(card2)
            assert t.decide_split() == False
            assert t.decide_surrender() == False
            assert t.decide_double() == False


def test_decide_hit():

    # Test Invalid Call
    t = ThresholdPlayer()
    gc = GameConfig()
    with pytest.raises(AssertionError):
        t.decide_hit()

    t.sit_down(gc)
    with pytest.raises(AssertionError):
        t.decide_hit()

    # Test Threshold Player Hit
    cards = Deck(num_full_decks=1)

    t.hard_threshold = 0
    t.soft_threshold = 0
    for card1 in cards.deck:
        for card2 in cards.deck:
            t.place_bet()
            t.curr_hand().add(card1).add(card2)
            assert t.decide_hit() == False

    t.hard_threshold = 22
    t.soft_threshold = 22
    for card1 in cards.deck:
        for card2 in cards.deck:
            t.place_bet()
            t.curr_hand().add(card1).add(card2)
            assert t.decide_hit() == True

    t.hard_threshold = 13
    t.soft_threshold = 15
    for card1 in cards.deck:
        for card2 in cards.deck:
            t.place_bet()
            t.curr_hand().add(card1).add(card2)
            hand_type, total = t.curr_hand().total
            if hand_type == Hand.HARD and total < t.hard_threshold:
                assert t.decide_hit() == True
            elif hand_type == Hand.SOFT and total < t.soft_threshold:
                assert t.decide_hit() == True
            else:
                assert t.decide_hit() == False

    t.hard_threshold = 7
    t.soft_threshold = 18
    for card1 in cards.deck:
        for card2 in cards.deck:
            t.place_bet()
            t.curr_hand().add(card1).add(card2)
            hand_type, total = t.curr_hand().total
            if hand_type == Hand.HARD and total < t.hard_threshold:
                assert t.decide_hit() == True
            elif hand_type == Hand.SOFT and total < t.soft_threshold:
                assert t.decide_hit() == True
            else:
                assert t.decide_hit() == False


def test_final_payout():

    t = ThresholdPlayer(bankroll=5, bet=1)
    gc = GameConfig()

    # Test Invalid Setting
    with pytest.raises(AssertionError):
        t.final_payout([5])
    t.sit_down(gc)
    with pytest.raises(AssertionError):
        t.final_payout([5])

    # Test Illegal Params
    t.place_bet()

    def invalid_payout(p):
        with pytest.raises(AssertionError):
            t.final_payout(p)
    parametrize_test([3, True, None, "[2]", [-1], [0, 3]], invalid_payout)

    assert t.bankroll == 4
    t.final_payout([35])
    assert t.bankroll == 39

    t.place_bet()
    t._hands = [Hand(), Hand(), Hand(), Hand(), Hand()]
    with pytest.raises(AssertionError):
        t.final_payout([5])
    t.final_payout([0.5, 0.5, 24, 0, 1])
    assert round(t.bankroll, 5) == 64


def test_str_and_repr():

    anna = ThresholdPlayer(name="anna", bankroll=0)
    bob = ThresholdPlayer(name="bob", bankroll=100)
    t37 = ThresholdPlayer(name="t37", bankroll=0.5)
    t_ = ThresholdPlayer(name="", bankroll=float('inf'))

    for t in [anna, bob, t37, t_]:
        assert str(t) == t.name
        assert repr(t) == f'Player({t.name}, {t.bankroll})'
