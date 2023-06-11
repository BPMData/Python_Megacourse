# Re-using the bonus example code from day 12 as a baseline - with a focus on decoupling functions.
feet_inches = input("Enter feet and inches:")

def parse(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    # return feet, inches # we can do better than this by creating a {dictionary}.
    return {"Feet": feet, "Inches": inches}

def convert(Feet, Inches):
    meters = Feet * 0.3048 + Inches * 0.0254
    return meters

parsed = parse(feet_inches)
# result = convert(feet_inches)
result = convert(parsed["Feet"], parsed["Inches"])

print(f"\n{parsed['Feet']} feet and {parse(feet_inches)['Inches']} inches is equal to {result} meters.\n") # Here we see 3 different ways to call the output of a function in an f-string.


if result < 1:
    print("Kid is too small to rise the slide. He will be eaten by a grue if he attempts it.")
else:
    print("Kid can use the slide.")


# Quiz:

year_of_birth = int(input("Please enter your year of birth as an integer, for example, 1983."))

def get_age(year_of_birth, current_year = 2023):
    age = current_year - year_of_birth
    return age

print(get_age(1983))

