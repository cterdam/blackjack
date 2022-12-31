class GameConfig():

    def __init__(self, num_decks=8, reshuffle_threshold=0.25,
                 double_after_split=True, max_hands=4, late_surrender=True,
                 insurance=True, blackjack_pays=3/2):
        """
        Config for a Blackjack game.

        Params:

            num_decks (int): Number of full decks to include in this game.
            Req: num_decks > 1

            reshuffle_threshold (float or int): A special cut card will be
                inserted at this proportion in the playing deck. If the cut
                card comes up, that means the proportion of cards left in the
                deck had hit the reshuffle threshold, and the dealer will
                reshuffle the deck after the current round. A value of 0 will
                put the cut card in the bottom of the deck, and a value of 1
                will put it on top.
            Req: 0 <= reshuffle_threshold <= 1

            double_after_split (bool): Whether a player is allowed to double
                down after splitting a hand.

            max_hands (int): The max number of hands a player can obtain in a
                round by splitting. For example a value of 4 means a player
                can split at most 3 times in a round.
            Req: max_hands > 0

            late_surrender (bool): Whether a player is allowed to forgo half
                the bet and surrender after the dealer checks for blackjack.

            insurance (bool): Whether a player is allowed to make a side bet
                when the dealer is dealed an Ace, which pays 2 to 1 if the
                dealer has a blackjack.

            blackjack_pays (float or int): The ratio of pay to player for a
                naturally dealt blackjack.
        """

        if type(num_decks) is not int or num_decks < 1:
            raise AssertionError('num_decks must be a positive integer')
        if type(reshuffle_threshold) not in (float, int) or\
                not (0 <= reshuffle_threshold <= 1):
            raise AssertionError(
                'reshuffle_threshold must be a float or int with value between'
                '0 and 1 (inclusive)')
        if type(double_after_split) is not bool:
            raise AssertionError('double_after_split must be a boolean')
        if type(max_hands) is not int or max_hands < 1:
            raise AssertionError('max_hands must be a positive integer')
        if type(late_surrender) is not bool:
            raise AssertionError('late_surrender must be a boolean')

        self.num_decks = num_decks
        self.reshuffle_threshold = reshuffle_threshold
        self.double_after_split = double_after_split
        self.max_hands = max_hands
        self.late_surrender = late_surrender
