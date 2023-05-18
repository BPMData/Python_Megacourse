# code from yesterday

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

# code from now
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
        case _:
            print("You entered an unknown command.\n"
                  "Please type either Add, Show or Exit:")
print("Good bye!")

# OR, using IF and ELSE:
todos = []

while True:
    user_decision = input("Type either Add, Show or Exit:")
    user_decision = user_decision.strip().casefold()


    if user_decision == "add":
        todo = input("Enter a To-Do Item:")
        todos.append(todo)
    elif user_decision == "show":
        for item in todos:
            print(item)
    elif user_decision == "exit":
        break
    else:
        print("You entered an unknown command.\n"
              "Please type either Add, Show or Exit:")

print("Good bye!")

# This method above is way more annoying to type though, so no thanks.

# Back to the video

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