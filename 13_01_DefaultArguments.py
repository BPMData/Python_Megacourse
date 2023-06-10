# https://www.udemy.com/course/the-python-mega-course/learn/lecture/34598152#overview

from num2words import num2words

# Best practice is to define custom functions outside a loop.

# New code - adding arguments to our custom functions

# with open("12_Save.txt","w"):
#     pass
# ^^^ Include this code to create a new savefile

def get_save(filepath="12_Save.txt"): # everything after the = sign is the default argument/parameter.
    """Loads your To-Do Items from the specified Save.txt file.
    Reads the text file and returns the list of to-do items."""
    with open(filepath, "r") as savefile_local:
        todos_local = savefile_local.readlines()
    return todos_local

print(help(get_save))
def write_save(todos_arg, filepath="12_Save.txt"): # Non-default parameters must always precede default parameters. IDK why.
    """Writes the current list saved in the variable todos to your specified Save.txt file.
    Thereby, when you run the program again, your To-Do Items will be saved."""
    with open(filepath,"w") as savefile_local:
        savefile_local.writelines(todos_arg)

print(help(write_save))

# You can also use triple quotes to create multi-line strings.

multiline_string = """
Shall I compare thee to a summer's day?
No, I think not.

Bye!
"""


print(multiline_string)
# These two above are LOCAL variables because they're defined _within_ a function.

while True:
    user_decision_base = input("Type either Add, Show, Edit, Complete, Reset or Exit:")
    user_decision = user_decision_base.strip().casefold()
    list_decision = user_decision.split()

    todos = get_save(filepath="12_Save.txt") # Including the parameter is optional. It'll assign arguments to parameters by sequential order, like R does.
    todo = ()

    # if "add" in user_decision or "new" in user_decision: old method
    # if user_decision.startswith("add"): # technique suggested in the video
    if list_decision[0] == "add": # my technique, it also works.
        if len(list_decision) > 1:
            todo = user_decision_base[4:] +"\n" # This is the first bug we were "supposed" to fix.
        else:
            todo = input("Enter a To-Do Item:") + "\n"

        todos = get_save() # No need to include an argument as we specified the default parameter.

        todos.append(todo)

        write_save(todos)
        # with open("12_Save.txt", "w") as savefile:
        #     savefile.writelines(todos)
        #     todo = todo.rstrip()

        print(f"Item {todo.rstrip()} added to your To-Do List.")

    elif user_decision.startswith("show"):

        print()
        for index, item in enumerate(todos):
            item = item.rstrip()
            row = f"{index + 1}: {item}"
            print(row)
        print(f"\nYour To-Do List is {num2words(len(todos))} items long.")
        print()

    elif user_decision.startswith("edit"): # I guess I might have to add the if loop to let the user type edit 5 directly...
        if len(list_decision) > 1:
            try:
                number = int(user_decision[5:])
                number = number-1

                if number < 0 or user_decision[5:] == 0:
                    raise IndexError

                todos = get_save()

                new_todo = input(f"Please enter the To-Do Item you wish to replace the current item:\n {todos[number].rstrip()}.")
                todos[number] = new_todo + "\n"
                print(f"Your new To-Do Item is {todos[number].rstrip()}.")

                write_save(todos)

            except ValueError:
                print(
                    "A non-integer response was provided. Please type Edit again, then enter the number of the To-Do Item you wish to edit.")
            except IndexError:
                print(
                    "You have entered a number outside the range of To-Do Items in your To-Do List. "
                    "Please type Edit again, then enter the number of the To-Do Item you wish to edit."
                )
        else:
            while True:

                for index, item in enumerate(todos):
                    item = item.rstrip()
                    row = f"{index + 1}: {item}"
                    print(row)

                try:
                    number = int(input("Please enter the number of the To-Do Item you wish to edit:"))
                    number = number - 1

                    if number < 0 or user_decision[5:] == 0:
                        raise IndexError

                    todos = get_save()

                    # Two ways of printing a variable in a line of code. Here's way #1, old school way.
                    print("You selected {}.".format(todos[number].rstrip()))

                    new_todo = input("Please enter the To-Do Item you wish to replace this item:")
                    todos[number] = new_todo + "\n"

                    # Here's the easier way to do it, as an "f-string literal" as auto-recommended by PyCharm.
                    print(f"Your new To-Do Item is {todos[number].rstrip()}.")

                    write_save(todos)
                    break

                except ValueError:
                    print("A non-integer response was provided. Please provide an integer response.")
                except IndexError:
                    print(
                        "You have entered a number outside the range of To-Do Items in your To-Do List. "
                    )

    elif user_decision.startswith("complete"):
        if len(list_decision) > 1:
            try:
                number = int(user_decision[8:])
                number = number-1

                if number < 0 or user_decision[8:] == 0:
                    raise IndexError
                else:
                    removed = todos[number].rstrip()
                    todos.pop(number)

                write_save(todos)

                message = f'To-Do Item "{removed}" was marked as complete, and thus removed from the list.'
                print(message)

            except ValueError:
                print(
                    "A non-integer response was provided. Please type Complete again, then enter the number of the To-Do Item you wish to mark as Complete.")
            except IndexError:
                print(
                    "You have entered a number outside the range of To-Do Items in your To-Do List. "
                    "Please type Complete again, then enter the number of the To-Do Item you wish to mark as completed."
                )
        else:
            while True:

                for index, item in enumerate(todos):
                    item = item.rstrip()
                    row = f"{index + 1}: {item}"
                    print(row)
                try:
                    number = int(input("See your current To-Do Items Above.\nPlease enter the number of the To-Do Item you wish to mark as completed."))
                    number = number-1

                    if number < 0 or user_decision[8:] == 0:
                        raise IndexError

                    else:
                        removed = todos[number].rstrip()
                        todos.pop(number)

                    write_save(todos_arg=todos, filepath = "12_Save.txt") # You can put the arguments in the 'wrong' order if you specify them precisely.

                    message = f'To-Do Item "{removed}" was marked as complete, and thus removed from the list.'
                    print(message)
                    break

                except ValueError:
                    print("A non-integer response was provided.")
                    continue
                except IndexError:
                    print(
                        "You have entered a number outside the range of To-Do Items in your To-Do List. "
                    )

    elif user_decision.startswith("reset"):
        reset_choice = input("Continuing with Reset will erase all items from your To-Do List,\nleaving it totally blank. Continue?\nType YES if certain.")
        reset_choice = reset_choice.strip().casefold()

        if reset_choice == "yes":
            with open("12_Save.txt", "w+") as savefile:  #wow, w+ is dope
                savefile.write("")
                todos = savefile.readlines()

            print("Your To-Do List has been reset.")
            print(f"Your To-Do List is {num2words(len(todos))} items long.")

        else:
            print("Reset aborted.")

    elif "exit" in list_decision[0]:
        break

    else:
        print("You entered an unknown command.\n"
        "Please type either Add, Show, Edit, Complete, Reset or Exit:")

print("Good bye!")