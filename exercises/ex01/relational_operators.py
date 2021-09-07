"""Relational Operators Program to display the results of different relational operators."""

__author__ = "730390523"

left: str = input("Left-hand side:")
right: str = input("Right-hand side:")

answer1: bool = (int(left) < int(right))
answer2: bool = (int(left) >= int(right))
answer3: bool = (int(left) == int(right))
answer4: bool = (int(left) != int(right))

print((left) + " < " + (right) + " is " + str(answer1))
print((left) + " >= " + (right) + " is " + str(answer2))
print((left) + " == " + (right) + " is " + str(answer3))
print((left) + " != " + (right) + " is " + str(answer4))