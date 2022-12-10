from deck import Deck


class Game():

    cut_card = 'CUTCARD'

    def __init__(self, num_decks=8, shuffle_threshold=0.25,
                 double_after_split=True, max_hands=4, late_surrender=True):
        self.deck = Deck(num_full_decks=num_decks)
        self.deck.insert(
            int(shuffle_threshold * len(self.deck)), Game.cut_card)
