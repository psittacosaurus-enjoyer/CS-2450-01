import random
def age_guesser():
    lowest_age = 1
    highest_age = 110
    guess_count = 0
    
    correct = False
    
    while correct != True:
        if lowest_age > highest_age:
            print("Invalid response, you cannot be younger than", highest_age, "and older than", lowest_age)
            break
        guess = random.randint(lowest_age, highest_age)
        print("Are you:", guess, "?")
        guess_count += 1
        answer = input('Are you Older, Younger, or is this the correct age?')
        
        
        if answer.lower() == 'older':
            lowest_age = guess + 1
            
        elif answer.lower() == 'younger':
            highest_age = guess -1
            
        elif answer.lower() == "correct":
            correct = True
            print ("It took", guess_count, "guesses!")
            
        else:
            print("Invalid reponse, please enter 'younger', 'older', or 'correct'")
age_guesser()
        
        