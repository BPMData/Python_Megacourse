# https://www.udemy.com/course/the-python-mega-course/learn/lecture/34598582#learning-tools
# See 16_01_Backend

import time

import PySimpleGUI as sg

from Modules.Functions_Day16_GUI import ord, get_save, write_save

daymonth = time.strftime("%A, %B ")
date = ord(int(time.strftime("%d")))
dayofyear = ord(int(time.strftime("%j")))
time = time.strftime("%I:%M:%S %p")


datetimegreeting = sg.Text(f"Hello! The current date is {daymonth}{date}.\nThe current time is {time}.\n"
      f"It is the {dayofyear} day of the year.\n\n"
      "Welcome to your To-Do List.\n")

input_box = sg.InputText(tooltip="Enter To-Do Item:", key="todo")

add_button = sg.Button("Add To-Do")

window = sg.Window("Bryan's Python To-Do App",
                   layout=[[datetimegreeting], [input_box, add_button]],
                   font =("Garamond",20))

while True:
    event, values = window.read()
    print(event)  # Gets the label of the button that was pressed
    print(values)  # Gets the actual input to the field associated with that button.

    match event:
        case "Add To-Do":
            todos = get_save()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            write_save(todos)
        case sg.WINDOW_CLOSED:
            break


window.close()