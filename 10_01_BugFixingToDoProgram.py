# Gonna be bugfixing this code, except I think I already fixed some of the major bugs.
# It did occur to me, however, that trying to edit or complete an item number that didn't exist would cause a crash error.
# First bug - need a newline when using the shortcut add [text] method of add.
# Second bug - if you type edit add a new user, etc., it doesn't edit add a new user, it sees add and goes to add.
# Solution for this imo is to replace check for in user_decision to check for in list_decision[0]

from num2words import num2words

while True:
    user_decision_base = input("Type either Add, Show, Edit, Complete, Reset or Exit:")
    user_decision = user_decision_base.strip().casefold()
    list_decision = user_decision.split()

    with open("09_Save.txt", "r") as savefile:
        todos = savefile.readlines()
        todo = ()

### NEW CODE STARTS HERE ###
        # if "add" in user_decision or "new" in user_decision: old method
        # if user_decision.startswith("add"): # technique suggested in the video
        if list_decision[0] == "add": # my technique, it also works.
            if len(list_decision) > 1:
                todo = user_decision_base[4:] +"\n" # This is the first bug we were "supposed" to fix.
            else:
                todo = input("Enter a To-Do Item:") + "\n"

            with open("09_Save.txt", "r") as savefile:
                todos = savefile.readlines()

            todos.append(todo)

            with open("09_Save.txt", "w") as savefile:
                savefile.writelines(todos)
                todo = todo.rstrip()

            print(f"Item {todo} added to your To-Do List.")

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

                    with open("09_Save.txt", "r") as savefile:
                        todos = savefile.readlines()

                    new_todo = input(f"Please enter the To-Do Item you wish to replace the current item:\n {todos[number].rstrip()}.")
                    todos[number] = new_todo + "\n"
                    print(f"Your new To-Do Item is {todos[number].rstrip()}.")

                    with open("09_Save.txt", "w") as savefile:
                        savefile.writelines(todos)

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

                        with open("09_Save.txt", "r") as savefile:
                            todos = savefile.readlines()

                        # Two ways of printing a variable in a line of code. Here's way #1, old school way.
                        print("You selected {}.".format(todos[number].rstrip()))

                        new_todo = input("Please enter the To-Do Item you wish to replace this item:")
                        todos[number] = new_todo + "\n"

                        # Here's the easier way to do it, as an "f-string literal" as auto-recommended by PyCharm.
                        print(f"Your new To-Do Item is {todos[number].rstrip()}.")

                        with open("09_Save.txt", "w") as savefile:
                            savefile.writelines(todos)
                            break

                    except ValueError:
                        print("A non-integer response was provided. Please provide an integer responsSe.")
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

                    with open("09_Save.txt", "w") as savefile:
                        savefile.writelines(todos)

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

                    try:
                        number = int(input("Please enter the number of the To-Do Item you wish to mark as completed."))
                        number = number-1

                        if number < 0 or user_decision[8:] == 0:
                            raise IndexError

                        else:
                            removed = todos[number].rstrip()
                            todos.pop(number)

                        with open("09_Save.txt", "w") as savefile:
                            savefile.writelines(todos)

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
                with open("09_Save.txt", "w+") as savefile:  #wow, w+ is dope
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
