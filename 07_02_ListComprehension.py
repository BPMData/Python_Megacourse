# Today's code - we're going to learn a different way to remove the newlines in the output of SHOW.
from num2words import num2words

# with open("07_Save.txt", "w") as file:
# 	pass # doing this makes a new file, but run it in the CONSOLE because running it in the program itself every time will continually start with a blank savefile.


while True:
    user_decision = input("Type either Add, Show, Edit, Complete, Reset or Exit:")
    user_decision = user_decision.strip().casefold()

    savefile = open("07_Save.txt", "r")
    todos = savefile.readlines()
    savefile.close()

    match user_decision:
        case "add":
            todo = input("Enter a To-Do Item:") + "\n"
            savefile = open("07_Save.txt", "r")
            todos = savefile.readlines()
            savefile.close()

            todos.append(todo)

            savefile = open("07_Save.txt", "w")
            savefile.writelines(todos)
            savefile.close()
            # Old way of doing it
            #            for index, item in enumerate(todos):
            #                item = item.rstrip()
            #                row = f"{index + 1}: {item}"
            #                print(row)
            # New code starts here. Using a for-loop
        case "show" | "display":
            # new_todos = []
            # for item in todos:
            #    new_item = item.strip("\n")
            #    new_todos.append(new_item)

# Here's another way to do this - still worse than my method, but yolo
            new_todos = [item.strip("\n") for item in todos]

            for index, item in enumerate(new_todos):
                row = f"{index + 1}: {item}"
                print(row)

            print(f"\nYour To-Do List is {num2words(len(todos))} items long.")
            print()
        case "edit":
            number = int(input("Please enter the number of the To-Do Item you wish to edit."))
            number = number - 1
            # Two ways of printing a variable in a line of code. Here's way #1, old schoolway.
            print("You selected {}.".format(todos[number]))
            new_todo = input("Please enter the To-Do Item you wish to replace this item.")
            todos[number] = new_todo
            # Here's the easier way to do it, as an "f-string literal" as autorecommended by PyCharm.
            print(f"Your new To-Do Item is {todos[number]}.")
            savefile = open("07_Save.txt", "w")
            savefile.writelines(todos)
            savefile.close()
        case "complete":
            # dir(list)
            # help(list.remove)
            # Go to the end of this line of code to see more messing around
            number = int(input("Please enter the number of the To-Do Item you wish to mark as completed."))
            todos.pop(number - 1)
        case "reset":
            choice = input("Continuing with Reset will erase all items from your To-Do List,\nleaving it totally blank. Continue?\nType YES if certain.")
            choice = choice.strip().casefold()

            if choice == "yes":
                with open("07_Save.txt", "w") as savefile:
                    savefile.write("")
                    savefile.close()
                    savefile = open("07_Save.txt", "r")
                    todos = savefile.readlines()
                    savefile.close()
            else:
                print("Reset aborted.")
        case "exit":
            break
        case _:
            print("You entered an unknown command.\n"
                  "Please type either Add, Show, Edit, Complete, Reset or Exit:")
print("Good bye!")

