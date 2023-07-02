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

        """ Init param check """
        h_wrong = False
        if not isinstance(h, list):
            h_wrong = True
        else:
            for c in h:
                if not isinstance(c, Card):
                    h_wrong = True
        if h_wrong:
            raise AssertionError('Initialization of a hand requires a list of '
                                 'cards that can be empty.')

        self.hand = h.copy()
        num_aces, hard_total = Hand._breakdown(self.hand)

        self.num_aces = num_aces
        self.hard_total = hard_total
        self.total = Hand._calc_total(num_aces, hard_total)
        self.uniform_value = Hand._get_uniform_value(self.hand)

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
            if c.is_ace():
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

    @classmethod
    def _get_uniform_value(cls, h):
        """
        Determine if the list contains some cards of the same rank value.

        Params:
            h (list of Card): list of cards to survey.
                Req: None

        Returns:
            if h contains at lease one card and all cards in the list are the
                same rank
                -> rank, where
                    - rank in Card.ranks
                    - rank is the common rank of all cards in h
            else (if h is empty, or if at least two cards differ in rank)
                -> None
        """
        ranks = {c.rank for c in h}
        if len(ranks) == 1:
            return h[0].rank
        else:
            return None

    def add(self, newcard):
        """
        Add a new card into this hand.

        Params:
            newcard (Card): The new card to input.
                Req: None

        Returns:
            self (Hand) after adding the card and updating data.
        """
        self.hand.append(newcard)
        if newcard.is_ace():
            self.num_aces += 1
        else:
            self.hard_total += Game.rank2value[newcard.rank]
        self.total = Hand._calc_total(self.num_aces, self.hard_total)
        if self.uniform_value != None:
            if newcard.rank != self.uniform_value:
                self.uniform_value = None
        else:
            if len(self.hand) == 1:
                self.uniform_value = self.hand[0].rank

        return self
    
    def explode(h):
        """
        Creates a separate hand for each card in the current hand. 

        Params:
            h (list of Card): list of cards to survey.
                Req: None

        Returns:
            A list of hand objects, where each contains a single card 
            from the original hand. 
        """
        return [Hand([c]) for c in h] 

    def __eq__(self, other):
        """
        Two hands are equal when they are equal in num_aces, hard_total,
        total, and uniform_value.
        """
        if not isinstance(other, Hand):
            return False
        return self.num_aces == other.num_aces\
            and self.hard_total == other.hard_total\
            and self.total == other.total\
            and self.uniform_value == other.uniform_value

    def __str__(self):
        """
        Short string representation of the hand.
        """
        return f'Hand of {len(self.hand)} cards'

    def __repr__(self):
        """
        Long string representation of the hand.

        Returns (str):
            Examples:
                -> 'Hand [ ♥9 ♠K ♠2 ♣4 ]'
                -> 'Hand [ ♠K ♠2 ♣4 ]'
                -> 'Hand [ ♠2 ♣4 ]'
                -> 'Hand [ ♣4 ]'
                -> 'Hand [ ]'
            In each case the cards are shown in the same order as the hand,
            where the furthest left card is first in the hand.
        """
        target = 'Hand [ '
        for c in self.hand:
            target += str(c)
            target += ' '
        target += ']'
        return target
