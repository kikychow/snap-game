import random
import time
from player import Player


class SnapGame:
    """
    Represents a game of Snap.

    Attributes:
        num_decks (int): The number of decks used in the game.
        num_players (int): The number of players in the game.
        stop_rounds (int): The maximum number of rounds to play.
        round_count (int): The current round number.
        players (list): A list of Player objects representing the players in the game.
    """

    def __init__(self, num_decks=1, num_players=2, stop_rounds=1):
        self.num_decks = num_decks
        self.num_players = num_players
        self.stop_rounds = stop_rounds
        self.round_count = 0
        self.players = [Player(f"Player {i+1}") for i in range(num_players)]

    def create_deck(self):
        suits = ["diamonds", "clubs", "hearts", "spades"]
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        deck = [(rank, suit) for rank in ranks for suit in suits]
        return deck

    def shuffle_and_deal_cards(self):
        deck = self.create_deck()
        deck *= self.num_decks
        random.shuffle(deck)
        for i, card in enumerate(deck):
            self.players[i % len(self.players)].pile.append(card)

    def is_snap(self, player):
        """
        Check if the top card of the player's stack matches the top card of any other player's stack.
        """
        for stack in [other.stack for other in self.players if other != player]:
            if len(stack) > 0:
                player_card_rank = player.stack[-1][0]
                other_card_rank = stack[-1][0]
                if player_card_rank == other_card_rank:
                    return True
        return False

    def start_game(self):
        """
        Start the game and continue until a player runs out of cards or the maximum number of rounds is reached.
        """
        while all([player.pile for player in self.players]):  # Continue while all players have cards
            for player in self.players:
                time.sleep(0.5)  # Delay between each player's turn
                player.play_card()

                if self.is_snap(player):  # Check if a snap is possible
                    # Simulate snap delays for all players and find the quickest player
                    delays = [(player, player.snap_delay()) for player in self.players]
                    quickest_player, min_delay = min(delays, key=lambda x: x[1])
                    time.sleep(min_delay)
                    quickest_player.resolve_snap(self.players)

                    self.round_count += 1
                    print(f"Round {self.round_count}:")

                    # Print the number of cards remaining for each player
                    for player in self.players:
                        print(f"{player.name} now has {len(player.pile)} cards.")
                    print("\n")

                    # Check if the maximum number of rounds has been reached
                    if self.stop_rounds >= 0:
                        if self.round_count >= self.stop_rounds:
                            return

    def end_game_and_print_winner(self):
        """
        Print the number of cards remaining for each player and the winner(s) of the game.
        """
        # Print the number of cards remaining for each player
        for player in self.players:
            print(f"{player.name} has {len(player.pile)} cards remaining.")

        # Find the player(s) with the most cards
        max_cards = max(len(player.pile) for player in self.players)
        winners = [player for player in self.players if len(player.pile) == max_cards]

        # Print the winner(s)
        winner_names = ", ".join(winner.name for winner in winners)
        winning_message = f"   {winner_names} Wins!   "
        border = "*" * (len(winning_message) + 2)
        print(border)
        print(f"*{winning_message}*")
        print(border)

    def play_game(self):
        self.shuffle_and_deal_cards()

        print("\nStarting the Snap Game!\n")
        print("=" * 20)

        self.start_game()

        print("=" * 20)
        print("\nGame Over!\n")

        self.end_game_and_print_winner()
