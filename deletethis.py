password = input("Enter a new password:")

digit = False
digits = []

for i in password:
    if i.isdigit():
        digit = True
        digits.append(digit)

print(f"Your password contains {sum(digits)} numbers.")

# Boom I totally noscoped that, no chatgpt, no stackoverflow, nothing.

