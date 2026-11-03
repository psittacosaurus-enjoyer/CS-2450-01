# Refactoring Activity

## Part 1 – tic-tac-toe.py

The original file is in the first commit on this branch ("Add original refactoring activity files") so the before/after can be compared with `git diff`.

**What I changed**
- **Names:** `b` → `board`, `r` → `row`, `turn` → `current_player`, `move` → `chosen_spot`, `winner_result` → `winning_player`, `show` → `show_board`, `winner` → `get_winner`.
- **Simplified the winner function:** the old one had 16 almost identical `if` statements (8 lines × 2 players). I put the 8 winning lines in a `WINNING_LINES` list and loop over each player and each line with `all(...)`. It still checks X before O, same as before.
- **Removed duplicated code:** "clear the screen, print the title, show the board" was copied 3 times in `play()`, so I moved it into `show_game_screen(board)`.
- **Flatter if/else:** an invalid spot now does `continue` right away, so the normal path isn't nested inside the `if`.
- **Formatting/comments:** two blank lines between functions, short docstrings, and comments on the parts that weren't obvious (why empty spots hold numbers, why the loop ending means a draw).
- I added `if __name__ == "__main__":` around `play()`. Running the file works exactly the same, but now it can be imported without starting a game.

**Checks (before and after)**

`check_tictactoe.py` plays scripted games by piping moves into the program and prints the final board for each one. Results are in `before_checks.txt` and `after_checks.txt`, and the two files are **identical** (`diff` printed nothing).

| Check | Moves | Expected | Before | After |
|---|---|---|---|---|
| Row win | X:0,1,2 | X wins | X wins ✅ | X wins ✅ |
| Column win | X:0,3,6 | X wins | X wins ✅ | X wins ✅ |
| Diagonal win | O:0,4,8 | O wins | O wins ✅ | O wins ✅ |
| Other diagonal | X:2,4,6 | X wins | X wins ✅ | X wins ✅ |
| Draw | board fills up, no line | "It's a draw!" | draw ✅ | draw ✅ |
| Invalid move | O picks 4 (taken), 9, "abc" | error message, still O's turn | ✅ | ✅ |

**Bug I noticed (not fixed, since this is just a refactor):** after an invalid move the error message prints, but the loop clears the screen right away, so a real player never actually sees "Spot is taken…" or "Invalid input…".

## Part 2 – player.py

Copied `x`, `y`, `speed`, and `move()` from `CharacterBase` into `Player`, changed `class Player(CharacterBase)` to `class Player`, replaced `super().__init__(x, y, speed)` with setting the attributes directly, and deleted `CharacterBase`. `test_player.py` was not changed.

Test run before the change:
```
Test player:
  ✓ The player moves correctly
  ✓ The player jumps correctly
  ✓ The player takes damage correctly
  ✓ The score is added correctly

4 passed
```

Test run after the change (`python -m pytest --spec test_player.py`):
```
test_player.py:

Test player:
  ✓ The player moves correctly
  ✓ The player jumps correctly
  ✓ The player takes damage correctly
  ✓ The score is added correctly

============================== 4 passed in 0.05s ===============================
```

## Part 3 – age_guesser.py

Done on the `refactor-age-guesser` branch, with a pull request into `main`.
