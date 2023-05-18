todos = []

while True:
    user_decision = input("Type either Add, Show, Edit, Complete or Exit:")
    user_decision = user_decision.strip().casefold()

    match user_decision:
        case "add":
            todo = input("Enter a To-Do Item:")
            todos.append(todo)
        case "show" | "display":
            print()
            for index, item in enumerate(todos):
                item = item.title()
                row = f"{index+1}: {item}"
                print(row)
            print(f"\nYour To-Do List is {len(todos)} items long.")
            print()
        case "edit":
            number = int(input("Please enter the number of the To-Do Item you wish to edit."))
            number = number-1
            # Two ways of printing a variable in a line of code. Here's way #1, old schoolway.
            print("You selected {}.".format(todos[number]))
            new_todo = input("Please enter the To-Do Item you wish to replace this item.")
            todos[number] = new_todo
            # Here's the easier way to do it, as an "f-string literal" as autorecommended by PyCharm.
            print(f"Your new To-Do Item is {todos[number]}.")
        case "complete":
            # dir(list)
            # help(list.remove)
            # Go to the end of this line of code to see more messing around
            number = int(input("Please enter the number of the To-Do Item you wish to mark as completed."))
            todos.pop(number - 1)
        case "exit":
            break
        case _:
            print("You entered an unknown command.\n"
                  "Please type either Add, Show or Exit:")
print("Good bye!")

# Numbers to words

# In the terminal, I typed pip install num2words, then:
from num2words import num2words

todos = []

while True:
    user_decision = input("Type either Add, Show, Edit, Complete or Exit:")
    user_decision = user_decision.strip().casefold()

    match user_decision:
        case "add":
            todo = input("Enter a To-Do Item:")
            todos.append(todo)
        case "show" | "display":
            print()
            for index, item in enumerate(todos):
                item = item.title()
                row = f"{index+1}: {item}"
                print(row)
            print(f"\nYour To-Do List is {num2words(len(todos))} items long.")
            print()
        case "edit":
            number = int(input("Please enter the number of the To-Do Item you wish to edit."))
            number = number-1
            # Two ways of printing a variable in a line of code. Here's way #1, old schoolway.
            print("You selected {}.".format(todos[number]))
            new_todo = input("Please enter the To-Do Item you wish to replace this item.")
            todos[number] = new_todo
            # Here's the easier way to do it, as an "f-string literal" as autorecommended by PyCharm.
            print(f"Your new To-Do Item is {todos[number]}.")
        case "complete":
            # dir(list)
            # help(list.remove)
            # Go to the end of this line of code to see more messing around
            number = int(input("Please enter the number of the To-Do Item you wish to mark as completed."))
            todos.pop(number - 1)
        case "exit":
            break
        case _:
            print("You entered an unknown command.\n"
                  "Please type either Add, Show or Exit:")
print("Good bye!")

# Here's a weird trick:

for i, j in enumerate("Hello world."):
    print(i,j)

for i in enumerate("Hello world."):
    print(i)

# See day 5 in notes for an explanation of why these outputs look particularly different.

# New little program

waiting_list = ["Sean","Ben","CINDY!!!!!!"]

for index, item in enumerate(waiting_list):
    row = f"{index + 1}. {item.capitalize()}."
    print(row)

# Now lets sort

help(list.sort)

waiting_list = ["Sean","Ben","CINDY!!!!!!"]
waiting_list.sort()

for index, item in enumerate(waiting_list):
    row = f"{index + 1}. {item.capitalize()}."
    print(row)

waiting_list

# Note that waiting_list was permanently altered. Good or bad, that depends.
waiting_list = ["Sean","Ben","CINDY!!!!!!"]
waiting_list.sort(reverse=True)

for index, item in enumerate(waiting_list):
    row = f"{index + 1}. {item.capitalize()}."
    print(row)

waiting_list


# QUIZ

for i, j in enumerate("abcd"):
    print(i + 1)

for i, j in enumerate("abcd"):
    print(i.capitalize())

# Coding exercises here:  https://www.udemy.com/course/the-python-mega-course/learn/lecture/32165920#overview

# BUG SOLVING:https://www.udemy.com/course/the-python-mega-course/learn/lecture/32166178#overview

    menu = ["pasta", "pizza", "salad"]

    user_choice = int(input("Enter the index of the item: "))

    message = f"You chose {menu[user_choice]}."
    print(message)


# BUG #2

    menu = ["pasta", "pizza", "salad"]

    for i, j in enumerate(menu):
        print(F"{i}.{j}")