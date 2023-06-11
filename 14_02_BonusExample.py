# Re-using the bonus example code from day 13 as a baseline - with a focus on decoupling functions.
from Modules.Bonus_14_Day import parse, convert

feet_inches = input("Enter feet and inches:")

parsed = parse(feet_inches)

result = convert(parsed["Feet"], parsed["Inches"])

print(f"\n{parsed['Feet']} feet and {parse(feet_inches)['Inches']} inches is equal to {result} meters.\n") # Here we see 3 different ways to call the output of a function in an f-string.


if result < 1:
    print("Kid is too small to rise the slide. He will be eaten by a grue if he attempts it.")
else:
    print("Kid can use the slide.")

# Day 14 Quiz:  https://www.udemy.com/course/the-python-mega-course/learn/quiz/5579090#overview

# Day 14 Coding Exercises

# Exercise 1
def water_state(temperature):
    if temperature <= 0:
        print("Solid")
    elif temperature > 0 and temperature < 100:
        print("Liquid")
    else:
        print("Gas")

water_state(100)

# Exercise 2

FREEZING_POINT = 0
BOILING_POINT = 100

def water_state(temperature):
    if temperature <= FREEZING_POINT:
        return "Solid"
    elif FREEZING_POINT < temperature < BOILING_POINT:
        return "Liquid"
    else:
        return "Gas"

# Exercise 3

def marcopolo(temp):
    if temp > 25:
        print("Hot")
    elif 15 <= temp <= 25:
        print("Warm")
    elif temp < 15:
        print("Cold")

marcopolo(10)
marcopolo(15)
marcopolo(25)
marcopolo(26)


def count(phrase):
    return phrase.count('.')

nr_of_periods = count("Trees are good. Grass is green.")
print(nr_of_periods)