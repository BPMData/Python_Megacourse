# lower = int(input("Enter the lower bound:"))
# upper = int(input("Enter the upper bound:"))
#
# from random import randint
#
# output = randint(lower,upper)
#
# print(f"Your random number is {output}.")

#Bug fixing exercise

import random

from Modules.Day15_BugParser import parse

# Ask the user to enter a lower and an upper bound divided by a comma
user_input = input("Enter a lower bound and an upper bound divided a comma (e.g., 2,10)")

# Parse the user string by calling the parse function
parsed = parse(user_input)

# Pick a random int between the two numbers
rand = random.randint(parsed['lower_bound'], parsed['upper_bound'])

print(rand)