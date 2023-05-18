# https://www.udemy.com/course/the-python-mega-course/learn/lecture/32149754#overview

# 1

country = input("Please tell me what country you're from!")
country = country.strip().casefold()




while True:
    country = input("Where do you come from?")

    match country:
        case 'USA':
            print('Hello')
        case 'India':
            print('Namaste')
        case 'Germany':
            print('Hallo')

# ???


while True:
    country = input("Please tell me what country you're from!")
    country = country.casefold().strip()

    match country:
        case "usa":
            print("Hello!")
        case "india":
            print("Namaste!")
        case "germany":
            print("Gutentag.")

# WHEN USING MATCH WITH CASEFOLD MAKE SURE THE STUFF YOU'RE TRYING TO MATCH IS ALL IN LOWERCASE!!!

buttons = ["cancel", "reply", "submit"]

for i in buttons:
    print(i.capitalize())


for item in ["sandals", "glasses", "trousers"]:
    print(item.capitalize())
