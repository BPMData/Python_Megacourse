# Bonus Examples: https://www.udemy.com/course/the-python-mega-course/learn/lecture/34597844#overview

try:
    width = float(input("Enter rectangle width:"))
    length = float(input("Enter rectangle length:"))

    if width == length:
        exit("Bad move, hombre. We don't like squares in these parts.")

# Note, if can be used without elif or else statements following it.

    area = width * length
    print(area)

except ValueError:
    print("Please enter a number; do not spell the word out.")

try:
    total_value = float(input("Enter the total value as a number."))
    value = float(input("Enter the value of the subtotal under consideration."))

    percentage = value / total_value * 100

    print(f"That is {percentage}%.")

except ValueError:
    print("You need to enter a number. Run the program again.")

colors = [11, 34, 98, 43, 45, 54, 54]

for i in colors:
    if i > 50:
        print(i)
    else:
        continue