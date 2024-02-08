import random


class Player:
    """
    Represents a player in the Snap game.

    Attributes:
        name (str): The name of the player.
        pile (list): The pile of cards that the player holds.
        stack (list): The stack of cards that the player has played.
    """

    def __init__(self, name):
        self.name = name
        self.pile = []
        self.stack = []

    def play_card(self):
        """
        Play the top card from the player's pile and move it to the stack.
        """
        card = self.pile.pop(0)
        self.stack.append(card)
        print(f"{self.name} played: {card[0]} of {card[1]}")

    def snap_delay(self):
        """
        Return a random delay between 0.5 and 1.5 seconds.
        """
        return random.uniform(0.5, 1.5)

    def resolve_snap(self, players):
        """
        Resolve a snap by collecting all cards from the played stack and shuffling them.
        """
        snap_message = f"   {self.name} Snapped!   "
        border = "*" * (len(snap_message) + 2)
        print(border)
        print(f"*{snap_message}*")
        print(border)

        # Collect all cards from the played stacks
        for player in players:
            self.pile.extend(player.stack)
            player.stack = []
        random.shuffle(self.pile)
