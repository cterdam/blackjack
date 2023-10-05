from blackjack import Card, GameConfig
from enum import Enum, auto, unique


class Hand:

    ############################ Define constants ############################

    @unique
    class Constants(Enum):
        """ Define constants for Hand class """
        SOFT = auto()
        HARD = auto()

    # Indicators for soft and hard hand totals
    SOFT = Constants.SOFT
    HARD = Constants.HARD

    ##########################################################################

    def __init__(self,
                 cards=[],
                 blackjack_value=GameConfig.Defaults.blackjack_value,
                 valuation=GameConfig.Defaults.valuation):
        """
        Initialize the hand.

        Params:

            cards (list of Card): List of cards to start with. Default to
                empty.
                Req: None

            blackjack_value (int or float): Sum at which a hand triggers the
                blackjack pay if dealt naturally.
                Req: blackjack_value > 0

            valuation (dict): The value each possible Card rank can take.
                Req: The keys should include all Card ranks (excluding
                    jokers), and a value should be either a number (int or
                    float), or a tuple of length more than 1 containing
                    numbers (int or float), where the rank can take on any
                    value within the tuple. In the tuple case, all values in
                    the tuple must be distinct.
        """

        """ Init param check """

        # Check cards
        assert isinstance(cards, list)
        for c in cards:
            assert isinstance(c, Card)

        # Check blackjack value
        assert type(blackjack_value) in (int, float)

        # Check valuation
        assert GameConfig.is_valid_valuation(valuation)

        """ Assign attributes """

        # Store attributes
        self.cards = cards.copy()
        self._blackjack_value = blackjack_value
        self._valuation = valuation.copy()

        # Compute tally
        #   tally dict should include every card rank as key
        self._tally = {rank: 0 for rank in Card.ranks}
        for card in cards:
            self._tally[card.rank] += 1

        # Compute uniform value
        self.uniform_value = valuation[cards[0].rank] if len(
            {valuation[card.rank] for card in cards}) == 1 else None

        # Compute total
        self._soft_tuples = []
        self._hard_total = 0
        for card in cards:
            if type(valuation[card.rank]) is tuple:
                self._soft_tuples.append(valuation[card.rank])
            else:
                self._hard_total += self._valuation[card.rank]
        self.total = self._calc_total()

    def _calc_total(self):
        """
        Calculates the total for the current Hand.

        Params: None

        Returns (tuple): (mode, value) where
            mode -> is in (Hand.SOFT, Hand.HARD).
                Hand.SOFT if there is at least one soft card which takes a
                    non-minimum value.
                Hand.HARD if there is no soft cards or all soft cards take
                    their minimum value.
            value (int or float) -> total of this hand.
        """

        pass

    def add(self, newcard):
        """
        Add a new card into this hand.

        Params:
            newcard (Card): The new card to input.
                Req: None

        Returns:
            self (Hand) after adding the card and updating data.
        """

        self.cards.append(newcard)
        self._tally[newcard.rank] += 1

        # Update hard total / soft cards

        # Update total

        # Update uniform value
        if self.uniform_value != None:
            if newcard.rank != self.uniform_value:
                self.uniform_value = None
        else:
            if len(self.cards) == 1:
                self.uniform_value = self.cards[0].rank

        return self

    # def explode(self):
    #     """
    #     Creates a separate hand for each card in the current hand.

    #     Params: None

    #     Returns:
    #         A list of hand objects each containing a single card from the
    #         original hand.
    #     """
    #     return [Hand(c) for c in self.hand]

    def __eq__(self, other):
        """
        Two hands are equal when they contain the same card ranks, regardless of
            order.
        """
        if not isinstance(other, Hand):
            return False
        return self._tally == other._tally

    def __str__(self):
        """
        Short string representation of the hand.
        """
        return f'Hand of {len(self.cards)} cards'

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
        for c in self.cards:
            target += str(c)
            target += ' '
        target += ']'
        return target
