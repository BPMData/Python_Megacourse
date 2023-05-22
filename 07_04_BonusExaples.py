filenames = ["1.doc","1.report","1.presentation"]

filenames = [filename.replace(".","-") + ".txt" for filename in filenames]

print(filenames)

Quiz:

new = []

for i in [1, 2, 3]:
    new.append(i + 10)

print(new)

new = [i for i in ['a', 'b', 'c']]
print(new)

# Coding Exercises:

# #1, two solutions

# Harder
names = ["john smith", "jay santi", "eva kuki"]

for index, name in enumerate(names):
    names[index] = name.title()

print(names)

# Easier
names = ["john smith", "jay santi", "eva kuki"]
names = [name.title() for name in names]
print(names)

# Coding Exercise 2
#
# usernames = ["john 1990", "alberta1970", "magnola2000"]
#
# Extend the code above so the code prints out a list containing the number of characters for each username.
#
# The output of your code should be as below:

# 9, 11, 11

usernames = ["john 1990", "alberta1970", "magnola2000"]

lengths = [name.__len__() for name in usernames]

print(lengths)


# Coding Exercise 3
#
#     user_entries = ['10', '19.1', '20']
#
# Extend the code above so the code prints out a list containing the same items as floats.
#
# The output of your code should be as below:
#
#     [10.0, 19.1, 20.0]

user_entries = ['10', '19.1', '20']

floats = [float(entry) for entry in user_entries]
print(floats)

# Coding Exercise 4
#
#     user_entries = ['10', '19.1', '20']
#
# Extend the code above so the code prints out the sum of the numbers.
#
# The output of your code should be as below:
#
#     49.1
#
# Hint: Use the sum() function.
# The function gets a list of numbers as input and produces the sum of all numbers. For more info, try help(sum).

sum(floats)
# Lol, that was 2 e-z
#
# Bug-Fixing Exercise 1
#
# The code below tries to write the items of temperatures each in one line in the file.txt list.
# However, the code has an error. Try to fix the error.

temperatures = [10, 12, 14]

file = open("file.txt", 'w')

file.writelines(temperatures)

# Solution:
temperatures = [10, 12, 14]

temperatures = [str(i) + '\n' for i in temperatures]

file = open("file.txt", 'w')
file.writelines(temperatures)

# Bug-Fixing Exercise 2
#
# The code below tries to convert all the numbers to integers. However, the code has an error. Try to fix the error.
#
#     numbers = [10.1, 12.3, 14.7]
#     numbers = [int(number) for item in numbers]
#     print(numbers)

# Solution:

numbers = [10.1, 12.3, 14.7]
numbers = [int(number) for number in numbers] # can't define it as both number and item
print(numbers)

