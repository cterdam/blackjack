from abc import ABC, abstractmethod


class Player(ABC):
    @abstractmethod
    def __init__(self, name="", bankroll=0):
        """
        Initializes player.

        Params:
            name (str): The player's name.
                Req: None
            bankroll (int): The player's starting bankroll.
                Req: bankroll >= 0
        """
        pass

    @abstractmethod
    def sit_down(self, game_config):
        """
        Notifies the player that they are playing in a game.

        Params:
            game_config (GameConfig): The game_config of the game they will 
                begin playing in.
                Req: None
        """
        pass

    @abstractmethod
    def place_bet(self):
        """
        Places the player's bet for a round.

        Returns (int):
            bet -> The amount the player is betting.
            Inv: bet >= 0

        Side Effects:
            -> Subtracts the bet amount from the player's bankroll.
            -> Initialize the hand list the player will play with this round.
        """
        pass

    @abstractmethod
    def observe_card(self, card, player):
        """
        Notifies the player of a card being assigned to some player.

        Params:
            card (Card): The card to be observed.
                Req: None
            player (int): The seat number of the player who received the card.
                Req: player >= 0
        """
        pass

    @abstractmethod
    def has_hand(self):
        """
        Determines whether the player is looking at a meaningful hand.

        Returns (bool):
            -> True if the player has a hand they are currently focusing on.
            -> False otherwise.
        """
        pass

    @abstractmethod
    def curr_hand(self):
        """
        Returns the hand object the player is current focusing on.

        Returns (Hand):
            The hand the player is currently playing with.
        """
        pass

    @abstractmethod
    def next_hand(self):
        """
        Notifies the player to switch to focusing on their next hand.

        Side Effects:
            -> Player switches to focus on next hand, if one exists
        """
        pass

    @abstractmethod
    def decide_split(self):
        """
        Determines whether the player wishes to split their hand.

        Returns (bool):
            -> True if the player wishes to split their current hand
            -> False otherwise

        Side Effects:
            -> Subtracts the additional bet from the bankroll if the player
                decides to split.
        """
        pass

    @abstractmethod
    def decide_surrender(self):
        """
        Determine whether the player wishes to surrender their hand.

        Returns (bool):
            -> True if the player wishes to surrender their current hand
            -> False otherwise
        """
        pass

    @abstractmethod
    def decide_double(self):
        """
        Determine whether the player wishes to double their hand.

        Returns (bool):
            -> True if the player wishes to double their current hand
            -> False otherwise

        Side Effects:
            -> Subtracts the additional bet from the bankroll if the player
                decides to double.
        """
        pass

    @abstractmethod
    def decide_hit(self):
        """
        Determine whether the player wishes to hit their hand.

        Returns (bool):
            -> True if the player wishes to hit their current hand
            -> False otherwise
        """
        pass

    @abstractmethod
    def payout(self, payout):
        """
        Gives the player a payout for their current hand.

        Params:
            payout (int): The amount to pay out to the player.
                Req: payout >= 0

        Side Effects:
            -> Adds the payout to the player's bankroll.
        """
        pass

    def __str__(self):
        """
        Short string representation of the player.

        Returns (str):
            -> 'N' where N is the player's name
        """
        return self.name

    def __repr__(self):
        """
        Long string representation of the player.

        Returns (str):
            'Player(N, B)' where 
                -> N is the player's name
                -> B is the player's bankroll
        """
        return f'Player({self.name}, {self.bankroll})'
