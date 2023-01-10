from blackjack.card import Card
from blackjack.game import Game


class Hand():

    ############################ Define constants ############################

    # Indicators for soft and hard hand totals
    SOFT = 'Soft'
    HARD = 'Hard'

    ##########################################################################

    def __init__(self, h=[]):
        """
        Initialize the hand.

        Params:
            h (list of Card): A list of cards to start with. Default to empty.
                Req: None
        """

        # Init param check
        h_wrong = False
        if not isinstance(h, list):
            h_wrong = True
        else:
            for c in h:
                if not isinstance(c, Card):
                    h_wrong = True
        if h_wrong:
            raise AssertionError('initialization of a hand requires a list of '
                                 'cards that can be empty.')

        self.hand = h
        num_aces, hard_total = Hand._breakdown(self.hand)
        self.num_aces = num_aces
        self.hard_total = hard_total
        self.total = Hand._calc_total(num_aces, hard_total)

    @classmethod
    def _breakdown(cls, h):
        """
        Breaks down the list of cards into num_aces and hard_total.

        Params:
            h (List of Card): List of cards to break down.
                Req: None

        Returns (tuple): (num_aces, hard_total) where
            num_aces (int) -> the number of Ace cards in the list
                Inv: num_aces >= 0
            hard_total (int) -> the sum of values of all non-Ace cards in the
                list
                Inv: hard_total >= 0
        """
        num_aces = 0
        hard_total = 0
        for c in h:
            if c.is_ace:
                num_aces += 1
            else:
                hard_total += Game.rank2value[c.rank]
        return num_aces, hard_total

    @classmethod
    def _calc_total(cls, num_aces, hard_total):
        """
        Calculates the total for the current num_aces and hard_total.

        Params:
            num_aces (int): The number of Ace cards in the hand.
                Req: num_aces >= 0
            hard_total (int): The sum of values of all non-Ace cards in the
                hand.
                Req: hard_total >= 0

        Returns (tuple): (mode, value) where
            mode -> is in (Hand.SOFT, Hand.HARD).
            value (int) -> total of this hand.
        """

        # If no ace, hand total is hard total
        if num_aces == 0:
            return (Hand.HARD, hard_total)

        # There is at least one Ace
        less_one_ace = hard_total + num_aces - 1
        if less_one_ace <= 10:
            # Soft total, one ace counts as 11
            return (Hand.SOFT, less_one_ace + 11)
        else:
            # Hard total, all aces count as 1
            return (Hand.HARD, less_one_ace + 1)
