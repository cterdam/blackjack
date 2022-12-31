from blackjack.card import Card
import random


class Deck():
    def __init__(self, num_full_decks=1, include_joker=False, ordered=False):
        """
        Initializes deck.

        Params:
            num_full_decks (int): Number of full decks to include in this
                playing deck.
                Req: num_full_decks > 1
            include_joker (bool): Whether to include joker cards.
            ordered (bool): Whether the resulting deck should be ordered.
        """

        if type(num_full_decks) is not int or num_full_decks < 1:
            raise AssertionError('num_full_decks must be a positive integer')
        if type(include_joker) is not bool:
            raise AssertionError('include_joker must be a boolean')
        if type(ordered) is not bool:
            raise AssertionError('ordered must be a boolean')

        def get_single_deck(include_joker):
            result = [Card(suit, rank) for suit in Card.suits for rank in
                      Card.ranks]
            if include_joker:
                result += [Card(None, joker_value)
                           for joker_value in Card.jokers]
            return result

        self.deck = []
        for _ in range(num_full_decks):
            self.deck += get_single_deck(include_joker)

        if not ordered:
            random.shuffle(self.deck)

    def draw(self):
        """
        Removes the top card (last member of the deck array) and returns it.
        """
        return self.deck.pop()

    def count(self, item):
        """
        How many cards equal to this is present in the deck?
        """
        return self.deck.count(item)

    def insert(self, idx, item):
        """
        Inserts the item into this index
        """
        self.deck.insert(idx, item)

    def __len__(self):
        """
        Returns number of cards in deck.
        """
        return len(self.deck)

    def __getitem__(self, idx):
        return self.deck[idx]

    def __setitem__(self, key, val):
        self.deck[key] = val

    def __eq__(self, other):
        if not isinstance(other, Deck):
            return False
        return self.deck == other.deck

    def __iter__(self):
        return self

    def __next__(self):
        if len(self) == 0:
            raise StopIteration
        else:
            return self.draw()

    def __str__(self):
        return f'Deck of {len(self)} cards'

    def __repr__(self):
        return f'Deck of {len(self)} cards'
