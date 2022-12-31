from blackjack.deck import Deck
from blackjack.card import Card


class Game():

    # Special card to be inserted at the position of reshuffle_threshold
    cut_card = Card(None, 'Little Joker')

    def __init__(self, game_config):
        """
        Initializes game.

        Params:
            game_config (GameConfig): Config for the game.
        """

        self.config = game_config
        self.deck = self._prepare_deck(self.config)

    def _prepare_deck(self, config):
        """
        Prepares a fresh deck of cards in self.deck

        Params:
            config (GameConfig): Config for a game.
        """
        d = Deck(num_full_decks=config.num_decks)
        d.insert(int(config.reshuffle_threshold * len(d)), Game.cut_card)
        return d
