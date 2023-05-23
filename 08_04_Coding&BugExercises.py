# Bug Fixing

# Bug-Fixing Exercise 1

# with open("file.txt", 'r') as file:
#     print(file.read())
#     print(len(file.read()))

# The Python script above is in the same directory with a file named file.txt whose content is:
#
# Hello You
#
# The Python script should print out the content of the file and the number of characters of the text inside file.txt. So, the expected output would be:
#
#     Hello You
#     9
#
# However, the script prints out this:
#
#     Hello You
#     0
#
# Can you fix the program so it prints out the expected output?

# SOLUTION!!!!

file_name = "bugfile.txt"

open(file_name, 'w')

with open(file_name, "w") as bugtestfile:
    bugtestfile.writelines("Hello You")
    bugtestfile.close()

with open(file_name, 'r') as file:
    content = file.read()
    print(content)
    print(len(content))


# Coding Exercise 1
# https://www.udemy.com/course/the-python-mega-course/learn/lecture/32276314#overview

 # Actually pretty easy, here's the solution:

while True:
    with open("sides.txt", 'r') as file:
        sides = file.readlines()

    side = input("Throw the coin and enter head or tail here: ?") + "\n"

    sides.append(side)

    with open("sides.txt", 'w') as file:
        file.writelines(sides)

    nr_heads = sides.count("head\n")
    percentage = nr_heads / len(sides) * 100

    print(f"Heads: {percentage}%")