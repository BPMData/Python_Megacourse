import os
import time
from time import strftime

import PySimpleGUI as sg

from Modules.Functions_Day16_GUI import fadepopup
from Modules.Functions_Day16_GUI import ord, get_save, write_save

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

sg.theme("DarkBrown1")

daymonth = time.strftime("%A, %B ")
date = ord(int(time.strftime("%d")))
dayofyear = ord(int(time.strftime("%j")))
time = time.strftime("%I:%M:%S %p")

datetimegreeting = sg.Text(
    f"Hello! The current date is {daymonth}{date}.\nThe time at which you opened this program was {time}.\n"
    f"It is the {dayofyear} day of the year.", text_color="LemonChiffon4", justification="left")

clock = sg.Text("", key="clock")

hello = sg.Text("Welcome to your To-Do List.", justification="center")

input_text = sg.Text("New To-Do Item:")
input_box = sg.InputText(enable_events=True,
                         key="TODO", size=29,tooltip="Add a To-Do Item:")

buttontext = ("Garamond", 16)

add_button = sg.Button("Add Item", key="add", mouseover_colors="dark orange", font=buttontext)

list_box = sg.Listbox(values=get_save(), enable_events=True, size=[45, 10],
                      key = "todos")

edit_button = sg.Button("Edit a To-Do Item", key="edit", mouseover_colors="dark orange",
                        font=buttontext, size=19)

complete_button = sg.Button("Complete a To-Do Item",
                            key="complete", mouseover_colors="dark orange",
                            font=buttontext, size=19)

exit_button = sg.Button("Exit program", key="exit", mouseover_colors="dark orange",
                        font=buttontext, size = 20)


buttoncol = [[sg.Text("For Existing To-Do Items:")], [edit_button], [complete_button]]

window = sg.Window("Bryan's Python To-Do App",
                   layout=[[datetimegreeting],[clock], [hello],
                           [input_text, input_box, add_button],
                           [list_box, sg.Column(buttoncol, element_justification="center")],
                           [exit_button]],
                   font=("Garamond", 18))

edit_popup_active = False
edit_window_active = False

while True:
    event, values = window.read(timeout=400)

    window["clock"].update(value=f"The current time is: {strftime('%b %d, %Y %I:%M:%S %p')}.")

    match event:

        case "add":
            todos = get_save()
            new_todo = values["TODO"] + "\n"
            todos.append(new_todo)
            write_save(todos)
            window["todos"].update(values=todos)
            window["TODO"].update(value="")

        case "edit":
            if not edit_popup_active and not edit_window_active:
                edit_popup_active = True

                # Create the pop-up window to ask user to select what to edit.
                fadepopup("Please select the item to edit.",
                          "The next item in the list you select will be brought up to edit.")

        case "todos":
            if edit_popup_active and not edit_window_active:
                while True:

                    if values["todos"]:
                        selected_todo = values["todos"][0]

                        # Create second pop-up
                        edit_layout = [
                            [sg.Text("Please what you'd like to edit this To-Do Item to be.")],
                            [sg.Input(key="edit_input")],
                            [sg.Button("Finish editing", key="edit_confirm"),
                             sg.Button("Nevermind", key="edit_nevermind")]
                        ]
                        edit_window = sg.Window("Edit To-Do", layout=edit_layout)
                        edit_window_active = True
###
                        edit_event, edit_values = edit_window.read()
###
                        if edit_event == "edit_confirm" and edit_window_active:
                            new_todo = edit_values["edit_input"] + "\n"
                            todos = get_save()
                            index = todos.index(selected_todo)
                            todos[index] = new_todo
                            write_save(todos)
                            window["todos"].update(values=todos)
                            edit_popup_active = False
                            edit_window_active = False
                            edit_window.close()
                            break

                        elif edit_event == "edit_nevermind" and edit_window_active:
                            edit_window.close()
                            edit_popup_active = False
                            edit_window_active = False
                            break

                        elif edit_event == sg.WINDOW_CLOSED:
                            edit_window.close()
                            edit_popup_active = False
                            edit_window_active = False
                            break

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

        case "exit":
            break

        case sg.WINDOW_CLOSED:
            break

print("Bye!")
window.close()

