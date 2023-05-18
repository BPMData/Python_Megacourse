# old code:

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

# New code:

meals = ["pasta","pizza","wrath"]

for meal in meals:
    print(meal.capitalize())

    meals = ["pasta", "pizza", "wrath"]

    for meal in "meals":
        print(meal.capitalize())


