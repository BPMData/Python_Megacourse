# I overwrote some stuff from Main17 already and I also think I BROKE Main17. To GitHub we go.

# https://www.udemy.com/course/the-python-mega-course/learn/lecture/34598582#learning-tools
# See 16_01_Backend

import time
from time import strftime

import PySimpleGUI as sg

from Modules.Functions_Day16_GUI import ord, get_save, write_save

sg.theme("DarkBrown1")

daymonth = time.strftime("%A, %B ")
date = ord(int(time.strftime("%d")))
dayofyear = ord(int(time.strftime("%j")))
time = time.strftime("%I:%M:%S %p")

datetimegreeting = sg.Text(
    f"Hello! The current date is {daymonth}{date}.\nThe time at which you opened this program was {time}.\n"
    f"It is the {dayofyear} day of the year.", text_color="LemonChiffon4", justification="right")

clock = sg.Text("", key="clock")

hello = sg.Text("Welcome to your To-Do List.\n Enter your input below.", justification="center")

input_box = sg.InputText("Enter input here:", enable_events=True,
                         key="TODO")  # Defining these keys is important, do not forget them!
# The all caps is actually necessary, I did that to help me not
# make the mistake of confusing TODO and todos
# Bro why is that text in yellow?
# Lol it's because PyCharm assumes its something I need to flag
# as a note to self todo when I go to make a commit.

buttontext = ("Garamond", 14)

add_button = sg.Button("Add a To-Do", key="add", font=buttontext, mouseover_colors="dark orange", size=(16, 2))

list_box = sg.Listbox(values=get_save(), key="todos",
                      enable_events=True, size=[45, 10])  # This is where we define our second key, todos, not TODO

edit_button = sg.Button("Edit a To-Do", key="edit", font=buttontext, mouseover_colors="dark orange", size=(16, 2))

complete_button = sg.Button("Complete a To-Do", key="complete", font=buttontext, mouseover_colors="dark orange", size=(16, 2))

exit_button = sg.Button("Exit", key="exit", font=buttontext, mouseover_colors="dark orange", size=15)

buttoncol = [[add_button], [edit_button], [complete_button]]


window = sg.Window("Bryan's Python To-Do App",
                   layout=[[datetimegreeting], [clock], [hello],
                           [input_box],
                           [list_box, sg.Column(buttoncol)],
                           [exit_button]],
                   font=("Garamond", 18))

while True:
    event, values = window.read(timeout=200)

    # window["clock"].update(value=f"The current time is: {strftime('%b %d, %Y %H:%M:%S')} -  His format, I don't like as much.

    window["clock"].update(value=f"The current time is: {strftime('%b %d, %Y %I:%M:%S %p')}.", text_color="sienna3")

    print(f"Event is {event}")  # Gets the label of the button that was pressed
    print(f"values is {values}")  # Gets the actual input to the field associated with that button.
    print(f"values['todos'] is {values['todos']}")
    #   print(f"values['todos'][0] is {values['todos'][0]}") # This will crash your shit if you try clicking a button before clicking a Listbox item

    match event:

        case "add":
            todos = get_save()
            new_todo = values["TODO"] + "\n"
            todos.append(new_todo)
            write_save(todos)
            window["todos"].update(values=todos)

        case "edit":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values["TODO"]

                todos = get_save()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo + "\n"
                write_save(todos)
                window["todos"].update(values=todos)
                # ^^^ Code to update the input box to display whatever you selected
                # window[list_box] SEEMS like it should work but WILL NOT. PySimpleGUI is all about them KEYS.
            except IndexError:
                sg.popup("Please select an item to edit before clicking the Edit button.", no_titlebar=True,
                         font=("Garamond", 14))

        case "todos":
            window["TODO"].update(value=values["todos"][0])

        case "complete":
            try:
                todo_to_complete = values["todos"][0]
                todos = get_save()
                todos.remove(todo_to_complete)
                write_save(todos)
                window["todos"].update(values=todos)
                window["TODO"].update(value="")
            except IndexError:
                sg.popup("Please select an item to complete before clicking the Complete button.", no_titlebar=True,
                         font=("Garamond", 14))

        case "TODO":
            if window["TODO"].get() == "Enter input here:":
                window["TODO"].update(value="")

        case ("exit"):
            break

        case sg.WINDOW_CLOSED:
            break

print("Bye!")
window.close()

# Way to hypothetically generate buttons dynamically. Remove the ''' multiline quotes to run.

'''button_labels = ["Close","Apply","Edit"]

layout = []

for bl in button_labels:
    layout.append([sg.Button(bl)])'''
