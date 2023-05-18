prompt = 'Enter to To-Do Item:'

# todo1 = input(prompt)
# todo2 = input(prompt)
# todo3 = input(prompt)
#
# todos = [todo1,todo2,todo3]
#
# print(todos)

# We don't want that stuff because it's slow and bad and doesn't scale.

while 2 > 1: # Picked because this is always true. Same principle as the "Until King Charles' last descendant dies..."
    todo = input(prompt) # The tab here is PART OF THE SYNTAX, AND IS NECESSARY. Used instead of {}
    print("Next Item...")

# tHIS ALSO WORKS:

while True: # True MUST be in title case
    todo = input(prompt) # The tab here is PART OF THE SYNTAX, AND IS NECESSARY. Used instead of {}
    print("Next Item...")

# Here's the code to store in a list - I'll have to copy/paste this to go above to run it, or comment out the code above

todos = []

while True:
    todo = input(prompt)
    todos.append(todo)