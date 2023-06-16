# password = input("Enter a new password:")
#
# digit = False
# digits = []
#
# for i in password:
#     if i.isdigit():
#         digit = True
#         digits.append(digit)
#
# print(f"Your password contains {sum(digits)} numbers.")
#
# # Boom I totally noscoped that, no chatgpt, no stackoverflow, nothing.
#  XXXXXXXX

# def foo(oz):
#     mls = oz*29.57353
#     print(mls)
#     return(mls)
# XXXXXXXXXXXXXXXXX

import PySimpleGUI as sg


def km_to_miles(km):
    return int(km) / 1.6


label = sg.Text("Kilometers: ")
input_box = sg.InputText(tooltip="Enter todo", key="kms")
miles_button = sg.Button("Convert")

output = sg.Text(key="output")

window = sg.Window('Km to Miles Converter',
                   layout=[[label, input_box], [miles_button, output]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read()
    match event:
        case "Convert":
            km = values["kms"]
            result = km_to_miles(km)
            window['output'].update(value=result)
        case sg.WIN_CLOSED:
            break

window.close()