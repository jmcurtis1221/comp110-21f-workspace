"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730390523"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...

fortune: int = int(randint(1,4))

print("Your fortune cookie says...")

if fortune == 1:
    print("You are going to get an A in Comp110!")
else:
    if fortune == 2:
        print("Life is about to get good!")
    else:
        if fortune == 3:
            print("Today is going to be a great day!")
        else:
            print("Don't worry, be happy!")

print("Now, go spread positive vibes!")