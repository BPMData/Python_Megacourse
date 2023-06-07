def greet():
    message = "hello"
    new_message = message.capitalize()
    return new_message

greeting = greet()
print(greeting)

# It works! We get "Hello". But this will not work:

print(new_message)

# You also cannot run greet() or try print(greeting) in another py file.

# Code Experiments: