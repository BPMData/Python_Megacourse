password = input("Enter a new password:")

result = [] # create a blank list to store our checks for each of the 3 conditions of a strong password:

# A strong password should:
    # 1) Be at least 8 characters long
    # 2) Have at least 3 numeric digits
    # 3) Have at least one upper and one lower case character

if len(password) >= 8:
    result.append(True)

# check if each character of password is a digit, and we have at least 3 digits:

digit = False
digits = []

for i in password:
    if i.isdigit():
        digit = True
        digits.append(digit)

print(f"Your password contains {sum(digits)} numbers.")

if sum(digits) >= 3:
    result.append(True)
else:
    result.append(False)

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
    result.append(True)
else:
    result.append(False)

print(f"Your password passes {sum(result)} of the 3 criterion tests.")

print(result)

# if sum(result) == 3:
#     print("You have entered a Strong Password.")
# else:
#     print("You have entered a Weak Password.")

if all(result): # returns as True IFF every boolean in the containment unit is True.
    print("You have entered a Strong Password.")
else:
    print("You have entered a Weak Password.")

# Now let's rewrite all this code using a DICTIONARY for result instead of a LIST.
# Complication: the method .append() does NOT exist for Dictionaries. SO:

#################################################################################################################################################
#################################################################################################################################################
#################################################################################################################################################
#################################################################################################################################################

