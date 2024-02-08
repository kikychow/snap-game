from snap_game import SnapGame


def get_valid_integer(message, greater_than):
    while True:
        user_input = input(message)
        try:
            integer_value = int(user_input)
            if integer_value > greater_than:
                return integer_value
            else:
                print(f"Error: Please enter an integer greater than {greater_than}.")
        except ValueError:
            print("Error: Please enter a valid integer.")


if __name__ == "__main__":
    print("Welcome to Snap!")
    num_decks = get_valid_integer(">>> How many decks would you like to play with? ", 0)
    num_players = get_valid_integer(">>> How many players are there? ", 0)
    stop_rounds = get_valid_integer(
        ">>> How many rounds would you like to play? (Enter 0 to play until a player run out of cards) ",
        -1,
    )
    game = SnapGame(num_decks=num_decks, num_players=num_players, stop_rounds=stop_rounds)
    print("=" * 20)
    game.play_game()
