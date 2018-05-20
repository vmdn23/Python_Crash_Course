#!/usr/bin/python3
"""Make a class Die with one attribute called sides,
which has a default value of 6. Write a method called roll_die()
that prints a random number between 1 and the number of sides
the die has. Make a 6-sided die and roll it 10 times.
Make a 10-sided die and a 20-sided die. Roll each die 10 times.
"""


from random import randint


class Die():
    """Represents a die that can be rolled"""

    def __init__(self, sides=6):
        """Initializes the die"""
        self.sides = sides

    def roll_die(self):
        """Returns a number from 1 and the number of sides"""
        return randint(1, self.sides)

# Make a 6-sided die and show the results from 10 rolls
d6 = Die()

results = []
for roll_num in range(10):
    result = d6.roll_die()
    results.append(result)
print("10 rolls from a 6-sided die:")
print(results)


# Make a 6-sided die and show the results from 10 rolls
d10 = Die(sides=10)

results = []
for roll_num in range(10):
    result = d10.roll_die()
    results.append(result)
print("\n10 rolls from a 10-sided die:")
print(results)



# Make a 6-sided die and show the results from 10 rolls
d20 = Die(sides=20)

results = []
for roll_num in range(10):
    result = d20.roll_die()
    results.append(result)
print("\n10 rolls from a 20-sided die:")
print(results)
