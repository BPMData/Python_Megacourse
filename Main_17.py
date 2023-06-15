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

input_box = sg.InputText(tooltip="Enter To-Do Item:", key="TODO") # Defining these keys is important, do not forget them!
                                                                    # The all caps is actually necessary, I did that to help me not
                                                                    # make the mistake of confusing TODO and todos
                                                                    # Bro why is that text in yellow?
                                                                    # Lol it's because PyCharm assumes its something I need to flag
                                                                    # as a note to self todo when I go to make a commit.
add_button = sg.Button("Add To-Do")

list_box = sg.Listbox(values=get_save(), key="todos",
                      enable_events=True, size=[45, 10]) # This is where we define our second key, todos, not TODO

edit_button = sg.Button("Edit a To-Do")

window = sg.Window("Bryan's Python To-Do App",
                   layout=[[datetimegreeting], [input_box, add_button], [list_box, edit_button]],
                   font =("Garamond", 18))

while True:
    event, values = window.read()
    print(f"Event is {event}")  # Gets the label of the button that was pressed
    print(f"values is {values}")  # Gets the actual input to the field associated with that button.
    print(f"values['todos'] is {values['todos']}")
#   print(f"values['todos'][0] is {values['todos'][0]}") # This will crash your shit if you try clicking a button before clicking a Listbox item

    match event:
        case "Add To-Do":
            todos = get_save()
            new_todo = values["TODO"] + "\n"
            todos.append(new_todo)
            write_save(todos)
            window["todos"].update(values=todos)
        case "Edit a To-Do":
            todo_to_edit = values["todos"][0]
            new_todo = values["TODO"]

            todos = get_save()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo + "\n"
            write_save(todos)
            window["todos"].update(values=todos) # window[list_box] SEEMS like it should work but WILL NOT. PySimpleGUI is all about them KEYS.
# Code to update the input box to display whatever you selected
        case "todos":
            window["TODO"].update(value=values["todos"][0])
        case sg.WINDOW_CLOSED:
            break

window.close()