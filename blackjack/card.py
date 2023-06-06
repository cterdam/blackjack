import random
from enum import Enum, auto, unique


class Card:

    ############################ Define constants ############################

    @unique
    class Constants(Enum):
        """ Define constants for Card class """

        # Suits
        CLUBS = auto()
        DIAMONDS = auto()
        HEARTS = auto()
        SPADES = auto()

        # Numbers
        NUM_2 = auto()
        NUM_3 = auto()
        NUM_4 = auto()
        NUM_5 = auto()
        NUM_6 = auto()
        NUM_7 = auto()
        NUM_8 = auto()
        NUM_9 = auto()
        NUM_10 = auto()

        # Faces
        JACK = auto()
        QUEEN = auto()
        KING = auto()

        # Ace
        ACE = auto()

        # Jokers
        LITTLE_JOKER = auto()
        BIG_JOKER = auto()

        # Flag for initializing a random card
        RANDOM = auto()

    """ Collect these constants from Constants class """

    # Suits
    CLUBS = Constants.CLUBS
    DIAMONDS = Constants.DIAMONDS
    HEARTS = Constants.HEARTS
    SPADES = Constants.SPADES

    # Numbers
    NUM_2 = Constants.NUM_2
    NUM_3 = Constants.NUM_3
    NUM_4 = Constants.NUM_4
    NUM_5 = Constants.NUM_5
    NUM_6 = Constants.NUM_6
    NUM_7 = Constants.NUM_7
    NUM_8 = Constants.NUM_8
    NUM_9 = Constants.NUM_9
    NUM_10 = Constants.NUM_10

    # Faces
    JACK = Constants.JACK
    QUEEN = Constants.QUEEN
    KING = Constants.KING

    # Ace
    ACE = Constants.ACE

    # Jokers
    LITTLE_JOKER = Constants.LITTLE_JOKER
    BIG_JOKER = Constants.BIG_JOKER

    # Flag for initializing a random card
    RANDOM = Constants.RANDOM

    """ Define other collections """

    # Collections
    suits = (CLUBS, DIAMONDS, HEARTS, SPADES)
    numbers = (NUM_2, NUM_3, NUM_4, NUM_5, NUM_6, NUM_7, NUM_8, NUM_9, NUM_10)
    faces = (JACK, QUEEN, KING)
    ranks = (ACE,) + numbers + faces
    jokers = (LITTLE_JOKER, BIG_JOKER)

    # Representation
    _rank2str = {ACE: 'A', NUM_2: '2', NUM_3: '3', NUM_4: '4', NUM_5: '5',
                 NUM_6: '6', NUM_7: '7', NUM_8: '8', NUM_9: '9', NUM_10: '10',
                 JACK: 'J', QUEEN: 'Q', KING: 'K',
                 LITTLE_JOKER: 'Little Joker', BIG_JOKER: 'Big Joker'}
    _suit2str = {CLUBS: '♣', DIAMONDS: '♦', HEARTS: '♥', SPADES: '♠',
                 RANDOM: ''}
    _rank2repr = {ACE: 'Ace', NUM_2: '2', NUM_3: '3', NUM_4: '4', NUM_5: '5',
                  NUM_6: '6', NUM_7: '7', NUM_8: '8', NUM_9: '9', NUM_10: '10',
                  JACK: 'Jack', QUEEN: 'Queen', KING: 'King',
                  LITTLE_JOKER: 'Little Joker', BIG_JOKER: 'Big Joker'}
    _suit2repr = {CLUBS: 'Clubs', DIAMONDS: 'Diamonds', HEARTS: 'Hearts',
                  SPADES: 'Spades', RANDOM: ''}

    ##########################################################################

    def __init__(self, rank=RANDOM, suit=RANDOM):
        """
        Initializes card.

        Params: rank, suit.
        Req: either (rank in Card.ranks and suit in Card.suits)
                -> given rank, given suit
             or     (rank in Card.jokers and suit == Card.RANDOM)
                -> given joker rank, joker suit
             or     (rank in Card.ranks and suit == Card.RANDOM)
                -> given rank, random suit
             or     (rank in Card.suits and suit == Card.RANDOM)
                -> given suit, random rank
             or     (rank == Card.RANDOM and suit == Card.RANDOM)
                -> random rank, random suit (excluding jokers)

        Examples:
            >>> from blackjack.card import Card

            >>> Card(Card.NUM_2, Card.SPADES)   # Spawns 2 of Spades
            >>> Card(Card.QUEEN, Card.DIAMONDS) # Spawns Queen of Diamonds
            >>> Card(Card.LITTLE_JOKER)         # Spawns Little Joker

            >>> Card(Card.NUM_6)  # Spawns a 6 with a random suit
            >>> Card(Card.HEARTS) # Spawns a Hearts card with a random rank
            >>> Card()            # Spawns a random card excluding jokers
        """

        """ Init param check """
        invalid_param = AssertionError('Invalid initialization parameters.')

        if rank in Card.ranks:
            if suit in Card.suits:
                # Given rank, given suit
                pass
            elif suit == Card.RANDOM:
                # Given rank, random suit
                suit = Card._random_suit()
            else:
                raise invalid_param

        elif rank in Card.jokers:
            if suit == Card.RANDOM:
                # Given joker card
                pass
            else:
                raise invalid_param

        elif rank in Card.suits:
            if suit == Card.RANDOM:
                # Random rank, given suit
                suit = rank
                rank = Card._random_rank()
            else:
                raise invalid_param

        elif rank == Card.RANDOM:
            if suit == Card.RANDOM:
                # Random rank, random suit
                rank = Card._random_rank()
                suit = Card._random_suit()
            else:
                raise invalid_param

        else:
            raise invalid_param

        self.rank = rank
        self.suit = suit

    def is_ace(self):
        """ Returns True iff the rank is Ace.  """
        return self.rank == Card.ACE

    def is_number(self):
        """ Returns True iff the rank is a number (2-10).  """
        return self.rank in Card.numbers

    def is_face(self):
        """ Returns True iff the rank is a Face card (J, Q, K). """
        return self.rank in Card.faces

    def is_joker(self):
        """ Returns True iff the card is a Joker card. """
        return self.rank in Card.jokers

    def __str__(self):
        """
        Gives the short string representation of the card.

        Returns(str):
            For ordinary cards
                -> 'IV' where I is a suit icon, and V is the value in short
            For joker cards
                -> 'Little Joker' or 'Big Joker'

        Examples:
            '♥A', '♣3', 'Big Joker'
        """
        return Card._suit2str[self.suit] + Card._rank2str[self.rank]

    def __repr__(self):
        """
        Gives the long string representation of the card.

        Returns(str):
            For ordinary cards
                -> 'V of S' where V is the value repr, and S is the suit repr
            For joker cards
                -> 'Little Joker' or 'Big Joker'

        Examples:
            'Ace of Hearts', '3 of Clubs', 'Big Joker'

        """
        return Card._rank2repr[self.rank] + \
            (' of ' if not self.is_joker() else '') + \
            Card._suit2repr[self.suit]

    def __eq__(self, other):
        """
        Two cards are equal when their suits and ranks are both equal.
        """
        if not isinstance(other, Card):
            return False
        return self.rank == other.rank and self.suit == other.suit

    def __hash__(self):
        return hash((self.rank, self.suit))

    @classmethod
    def _random_rank(cls):
        """
        Returns a random rank from Card.ranks, excluding joker ranks in
        Card.jokers.
        """
        return random.sample(Card.ranks, 1)[0]

    @classmethod
    def _random_suit(cls):
        """
        Returns a random suit from Card.suits
        """
        return random.sample(Card.suits, 1)[0]
