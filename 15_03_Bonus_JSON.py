import json

with open("TestDir/QuizQuestions.json","r") as file:
    content = file.read()

print(content)

data = json.loads(content)

print(data)

print("Types")
print(type(content)) # str
print(type(data)) # list

# The nested for loop is intentional & necessary to bring about the correct outcome
for question in data:
    print(question["question_text"])
    for choices in question["choices"]:
        print(choices)

print("-------------------------------------------------------------------")
# Better version
score = 0

for index, question in enumerate(data):
    print(f"Question {index+1}: {question['question_text']}")
    for index, choices in enumerate(question["choices"]):
        print(index+1, "-", choices)
    user_choice = int(input("Enter your answer, as a number:"))

    question["user_choice"] = user_choice # we injected a key-pair into our dictionary question: "user_choice" is the key, user_choice is the value of that key
    if question["user_choice"] == question["correct_answer"]:
        question["result"] = "Right answer, amigo!"
        score = score+1
    else:
        question["result"] = "Wrong answer, hombre/ette."


# Print out the answers in a user-friendly way

for index, question in enumerate(data):
    message = f"Your answer to Question {index+1}: {question['user_choice']},\n" \
              f"Correct answer to Question {index+1}: {question['correct_answer']}\n" \
              f"{question['result']}"

    print(message)

print(f"Your total score was {score} out of {len(data)}.")
