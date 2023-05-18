# Code from last video

todos = []

while True:
    user_decision = input("Type either Add, Show or Exit:")

    match user_decision.casefold():
        case "add":
            todo = input("Enter a To-Do Item:")
            todos.append(todo)
        case "show":
            print(todos)
        case "exit":
            break
print("Good bye!")


# Code from today - for loop

todos = []

while True:
    user_decision = input("Type either Add, Show or Exit:")

    match user_decision.casefold():
        case "add":
            todo = input("Enter a To-Do Item:")
            todos.append(todo)
        case "show":
            for item in todos:
                print(item)
        case "exit":
            break
print("Good bye!")


# How to also trim whitespace:

todos = []

while True:
    user_decision = input("Type either Add, Show or Exit:")
    user_decision = user_decision.strip()

    match user_decision.casefold():
        case "add":
            todo = input("Enter a To-Do Item:")
            todos.append(todo)
        case "show":
            for item in todos:
                print(item)
        case "exit":
            break
print("Good bye!")