from blackjack.player import Player
from blackjack.card import Card
from blackjack.hand import Hand
from blackjack.game_config import GameConfig


class ThresholdPlayer(Player):
    def __init__(self, name="", bankroll=float('inf'),
                 hard_threshold=17, soft_threshold=17, bet=1):
        """
        Initializes threshold player.

        Params:
            name (str): The player's name.
                Req: None
            bankroll (int or float): The player's starting bankroll.
                Req: bankroll >= 0
            hard_threshold (int): The minimum hard total player will stand at.
                Req: hard_threshold >= 0
            hard_threshold (int): The minimum soft total player will stand at.
                Req: soft_threshold >= 0
            bet (int or float): The constant bet player will make each round.
                If bet is a float, it will be rounded down if the player plays
                a game with int_bet_only enabled.
                Req: bet >= 0
        """

        """ Init param check """
        invalid_param = AssertionError('Invalid initialization parameters.')
        if not isinstance(name, str):
            raise invalid_param
        # Each of these arguments must be non-negative integers
        if type(bankroll) not in (int, float) or bankroll < 0:
            raise invalid_param
        if not isinstance(hard_threshold, int) or hard_threshold < 0:
            raise invalid_param
        if not isinstance(soft_threshold, int) or soft_threshold < 0:
            raise invalid_param
        if type(bet) not in (int, float) or bet < 0:
            raise invalid_param

        # Initialize Basic Player Information
        self.name = name
        self.bankroll = bankroll
        self.dealer = False

        # Initialize Threshold Player-Specific Information
        self.soft_threshold = soft_threshold
        self.hard_threshold = hard_threshold
        self.bet = bet

        # Initialize Game-Dependent Information
        self._game_config = None
        self._hands = None
        self._hand_index = None

    def sit_down(self, game_config):
        """
        Notifies the player that they are playing in a game.

        Params:
            game_config (GameConfig): The game_config of the game they will
                begin playing in.
                Req: None
        """

        """ Param check """
        if not isinstance(game_config, GameConfig):
            raise AssertionError('Invalid parameters.')

        self._game_config = game_config
        self._hands = None
        self._hand_index = None

    def place_bet(self):
        """
        Places the player's bet for a round. Only callable if player has
        already sat down.

        Returns (int):
            bet -> The amount the player is betting.
            Inv: 0 <= bet <= bankroll, where bankroll is the player's bankroll

        Side Effects:
            -> Subtracts the bet amount from the player's bankroll.
            -> Initialize the hand list the player will play with this round.
        """
        if self._game_config is None:
            raise AssertionError('Player must sit down before placing a bet.')

        if self._game_config.int_bet_only:
            bet = min(self.bankroll, int(self.bet))
        else:
            bet = min(self.bankroll, self.bet)

        self.bankroll -= bet
        if bet > 0:
            self._hands = [Hand()]
            self._hand_index = 0
        else:
            self._hands = None
            self._hand_index = None
        return bet

    def observe_card(self, card, player):
        """
        Notifies the player of a card being assigned to some player. Only
        callable if the player has already placed a bet.

        Params:
            card (Card): The card to be observed.
                Req: None
            player (int): The seat number of the player who received the card.
                Req: player >= 0
        """
        if not isinstance(self._game_config, GameConfig):
            raise AssertionError("Player can't observe card if not in a game.")
        if not isinstance(card, Card):
            raise AssertionError("Invalid params")
        if not isinstance(player, int) or player < 0:
            raise AssertionError("Invalid params")
        pass

    def has_hand(self):
        """
        Determines whether the player is looking at a meaningful hand.

        Returns (bool):
            -> True if the player has a hand they are currently focusing on.
            -> False otherwise.
        """
        if not isinstance(self._hands, list):
            return False
        if not isinstance(self._hand_index, int):
            return False
        if self._hand_index < 0 or self._hand_index >= len(self._hands):
            return False
        if not isinstance(self._hands[self._hand_index], Hand):
            return False
        return True

    def curr_hand(self):
        """
        Returns the hand object the player is current focusing on, if it exists.

        Returns:
            if the player is currently playing with a hand
                -> (Hand) the hand the player is playing with
            else
                -> None
        """
        if not self.has_hand():
            return None
        return self._hands[self._hand_index]

    def next_hand(self):
        """
        Notifies the player to switch to focusing on their next hand.

        Side Effects:
            -> Player switches to focus on next hand, if one exists
        """
        if isinstance(self._hand_index, int):
            self._hand_index += 1

    def decide_insurance(self):
        """
        Determines whether the player wishes to take insurance. Only callable
        if the player has already placed a bet.

        Returns (bool):
            -> True if the player wishes to take insurance.
            -> False otherwise.

        Side
        """
        if not self.has_hand():
            raise AssertionError("Player cannot decide before placing a bet.")

        return False

    def decide_split(self):
        """
        Determines whether the player wishes to split their hand. Only
        callable if the player has already placed a bet.

        Returns (bool):
            -> True if the player wishes to split their current hand.
            -> False otherwise.

        Side Effects:
            -> Subtracts the additional bet from the bankroll if the player
                decides to split.
        """
        if not self.has_hand():
            raise AssertionError("Player cannot decide without a hand.")

        return False

    def decide_surrender(self):
        """
        Determine whether the player wishes to surrender their hand. Only
        callable if the player has already placed a bet.

        Returns (bool):
            -> True if the player wishes to surrender their current hand.
            -> False otherwise.
        """
        if not self.has_hand():
            raise AssertionError("Player cannot decide without a hand.")

        return False

    def decide_double(self):
        """
        Determine whether the player wishes to double their hand. Only
        callable if the player has already placed a bet.

        Returns (bool):
            -> True if the player wishes to double their current hand.
            -> False otherwise.

        Side Effects:
            -> Subtracts the additional bet from the bankroll if the player
                decides to double.
        """
        if not self.has_hand():
            raise AssertionError("Player cannot decide without a hand.")

        return False

    def decide_hit(self):
        """
        Determine whether the player wishes to hit their hand. Only callable
        if the player has already placed a bet.

        Returns (bool):
            -> True if the player wishes to hit their current hand.
            -> False otherwise.
        """
        if not self.has_hand():
            raise AssertionError("Player cannot decide without a hand.")

        hand_type, total = self._hands[self._hand_index].total
        if hand_type == Hand.HARD:
            # Hand is Hard, Hit based on Hard total
            return total < self.hard_threshold
        else:
            # Hand is Soft, Hit based on Soft total
            return total < self.soft_threshold

    def insurance_payout(self, payout):
        """
        Gives the player payout for their insurance bet, and ends the round
        that began with the previous place_bet call.

        Params:
            payout (int or float): The amount to payout to the player.
                Req: payout >= 0

        Side Effects:
            -> Adds payout to the player's bankroll.
            -> Reset's the player's hand.
        """
        if not isinstance(self._hands, list):
            raise AssertionError(
                "Cannot payout a Player before they begin a round")
        if type(payout) not in (int, float) or payout < 0:
            raise AssertionError("Invalid parameters.")

        self.bankroll += payout
        self._hands = None
        self._hand_index = None

    def final_payout(self, payouts):
        """
        Gives the player payouts for their current hands, and ends the round
        that began with the previous place_bet call.

        Params:
            payouts (int list or float list): The amount to pay out to 
            the player for each hand.
                Req: 
                    -> len(payouts) is the number of hands the player is playing
                        with
                    -> payouts[i] >= 0 for all 0 <= i < len(payouts)

        Side Effects:
            -> Adds each payout to the player's bankroll.
        """

        """ Param Check """
        if not isinstance(self._hands, list):
            raise AssertionError(
                "Cannot payout a Player before they begin a round")
        if not isinstance(payouts, list):
            raise AssertionError("Invalid parameters.")
        if len(payouts) != len(self._hands):
            raise AssertionError("Invalid parameters.")
        for payout in payouts:
            if type(payout) not in (int, float) or payout < 0:
                raise AssertionError("Invalid parameters.")

        self.bankroll += sum(payouts)

        # Reset Hand
        self._hands = None
        self._hand_index = None
