def strength(password):
    result = {}  # create a blank DICTIONARY to store our checks for each of the 3 conditions of a strong password:

    if len(password) >= 8:
        result["Password length is at least 8 characters"] = True
    else:
        result["Password length is at least 8 characters"] = False

    # check if each character of password is a digit, and we have at least 3 digits:

    digit = False
    digits = []

    for i in password:
        if i.isdigit():
            digit = True
            digits.append(digit)

    print(f"Your password contains {sum(digits)} numbers.")

    if sum(digits) >= 3:
        result["# of Digits in Password is at least 3"] = True
    else:
        result["# of Digits in Password is at least 3"] = False

    # Check if we have at least one uppercase and one lowercase character

    uppercase = False
    uppers = []

    for i in password:
        if i.isupper():
            uppercase = True
            uppers.append(uppercase)
    print(f"Your password contains {sum(uppers)} uppercase characters.")

    lowercase = False
    lowers = []

    for i in password:
        if i.islower():
            lowercase = True
            lowers.append(lowercase)
    print(f"Your password contains {sum(lowers)} lowercase characters.")

    if sum(lowers) >= 1 and sum(uppers) >= 1:
        result["At least 1 uppercase and lowercase character"] = True
    else:
        result["At least 1 uppercase and lowercase character"] = False

    passes = sum(value for value in result.values())

    print(f"Your password passes {passes} of the 3 criterion tests.")

    print(result)

    # if sum(result) == 3:
    #     print("You have entered a Strong Password.")
    # else:
    #     print("You have entered a Weak Password.")

    if all(result.values()):  # returns as True IFF every boolean in the containment unit is True.
        print("You have entered a Strong Password.")
    else:
        print("You have entered a Weak Password.")

password = input("Enter a new password:")
strength(password)