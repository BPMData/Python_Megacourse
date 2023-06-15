# def get_maximum():
#     celsius = [14, 15.1, 12.3]
#     maximum = max(celsius)
#     print(maximum)
#
#
# celsius = get_maximum()
#
# fahrenheit = celsius * 1.8 + 32
# print(fahrenheit)

# def get_maximum():
#     celsius = [14, 15.1, 12.3]
#     maximum = max(celsius)
#     return(maximum)
#
#
# celsius = get_maximum()
#
# fahrenheit = celsius * 1.8 + 32
# print(fahrenheit)

# list = ("Apple","Banana","Orange")
#
# print(list)
# print(len(list))
#
# TIME STARTS HERE========================
# import datetime
# def ord(n):
#     return str(n)+("th" if 4<=n%100<=20 else {1:"st",2:"nd",3:"rd"}.get(n%10, "th"))
#
# def dtStylish(dt,f):
#     return dt.strftime(f).replace("{th}", ord(dt.day))
#
# dtStylish(datetime.datetime(2019, 5, 2, 16, 30), '%a the {th} at %I:%M')
#
#
# def ord(n):
#     return str(n)+("th" if 4<=n%100<=20 else {1:"st",2:"nd",3:"rd"}.get(n%10, "th"))
#
# import time
# # Monday, June 12th, 2023, 10:24 am)
# daymonth = time.strftime("%A, %B ")
# date = ord(int(time.strftime("%d")))
# dayofyear = ord(int(time.strftime("%j")))
# time = time.strftime("%I:%M:%S %p")
#
# print(f"Hello! The current date is {daymonth}{date}.\nThe current time is {time}.\n"
#       f"It is the {dayofyear} day of the year.")
# TIME ENDS HERE========================
import PySimpleGUI as sg

selectlabel = sg.Text("Enter feet:")
selectinput = sg.Input()
selects = [selectlabel, selectinput]

destlabel = sg.Text("Enter inches:")
destinput = sg.Input()
dests = [destlabel,destinput]

compress_button = sg.Button("Convert!")

window = sg.Window("Converter",layout=[[selects], [dests], [compress_button]])
# aha that did work!

window.read()

window.close()

import PySimpleGUI as sg

label = sg.Text("What are dolphins?")
option1 = sg.Radio("Amphibians", group_id="question1")
option2 = sg.Radio("Fish", group_id="question1")
option3 = sg.Radio("Mammals", group_id="question1")
option4 = sg.Radio("Birds", group_id="question1")

window = sg.Window("File Compressor",
                   layout=[[label],
                           [option1],
                           [option2],
                           [option3],
                           [option4],
                           ])

window.read()
window.close()