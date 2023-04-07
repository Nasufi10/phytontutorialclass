#!/usr/bin/env python

import random

def main():
    """Start a guessing music game."""
    print("Guess the music genre!")

    Genre = [
        "pop",
        "rock",
        "kpop",
        "balled",
        "traditional",
        "R&B",
        "Hip-hop"
        ]

    x = random.choice(Genre)
    guess = None

    while x != guess:

        guess = str(input("What genre of music am I thinking of? "))
        
        if x == guess:
            print("You guessed {}. Congratulations you got it right!".format(guess))
            break
        else:
            print("You guessed {}. Unfortunately you got the wrong answer. Please try again!".format(guess))
            print("Hint:The correct answer consist of {} letter".format(len(x)))
main()
