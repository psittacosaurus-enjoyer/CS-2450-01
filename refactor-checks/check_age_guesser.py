"""Runs age_guesser.py with a fixed random seed and scripted answers.
Usage: python check_age_guesser.py path/to/age_guesser.py
Same seed + same answers should give the exact same output before and after refactoring.
"""
import io
import random
import runpy
import sys
from contextlib import redirect_stdout

SCENARIOS = {
    "Older/younger narrowing then correct": ["older", "younger", "older", "correct"],
    "Mixed capitalization": ["OLDER", "Younger", "Correct"],
    "Invalid answer then correct": ["maybe", "correct"],
    "Contradicting answers (keeps saying younger)": ["younger"] * 200,
}

script = sys.argv[1]
for name, answers in SCENARIOS.items():
    random.seed(2450)
    sys.stdin = io.StringIO("\n".join(answers) + "\n")
    output = io.StringIO()
    with redirect_stdout(output):
        runpy.run_path(script, run_name="__main__")
    print(f"=== {name}")
    print(output.getvalue().replace("correct age?", "correct age?\n").rstrip())
    print()
