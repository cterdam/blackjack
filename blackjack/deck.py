from blackjack import Card
import random


class Deck:
    def __init__(self, num_full_decks=1, include_joker=False, ordered=False):
        """
        Initializes deck.

        Params:

            num_full_decks (int): Number of full decks to include in this
                playing deck.
                Req: num_full_decks > 1

            include_joker (bool): Whether to include joker cards in each full
                deck.
                Req: None

            ordered (bool): Whether the resulting deck should be ordered.
                Req: None
        """

        """ Init param check """
        # num_full_decks should be positive int
        assert type(num_full_decks) is int
        assert num_full_decks > 0
        # include_joker should be boolean
        assert type(include_joker) is bool
        # ordered should be boolean
        assert type(ordered) is bool

        def get_single_deck(include_joker):
            result = [Card(rank, suit)
                      for rank in Card.ranks for suit in Card.suits]
            if include_joker:
                result += [Card(joker_value)
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
        If the deck is empty, returns None.

        Returns:
            if len(self) > 0
                -> c (Card)
            else
                -> None
        """
        if len(self.deck) > 0:
            return self.deck.pop()
        else:
            return None

    def insert(self, idx, c):
        """
        Inserts a card into this index.

        To insert to the top of the deck, use idx=len(Deck) so the item will
        be returned at the next draw. To insert to the bottom of the deck, use
        idx=0.

        Params:
            idx (int): An index within the deck.
                Req: None
            c (Card): The card to insert.
                Req: None

        Returns:
            None
        """
        if not isinstance(idx, int):
            raise AssertionError('Deck insertion index must be int.')
        if not isinstance(c, Card):
            raise AssertionError('Only cards can be inserted into a deck.')
        self.deck.insert(idx, c)

    def __len__(self):
        """
        Returns number of cards in deck.
        """
        return len(self.deck)

    def __eq__(self, other):
        if not isinstance(other, Deck):
            return False
        return self.deck == other.deck

    def __str__(self):
        """
        Short string representation of the deck.
        """
        return f'Deck of {len(self)} cards'

    def __repr__(self):
        """
        Long string representation of the deck.

        Returns (str):
            If the deck contains more than 3 cards
                -> 'Deck [ ♥9 ... ♣4 ]'
            Else
                -> 'Deck [ ♠K ♠2 ♣4 ]'
                -> 'Deck [ ♠2 ♣4 ]'
                -> 'Deck [ ♣4 ]'
                -> 'Deck [ ]'
            In each case the leftmost card is the top in the deck, which is in
            position for the next draw.
        """
        if len(self.deck) > 3:
            return f'Deck [ {str(self.deck[-1])} ... {str(self.deck[0])} ]'
        else:
            target = 'Deck [ '
            for c in reversed(self.deck):
                target += str(c)
                target += ' '
            target += ']'
            return target
