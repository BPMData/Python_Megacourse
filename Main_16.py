# See 16_01_Backend
# https://www.udemy.com/course/the-python-mega-course/learn/lecture/34598394#learning-tools

import time

import PySimpleGUI as sg

from Modules.Functions_Day16_GUI import ord

daymonth = time.strftime("%A, %B ")
date = ord(int(time.strftime("%d")))
dayofyear = ord(int(time.strftime("%j")))
time = time.strftime("%I:%M:%S %p")


datetimegreeting = sg.Text(f"Hello! The current date is {daymonth}{date}.\nThe current time is {time}.\n"
      f"It is the {dayofyear} day of the year.\n\n"
      "Welcome to your To-Do List.\n")

input_box = sg.InputText("Enter To-Do Item:")

add_button = sg.Button("Add To-Do")

window = sg.Window("Bryan's Python To-Do App", layout=[[datetimegreeting],[input_box, add_button]])

window.read()
window.close()