from deck import Deck
from card import Card


class Game():

    # Special card to be inserted at the position of reshuffle_threshold
    cut_card = Card(None, 'Little Joker')

    def __init__(self, num_decks=8, reshuffle_threshold=0.25,
                 double_after_split=True, max_hands=4, late_surrender=True):
        """
        Initializes game.

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
                round by splitting a hand. For example a value of 4 means a
                player can split at most 3 times in a round.
                Req: max_hands > 0
            late_surrender (bool): Whether a player is allowed to late
                surrender (forgo half the bet after the dealer checks for
                blackjack).
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

        self._init_deck()

    def _init_deck(self):
        """
        Prepares a fresh deck of cards in self.deck
        """
        self.deck = Deck(num_full_decks=self.num_decks)
        self.deck.insert(
            int(self.reshuffle_threshold * len(self.deck)), Game.cut_card)
