"""Counting letters in a string."""

__author__ = "730390523"


# Begin your solution here...

letter: str = input("What letter do you want to search for?: ")
word: str = input("Enter a word: ")
counter: int = 0
totalletters: int = 0

while len(word) > counter:
    if word[counter] == letter:
        totalletters = totalletters + 1
    counter = counter + 1
    
print("Count: " + str(totalletters))