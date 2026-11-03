import os

# Every set of 3 spots that counts as a win (spots are numbered 0-8, left to right, top to bottom)
WINNING_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
    (0, 4, 8), (2, 4, 6),             # diagonals
]


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def show_board(board):
    for row in range(3):
        first_spot = row * 3
        print(f" {board[first_spot]} | {board[first_spot + 1]} | {board[first_spot + 2]} ")
        if row < 2:
            print("---+---+---")


def show_game_screen(board):
    """Clears the terminal and redraws the title and the board."""
    clear_screen()
    print("Tic-Tac-Toe\n")
    show_board(board)


def get_winner(board):
    """Returns 'X' or 'O' if that player has three in a row, otherwise None."""
    for player in ("X", "O"):
        for line in WINNING_LINES:
            if all(board[spot] == player for spot in line):
                return player
    return None


def play():
    # Empty spots hold their own number so the player can see which number to type
    board = [str(spot) for spot in range(9)]
    current_player = "X"

    # Keep going while there is at least one open (numbered) spot left
    while any(spot.isdigit() for spot in board):
        show_game_screen(board)
        print(f"\n{current_player}'s turn!")

        try:
            chosen_spot = int(input("Pick a spot (0-8): "))
        except ValueError:
            print("Invalid input. Try again.")
            continue

        spot_is_open = 0 <= chosen_spot < 9 and board[chosen_spot].isdigit()
        if not spot_is_open:
            print("Spot is taken or out of range. Try again.")
            continue

        board[chosen_spot] = current_player

        winning_player = get_winner(board)
        if winning_player:
            show_game_screen(board)
            print(f"\n{winning_player} wins!")
            return

        current_player = "O" if current_player == "X" else "X"

    # The loop only ends without a winner when the board is full
    show_game_screen(board)
    print("\nIt's a draw!")


if __name__ == "__main__":
    play()
