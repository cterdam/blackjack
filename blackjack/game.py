from blackjack.deck import Deck
from blackjack.card import Card


class Game():

    ############################ Define constants ############################

    # Special card to be inserted at the position of reshuffle_threshold
    # Must not be present otherwise in the play deck
    cut_card = Card(Card.LITTLE_JOKER)

    # Sum at which a hand triggers the blackjack pay if dealt naturally
    blackjack_value = 21

    # Number of cards each player starts with in a hand
    initial_hand_size = 2

    # Assign value to each card rank other than Ace
    rank2value = {Card.NUM_2: 2, Card.NUM_3: 3, Card.NUM_4: 4, Card.NUM_5: 5,
                  Card.NUM_6: 6, Card.NUM_7: 7, Card.NUM_8: 8, Card.NUM_9: 9,
                  Card.NUM_10: 10, Card.JACK: 10, Card.QUEEN: 10, Card.KING: 10}

    ##########################################################################

    def __init__(self, game_config):
        """
        Initializes game.

        Params:
            game_config (GameConfig): Config for the game.
                Req: None
        """

        self.config = game_config
        self.deck = Game._prepare_deck(self.config.num_decks,
                                       self.config.reshuffle_threshold)

    @classmethod
    def _prepare_deck(cls, num_decks, reshuffle_threshold):
        """
        Prepares a fresh deck of cards in self.deck

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
