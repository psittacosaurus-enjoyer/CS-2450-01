import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show(b):
    for r in range(3):
        print(f" {b[r * 3]} | {b[r * 3 + 1]} | {b[r * 3 + 2]} ")
        if r < 2:
            print("---+---+---")

def winner(b):

    if b[0] == 'X' and b[1] == 'X' and b[2] == 'X':
        return 'X'
    if b[3] == 'X' and b[4] == 'X' and b[5] == 'X':
        return 'X'
    if b[6] == 'X' and b[7] == 'X' and b[8] == 'X':
        return 'X'
    if b[0] == 'X' and b[3] == 'X' and b[6] == 'X':
        return 'X'
    if b[1] == 'X' and b[4] == 'X' and b[7] == 'X':
        return 'X'
    if b[2] == 'X' and b[5] == 'X' and b[8] == 'X':
        return 'X'
    if b[0] == 'X' and b[4] == 'X' and b[8] == 'X':
        return 'X'
    if b[2] == 'X' and b[4] == 'X' and b[6] == 'X':
        return 'X'

    if b[0] == 'O' and b[1] == 'O' and b[2] == 'O':
        return 'O'
    if b[3] == 'O' and b[4] == 'O' and b[5] == 'O':
        return 'O'
    if b[6] == 'O' and b[7] == 'O' and b[8] == 'O':
        return 'O'
    if b[0] == 'O' and b[3] == 'O' and b[6] == 'O':
        return 'O'
    if b[1] == 'O' and b[4] == 'O' and b[7] == 'O':
        return 'O'
    if b[2] == 'O' and b[5] == 'O' and b[8] == 'O':
        return 'O'
    if b[0] == 'O' and b[4] == 'O' and b[8] == 'O':
        return 'O'
    if b[2] == 'O' and b[4] == 'O' and b[6] == 'O':
        return 'O'
    return None

def play():
    b = [str(i) for i in range(9)]
    turn = "X"
    while any(cell.isdigit() for cell in b):
        clear_screen()
        print("Tic-Tac-Toe\n")
        show(b)
        print(f"\n{turn}'s turn!")
        try:
            move = int(input("Pick a spot (0-8): "))
        except ValueError:
            print("Invalid input. Try again.")
            continue

        if 0 <= move < 9 and b[move].isdigit():
            b[move] = turn
            winner_result = winner(b)
            if winner_result:
                clear_screen()
                print("Tic-Tac-Toe\n")
                show(b)
                print(f"\n{winner_result} wins!")
                return
            turn = "O" if turn == "X" else "X"
        else:
            print("Spot is taken or out of range. Try again.")
    clear_screen()
    print("Tic-Tac-Toe\n")
    show(b)
    print("\nIt's a draw!")

play()
