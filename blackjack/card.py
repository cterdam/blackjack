import random


class Card():

    ############################ Define constants ############################

    # Suits
    CLUBS = 'Clubs'
    DIAMONDS = 'Diamonds'
    HEARTS = 'Hearts'
    SPADES = 'Spades'
    JOKER_SUIT = None

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

    RANDOM_FLAG = 'Random Flag'

    ##########################################################################

    def __init__(self, rank=RANDOM_FLAG, suit=JOKER_SUIT):
        """
        Initializes card.

        Params: rank, suit.
        Req: either (rank in Card.ranks and suit in Card.suits)
             or     (rank in Card.jokers and suit == Card.JOKER_SUIT)

        Examples:
            >>> from blackjack.card import Card
            >>> Card(Card.NUM_2, Card.SPADES)
            >>> Card(Card.QUEEN, Card.DIAMONDS)
            >>> Card(Card.LITTLE_JOKER)
        """

        if rank == Card.RANDOM_FLAG:
            target = Card.random()
            suit, rank = target.suit, target.rank

        if not (rank in Card.ranks and suit in Card.suits) and\
                not (rank in Card.jokers and suit == Card.JOKER_SUIT):
            raise AssertionError('Invalid initialization parameters. For '
                                 'ordinary cards, rank must be in Card.ranks '
                                 'and suit must be in Card.suits. For joker '
                                 'cards, rank must be in Card.jokers and suit '
                                 f'must be None. Got rank = {rank} and suit = '
                                 f'{suit}.')

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
    def random(cls, include_joker=False):
        """
        Returns a random card. This is not the same as returning a random
        member of a playing deck. Running this function n times, across all
        trials the distribution of all possible outcomes is the same.
        """
        if include_joker:
            rank = random.sample(Card.ranks+Card.jokers, 1)[0]
            if rank in Card.ranks:
                suit = random.sample(Card.suits, 1)[0]
            else:
                suit = Card.JOKER_SUIT
            return Card(rank, suit)
        else:
            rank = random.sample(Card.ranks, 1)[0]
            suit = random.sample(Card.suits, 1)[0]
            return Card(rank, suit)
