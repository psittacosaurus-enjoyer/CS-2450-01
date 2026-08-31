import random
def age_guesser():
    #initializies a random number, best_guess between 1 and 110
    best_guess = random.randint(1,111)
    #intiializes guest_count as 0
    guess_count = 0
    #prints best_guess, asks user if they older or younger than the random age, they respond with an input: 0 if its incorrrect and 1 if its correct
    print 
    #if user answers 0, guess_count +=1 and best_guess is updated as a random variable, then an input to ask if the best_guess is older or younger than their age (o or y)
    #
    #repeats
    