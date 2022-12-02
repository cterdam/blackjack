import random


class Card():

    suits = ('Clubs', 'Diamonds', 'Hearts', 'Spades')
    numbers = (2, 3, 4, 5, 6, 7, 8, 9, 10)
    faces = ('Jack', 'Queen', 'King')
    ranks = ('Ace',) + numbers + faces
    special_values = ('Little Joker', 'Big Joker')
    suit2icon = {'Clubs': '♣', 'Diamonds': '♦', 'Hearts': '♥', 'Spades': '♠'}
    rank2str = {'Ace': 'A', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8:
                '8', 9: '9', 10: '10', 'Jack': 'J', 'Queen': 'Q', 'King': 'K'}

    def __init__(self, suit, rank):

        if suit != None:
            # Ordinary card
            assert suit in Card.suits
            assert rank in Card.ranks
        else:
            # Special card
            assert self.suit == None
            assert rank in Card.special_values

        self.suit = suit
        self.rank = rank

    def is_ace(self):
        return self.rank == 'Ace'

    def is_number(self):
        return self.rank in Card.numbers

    def is_face(self):
        return self.rank in Card.faces

    def is_special(self):
        return self.rank in Card.special_values

    def __str__(self):
        if not self.is_special():
            return Card.suit2icon[self.suit]+Card.rank2str[self.rank]
        else:
            return str(self.rank)

    def __repr__(self):
        if not self.is_special():
            return str(self.rank) + ' of ' + str(self.suit)
        else:
            return str(self.rank)

    def __eq__(self, other):
        return self.suit == other.suit and self.rank == other.rank

    def __hash__(self):
        return hash((self.suit, self.rank))

    @classmethod
    def random(cls, include_special=False):
        if include_special:
            rank = random.sample(Card.ranks+Card.special_values, 1)[0]
            if rank in Card.ranks:
                suit = random.sample(Card.suits, 1)[0]
            else:
                suit = None
            return Card(suit, rank)
        else:
            rank = random.sample(Card.ranks, 1)[0]
            suit = random.sample(Card.suits, 1)[0]
            return Card(suit, rank)
