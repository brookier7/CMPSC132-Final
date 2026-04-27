"""
Andrew Brook
CMPSC 132
April 28, 2026
Final Project
"""

import random

def validate_guess():
    """
    Asks user for a guess and ensures it is valid
    Returns the guess after making sure it is valid
    """
    guess = None
    while guess is None:
        try:
            guess = int(input("Guess a number: "))
        except ValueError:
            print("Please enter a valid number.")
    return guess

def make_guess(guess, correct):
    """
    Inputs a numerical guess
    Returns a result based on if the number is too high/low/correct
    """
    if guess > correct:
        return "Too high"
    elif guess < correct:
        return "Too low"
    else:
        return "Correct!"

if __name__ == "__main__":
    correct = random.randint(1,100)
    num_guesses = 1

    guess = validate_guess()
    while make_guess(guess,correct)!="Correct!":
        print(make_guess(guess,correct))
        num_guesses+=1
        guess = validate_guess()
        
    print("Correct!\nCongratulations!\nIt took you "+str(num_guesses)+" guesses!")

