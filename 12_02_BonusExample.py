feet_inches = input("Enter feet and inches:")

def convert(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])

    meters = feet * 0.3048 + inches * 0.0254

    print(f"\n{feet} feet and {inches} inches is equal to {meters} meters.\n")

    return meters

result = convert(feet_inches)

if result < 1:
    print("Kid is too small.")
else:
    print("Kid can use the slide.")


# Code Experiments
https://www.udemy.com/course/the-python-mega-course/learn/quiz/5902628#overview
def liters_to_m3():
    liters = float(input("Enter the number of liters."))
    m3 = liters / 1000

    print(m3)
    return m3


liters_to_m3()


def foo(*list):
    length = len(list)
    total = sum(list)

    avg = total / length

    return avg


print(foo(10, 20, 30, 40))


def foo(*args):
    length = len(args)
    total = sum(args)
    avg = total / length
    return avg

print(foo(10, 20, 30, 40))

# This answer is BS, lol:

def foo(mylist):
    return sum(mylist) / len(mylist)


def foo(name):
    output = print(f"Hi {name}")
    return output


foo("Marry")

foo("Bobaldo")


def masher(one, two):
    mashup = f"{one}{two}"

    return mashup


masher("long", "johnson")


Code Exp 6


def greeter(name):
    name = name.title()
    output = f"Hi {name}"
    return output


greeter("john")