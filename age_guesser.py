import random

YOUNGEST_POSSIBLE_AGE = 1
OLDEST_POSSIBLE_AGE = 110


def ask_about_guess(guess):
    """Shows the guess to the user and returns their answer in lowercase."""
    print("Are you:", guess, "?")
    answer = input('Are you Older, Younger, or is this the correct age?')
    return answer.lower()


def age_guesser():
    lowest_age = YOUNGEST_POSSIBLE_AGE
    highest_age = OLDEST_POSSIBLE_AGE
    guess_count = 0

    while True:
        # If the answers contradict each other there are no ages left to guess
        if lowest_age > highest_age:
            print("Invalid response, you cannot be younger than", highest_age, "and older than", lowest_age)
            return

        guess = random.randint(lowest_age, highest_age)
        guess_count += 1
        answer = ask_about_guess(guess)

        if answer == 'older':
            lowest_age = guess + 1
        elif answer == 'younger':
            highest_age = guess - 1
        elif answer == 'correct':
            print("It took", guess_count, "guesses!")
            return
        else:
            print("Invalid reponse, please enter 'younger', 'older', or 'correct'")


if __name__ == "__main__":
    age_guesser()
