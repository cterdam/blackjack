from blackjack import Card, Deck
import copy


class Game:
    ############################ Define constants ############################

    # Special card to be inserted at the position of reshuffle_threshold
    # Must not be present otherwise in the play deck
    cut_card = Card(Card.LITTLE_JOKER)

    ##########################################################################

    def __init__(self, game_config):
        """
        Initializes game.

        Params:
            game_config (GameConfig): Config for the game.
                Req: None
        """

        self.config = copy.deepcopy(game_config)
        self.deck = Game._prepare_deck(
            self.config.num_decks, self.config.reshuffle_threshold
        )

    @classmethod
    def _prepare_deck(cls, num_decks, reshuffle_threshold):
        """
        Prepares a fresh deck of cards

        Params:
            num_decks (int): Number of full decks to include in the play deck.
                Req: num_decks > 0

            reshuffle_threshold (int or float): The threshold at which to
                insert the special cut card signaling the time to reshuffle.
                Req: 0 <= reshuffle_threshold <= 1
        """
        d = Deck(num_full_decks=num_decks)
        d.insert(int(reshuffle_threshold * len(d)), Game.cut_card)
        return d
