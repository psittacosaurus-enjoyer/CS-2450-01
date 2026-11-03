"""Plays scripted games of tic-tac-toe by feeding moves to stdin.
Usage: python check_tictactoe.py path/to/tic-tac-toe.py
Prints the last board + result line for each scenario so before/after can be compared.
"""
import subprocess
import sys

SCENARIOS = {
    "Row win (X: 0,1,2)": [0, 3, 1, 4, 2],
    "Column win (X: 0,3,6)": [0, 1, 3, 2, 6],
    "Diagonal win (O: 0,4,8)": [1, 0, 2, 4, 3, 8],
    "Anti-diagonal win (X: 2,4,6)": [2, 0, 4, 1, 6],
    "Draw (board fills up)": [0, 1, 2, 4, 3, 5, 7, 6, 8],
    # X takes 4, O tries occupied 4, then 9 (out of range), then 'abc', then plays on
    "Invalid moves (occupied, out of range, not a number)": [4, 4, 9, "abc", 0, 1, 3, 7],
}

script = sys.argv[1]
for name, moves in SCENARIOS.items():
    stdin = "\n".join(str(m) for m in moves) + "\n"
    result = subprocess.run([sys.executable, script], input=stdin, text=True,
                            capture_output=True, env={"TERM": "dumb"})
    out = result.stdout
    # keep only the last screen (after the last title) plus any error messages
    last_screen = out[out.rfind("Tic-Tac-Toe"):].strip()
    errors = [line.split("Pick a spot (0-8): ")[-1] for line in out.splitlines()
              if "Try again" in line]
    print(f"=== {name}")
    print(last_screen)
    if errors:
        print("Error messages shown:", errors)
    if result.returncode != 0:
        print("CRASHED:", result.stderr.strip().splitlines()[-1])
    print()
