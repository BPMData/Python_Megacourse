from num2words import num2words

while True:
    # Gets user input and formats it in an agnostic manner so it can be referred back to later despite how the user inputs it
    user_decision = input("Type either Add, Show, Edit, Complete, Reset or Exit:")
    user_decision = user_decision.strip().casefold()

    savefile = open("06_Save.txt", "r")
    todos = savefile.readlines()
    savefile.close()

    match user_decision:
        case "add":
            todo = input("Enter a To-Do Item:") + "\n"
            savefile = open("06_Save.txt", "r")
            todos = savefile.readlines()
            savefile.close()

            todos.append(todo)

            savefile = open("06_Save.txt", "w")
            savefile.writelines(todos)
            savefile.close()
        case "show" | "display":
            print()
            for index, item in enumerate(todos):
                item = item.rstrip()
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
            savefile = open("06_Save.txt", "w")
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
                with open("06_Save.txt", "w") as savefile:
                    savefile.write("")
                    savefile.close()
                    savefile = open("06_Save.txt", "r")
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

filenames = ["1.doc","1.report","1.presentation"]

filenames = [filename.replace(".","-") + ".txt" for filename in filenames]

print(filenames)