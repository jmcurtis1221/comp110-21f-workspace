"""Relational Operators Program to display the results of different relational operators"""

__author__ = "730390523"

left: int = input("Left-hand side:")
right: int = input("Right-hand side:")

answer1: str = (int(left) < int(right))
answer2: str = (int(left) >= int(right))
answer3: str = (int(left) == int(right))
answer4: str = (int(left) != int(right))

print((left) + " < " + (right) + " is " + str(answer1))
print((left) + " >= " + (right) + " is " + str(answer2))
print((left) + " == " + (right) + " is " + str(answer3))
print((left) + " != " + (right) + " is " + str(answer4))