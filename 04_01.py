# Yesterday's code:


todos = []

while True:
    user_decision = input("Type either Add, Show or Exit:")
    user_decision = user_decision.strip()

    match user_decision.casefold():
        case "add":
            todo = input("Enter a To-Do Item:")
            todos.append(todo)
        case "show" | "display":
            for item in todos:
                item = item.title()
                print(item)
        case "exit":
            break
        case _:
            print("You entered an unknown command.\n"
                  "Please type either Add, Show or Exit:")
print("Good bye!")

# Today's code - add an Edit function.

todos = []

while True:
    user_decision = input("Type either Add, Show, Edit or Exit:")
    user_decision = user_decision.strip().casefold()

    match user_decision:
        case "add":
            todo = input("Enter a To-Do Item:")
            todos.append(todo)
        case "show" | "display":
            for item in todos:
                item = item.title()
                print(item)
        case "edit":
            number = int(input("Please enter the number of the To-Do Item you wish to edit, with the number at the top of the list being 1."))
            number = number-1
            # Two ways of printing a variable in a line of code. Here's way #1, old schoolway.
            print("You selected {}.".format(todos[number]))
            new_todo = input("Please enter the To-Do Item you wish to replace this item.")
            todos[number] = new_todo
            # Here's the easier way to do it, as an "f-string literal" as autorecommended by PyCharm.
            print(f"Your new To-Do Item is {todos[number]}.")
        case "exit":
            break
        case _:
            print("You entered an unknown command.\n"
                  "Please type either Add, Show or Exit:")
print("Good bye!")