# Original code

prompt = 'Enter to To-Do Item:'

todos = []

while True:
    todo = input(prompt)
    todos.append(todo)
    print(todos)

# New code for Day 3
todos = []

while True:
    user_decision = input("Type either Add, Show or Exit:")

    match user_decision:
        case "Add":
            todo = input("Enter a To-Do Item:")
            todos.append(todo)
        case "Show":
            print(todos)
        case "Exit":
            break
print("Good bye!")

# Make it case insensitive:


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

