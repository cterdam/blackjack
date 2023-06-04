class GameConfig:
    def __init__(
        self,
        num_decks=8,
        reshuffle_threshold=0.25,
        double_after_split=True,
        max_hands=4,
        normal_pay=1,
        blackjack_pay=3 / 2,
        natural_blackjack_only=True,
        min_bet=0,
        max_bet=float("inf"),
        int_bet_only=True,
        blackjack_value=21,
        max_turns=300,
        init_hand_size=2,
    ):
        """
        Config for a Blackjack game.

        TODO: early surrender, late surrender, insurance

        TODO (extra): card valuation, num of cards for each hit,
            num of cards for each double, amount of bet for double

        Params:

            num_decks (int): Number of full decks to include in this game.
                Req: num_decks > 0

            reshuffle_threshold (int or float): A special cut card will be
                inserted at this proportion in the playing deck. If the cut
                card comes up, that means the proportion of cards left in the
                deck had hit the reshuffle threshold, and the dealer will
                reshuffle the deck after the current round. A value of 0 will
                put the cut card in the bottom of the deck, and a value of 1
                will put it on top.
                Req: 0 <= reshuffle_threshold <= 1

            double_after_split (bool): Whether a player is allowed to double
                down after splitting a hand.
                Req: None

            max_hands (int): The max number of hands a player can obtain in a
                round by splitting. For example a value of 4 means a player
                can split at most 3 times in a round.
                Req: max_hands > 0

            normal_pay (int or float): The ratio of pay to player for a
                normal winning hand that is not blackjack. The player will
                receive a payout equal to this ratio times their original bet,
                plus their original bet back, for such a hand.
                Req: None

            blackjack_pay (int or float): The ratio of pay to player for a
                winning blackjack hand. The player will receive a payout equal
                to this ratio times their original bet, plus their original
                bet back, for a blackjack hand.
                Req: None

            natural_blackjack_only (bool): If true, the player will receive the
                blackjack pay only if the hand consists of the very initial
                cards the player is dealt in this round, meaning only normal
                pay for attaining a winning blackjack hand after creating new
                hands by splitting. If false, the player will receive the
                blackjack pay for any winning hand that contains as many cards
                as the initial hand and sums to the blackjack value.
                Req: None

            min_bet (int or float): To begin a Blackjack hand, players must bet
                at least the table minimum. For example, at a $5 to $500 table,
                the minimum bet to play is $5.
                Req: 0 <= min_bet

            max_bet (int or float): The maximum amount that a player can bet in
                a given hand.
                Req: 0 <= max_bet

            int_bet_only (boolean): If true, the player is allowed to place
                only integer-valued bets.
                Req: None

            blackjack_value (int): Sum at which a hand triggers the blackjack
                pay if dealt naturally.
                Req: blackjack_value > 0

            max_turns (int): The maximum number of permissable turns
                Req: max_turns > 0

            init_hand_size (int): The Number of cards each player starts with
                in a hand
                Req: init_hand_size >= 0
        """

        """ Init param check """
        # num_decks should be positive int
        assert type(num_decks) is int
        assert num_decks > 0
        # reshuffle_threshold should be int or float within 0 and 1 (inclusive)
        assert type(reshuffle_threshold) in (int, float)
        assert 0 <= reshuffle_threshold <= 1
        # double_after_split should be bool
        assert type(double_after_split) is bool
        # max_hands should be positive int
        assert type(max_hands) is int
        assert max_hands > 0
        # normal_pay should be int or float
        assert type(normal_pay) in (int, float)
        # blackjack_pay should be int or float
        assert type(blackjack_pay) in (int, float)
        # natural_blackjack_only should be int or float
        assert type(natural_blackjack_only) is bool
        # min_bet should be non-negative int or float
        assert type(min_bet) in (int, float)
        assert min_bet >= 0
        # max_bet should be non-negative int or float
        assert type(max_bet) in (int, float)
        assert max_bet >= 0
        # int_bet_only should be bool
        assert type(int_bet_only) is bool
        # blackjack_value should be positive int
        assert type(blackjack_value) is int
        assert blackjack_value > 0
        # max_turns should be positive int
        assert type(max_turns) is int
        assert max_turns > 0
        # init_hand_size should be non-negative int
        assert type(init_hand_size) is int
        assert init_hand_size >= 0

        self.num_decks = num_decks
        self.reshuffle_threshold = reshuffle_threshold
        self.double_after_split = double_after_split
        self.max_hands = max_hands
        self.normal_pay = normal_pay
        self.blackjack_pay = blackjack_pay
        self.natural_blackjack_only = natural_blackjack_only
        self.min_bet = min_bet
        self.max_bet = max_bet
        self.int_bet_only = int_bet_only
        self.blackjack_value = blackjack_value
        self.max_turns = max_turns
        self.init_hand_size = init_hand_size
