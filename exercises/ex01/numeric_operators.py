"""Numerical Operators Program to display results of different numerical operators."""

__author__ = "730390523"

left: str = input("Left-hand side:")
right: str = input("Right-hand side:")

answer1: int = (int(left) ** int(right))
answer2: float = (int(left) / int(right))
answer3: int = (int(left) // int(right))
answer4: int = (int(left) % int(right))

print((left) + " ** " + (right) + " is " + str(answer1))
print((left) + " / " + (right) + " is " + str(answer2))
print((left) + " // " + (right) + " is " + str(answer3))
print((left) + " % " + (right) + " is " + str(answer4))