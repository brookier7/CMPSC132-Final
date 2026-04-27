"""
Andrew Brook
CMPSC 132
April 28, 2026
Final Project
"""

import random


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
    guess = int(input("Guess a number: "))
    while make_guess(guess,correct)!="Correct!":
        print(make_guess(guess,correct))
        num_guesses+=1
        guess = int(input("Guess a number: "))
    print("Correct!\nCongratulations!\nIt took you "+str(num_guesses)+" guesses!")

