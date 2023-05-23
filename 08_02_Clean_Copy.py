from num2words import num2words

while True:
    user_decision = input("Type either Add, Show, Edit, Complete, Reset or Exit:")
    user_decision = user_decision.strip().casefold()

    with open("08_Save.txt", "r") as savefile:
        todos = savefile.readlines()
    match user_decision:

        case "add":
            todo = input("Enter a To-Do Item:") + "\n"

            with open("08_Save.txt", "r") as savefile:
                todos = savefile.readlines()

            todos.append(todo)

            with open("08_Save.txt", "w") as savefile:
                savefile.writelines(todos)

        case "show" | "display":

            # with open("08_Save.txt","r") as savefile:
            # todos = savefile.readlines()  - this is definitely not needed, remember todos is actually defined outside of the match code

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

            with open("08_Save.txt", "r") as savefile:
                todos = savefile.readlines()

            # Two ways of printing a variable in a line of code. Here's way #1, old school way.
            print("You selected {}.".format(todos[number].rstrip()))

            new_todo = input("Please enter the To-Do Item you wish to replace this item.")
            todos[number] = new_todo + "\n"

            # Here's the easier way to do it, as an "f-string literal" as auto-recommended by PyCharm.
            print(f"Your new To-Do Item is {todos[number].rstrip()}.")

            with open("08_Save.txt", "w") as savefile:
                savefile.writelines(todos)

        case "complete":
            number = int(input("Please enter the number of the To-Do Item you wish to mark as completed."))
            removed = todos[number-1].rstrip()
            todos.pop(number - 1)

            with open("08_Save.txt", "w") as savefile:
                savefile.writelines(todos)

            message = f'To-Do Item "{removed}" was marked as complete, and thus removed from the list.'
            print(message)

        case "reset":
            reset_choice = input("Continuing with Reset will erase all items from your To-Do List,\nleaving it totally blank. Continue?\nType YES if certain.")
            reset_choice = reset_choice.strip().casefold()

            if reset_choice == "yes":
                with open("08_Save.txt", "w+") as savefile:  #wow, w+ is dope
                    savefile.write("")
                    todos = savefile.readlines()

                print("Your To-Do List has been reset.")
                print(f"Your To-Do List is {num2words(len(todos))} items long.")

            else:
                print("Reset aborted.")

        case "exit":
            break

        case _:
            print("You entered an unknown command.\n"
                  "Please type either Add, Show, Edit, Complete, Reset or Exit:")

print("Good bye!")
