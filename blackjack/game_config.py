class GameConfig():

    def __init__(self, num_decks=8, reshuffle_threshold=0.25,
                 double_after_split=True, max_hands=4, normal_pay=1,
                 blackjack_pay=3/2, natural_blackjack_only=True,
                 blackjack_value=21, initial_hand_size=2):
        """
        Config for a Blackjack game.

        TODO: early surrender, late surrender, insurance

        TODO (extra): card valuation, num of cards for each hit,
            num of cards for each double, amount of bet for double

        Params:

            num_decks (int): Number of full decks to include in this game.
                Req: num_decks > 1

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

            blackjack_value (int): If the initial cards dealt to the player's
                hand directly sum to this number and they win, they are
                awarded the blackjack pay instead of the normal pay. Note that
                a player hand summing to this value could also result in push
                if the dealer has the same sum.
                Req: None

            initial_hand_size (int): The number of cards dealt initially to
                the player. The dealer receives the same number of cards, but
                only the first card is shown.
                Req: initial_hand_size >= 0
        """

        if type(num_decks) is not int or num_decks < 1:
            raise AssertionError('num_decks must be a positive integer')
        if type(reshuffle_threshold) not in (int, float) or\
                not (0 <= reshuffle_threshold <= 1):
            raise AssertionError(
                'reshuffle_threshold must be int or float with value between'
                '0 and 1 (inclusive)')
        if type(double_after_split) is not bool:
            raise AssertionError('double_after_split must be a boolean')
        if type(max_hands) is not int or max_hands < 1:
            raise AssertionError('max_hands must be a positive integer')
        if type(normal_pay) not in (int, float):
            raise AssertionError('normal_pay must be int or float')
        if type(blackjack_pay) not in (int, float):
            raise AssertionError('blackjack_pay must be int or float')
        if type(natural_blackjack_only) is not bool:
            raise AssertionError('natural_blackjack_only must be a boolean')
        if type(blackjack_value) is not int:
            raise AssertionError('blackjack_value must be int')
        if type(initial_hand_size) is not int or initial_hand_size < 0:
            raise AssertionError('initial_hand_size must be nonnegative int')

        self.num_decks = num_decks
        self.reshuffle_threshold = reshuffle_threshold
        self.double_after_split = double_after_split
        self.max_hands = max_hands
        self.normal_pay = normal_pay
        self.blackjack_pay = blackjack_pay
        self.natural_blackjack_only = natural_blackjack_only
        self.blackjack_value = blackjack_value
        self.initial_hand_size = initial_hand_size
