"""Repeating a beat in a loop."""

__author__ = "730390523"


# Begin your solution here...

beat: str = input("What beat do you want to repeat?")
repeats: str = input("How many times do you want to repeat it?")
repeats = int(repeats)
count: int = 0
sound: str = ""

if repeats > 0:
    while count < repeats:
        sound = sound + beat
        count = count + 1
        if count < repeats:
            sound = sound + " "
else:
    sound = "No beat..."

print(sound)