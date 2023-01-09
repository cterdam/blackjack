import random


class Card():

    ############################ Define constants ############################

    # Suits
    CLUBS = 'Clubs'
    DIAMONDS = 'Diamonds'
    HEARTS = 'Hearts'
    SPADES = 'Spades'

    # Numbers
    NUM_2 = '2'
    NUM_3 = '3'
    NUM_4 = '4'
    NUM_5 = '5'
    NUM_6 = '6'
    NUM_7 = '7'
    NUM_8 = '8'
    NUM_9 = '9'
    NUM_10 = '10'

    # Faces
    JACK = 'Jack'
    QUEEN = 'Queen'
    KING = 'King'

    # Ace
    ACE = 'Ace'

    # Jokers
    LITTLE_JOKER = 'Little Joker'
    BIG_JOKER = 'Big Joker'

    # Flag for initializing a random card
    RANDOM_FLAG = 'Random Flag'
    JOKER_SUIT = 'Joker Suit'

    # Collections
    suits = (CLUBS, DIAMONDS, HEARTS, SPADES)
    numbers = (NUM_2, NUM_3, NUM_4, NUM_5, NUM_6, NUM_7, NUM_8, NUM_9, NUM_10)
    faces = (JACK, QUEEN, KING)
    ranks = (ACE,) + numbers + faces
    jokers = (LITTLE_JOKER, BIG_JOKER)

    # Representation dictionaries
    rank2str = {ACE: 'A', NUM_2: '2', NUM_3: '3', NUM_4: '4', NUM_5: '5',
                NUM_6: '6', NUM_7: '7', NUM_8: '8', NUM_9: '9', NUM_10: '10',
                JACK: 'J', QUEEN: 'Q', KING: 'K',
                LITTLE_JOKER: 'Little Joker', BIG_JOKER: 'Big Joker'}
    suit2str = {CLUBS: '♣', DIAMONDS: '♦', HEARTS: '♥', SPADES: '♠',
                JOKER_SUIT: ''}
    rank2repr = {ACE: 'Ace', NUM_2: '2', NUM_3: '3', NUM_4: '4', NUM_5: '5',
                 NUM_6: '6', NUM_7: '7', NUM_8: '8', NUM_9: '9', NUM_10: '10',
                 JACK: 'Jack', QUEEN: 'Queen', KING: 'King',
                 LITTLE_JOKER: 'Little Joker', BIG_JOKER: 'Big Joker'}
    suit2repr = {CLUBS: 'Clubs', DIAMONDS: 'Diamonds', HEARTS: 'Hearts',
                 SPADES: 'Spades', JOKER_SUIT: ''}

    ##########################################################################

    def __init__(self, rank=RANDOM_FLAG, suit=JOKER_SUIT):
        """
        Initializes card.

        Params: rank, suit.
        Req: either (rank in Card.ranks and suit in Card.suits)
                -> given rank, given suit
             or     (rank in Card.jokers and suit == Card.JOKER_SUIT)
                -> given joker rank, joker suit
             or     (rank in Card.ranks and suit == Card.JOKER_SUIT)
                -> given rank, random suit
             or     (rank in Card.suits and suit == Card.JOKER_SUIT)
                -> random rank, given suit
             or     (rank == Card.RANDOM_FLAG and suit == Card.JOKER_SUIT)
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

        # Initialization param check
        invalid_param = AssertionError('Invalid initialization parameters.')

        if rank in Card.ranks:
            if suit in Card.suits:
                # Given rank, given suit
                pass
            elif suit == Card.JOKER_SUIT:
                # Given rank, random suit
                suit = Card.random_suit()
            else:
                raise invalid_param

        elif rank in Card.jokers:
            if suit == Card.JOKER_SUIT:
                # Given joker card
                pass
            else:
                raise invalid_param

        elif rank in Card.suits:
            if suit == Card.JOKER_SUIT:
                # Random rank, given suit
                suit = rank
                rank = Card.random_rank()
            else:
                raise invalid_param

        elif rank == Card.RANDOM_FLAG:
            if suit == Card.JOKER_SUIT:
                # Random rank, random suit
                rank = Card.random_rank()
                suit = Card.random_suit()
            else:
                raise invalid_param

        else:
            raise invalid_param

        self.rank = rank
        self.suit = suit

        # Properties
        self.is_ace = self.rank == Card.ACE
        self.is_number = self.rank in Card.numbers
        self.is_face = self.rank in Card.faces
        self.is_joker = self.rank in Card.jokers

        # Short string representation
        # ♣A, ♥2, ♦Q, Big Joker
        self.str = Card.suit2str[self.suit] + Card.rank2str[self.rank]

        # Long string representation
        # Ace of Clubs, 2 of Hearts, Queen of Diamonds, Big Joker
        self.repr = Card.rank2repr[self.rank] + \
            (' of ' if not self.is_joker else '') + Card.suit2repr[self.suit]

    def __str__(self):
        """
        Gives the short string representation of the card.

        Returns (str):
            For ordinary cards
                -> 'IV' where I is a suit icon, and V is the value in short
            For joker cards
                -> 'Little Joker' or 'Big Joker'

        Examples:
            '♥A', '♣3', 'Big Joker'
        """
        return self.str

    def __repr__(self):
        """
        Gives the long string representation of the card.

        Returns (str):
            For ordinary cards
                -> 'V of S' where V is the value repr, and S is the suit repr
            For joker cards
                -> 'Little Joker' or 'Big Joker'

        Examples:
            'Ace of Hearts', '3 of Clubs', 'Big Joker'

        """
        return self.repr

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
    def random_rank(cls):
        """
        Returns a random rank from Card.ranks, excluding joker ranks in
        Card.jokers.
        """
        return random.sample(Card.ranks, 1)[0]

    @classmethod
    def random_suit(cls):
        """
        Returns a random suit from Card.suits, excluding Card.JOKER_SUIT.
        """
        return random.sample(Card.suits, 1)[0]
