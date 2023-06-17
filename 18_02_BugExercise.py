# import PySimpleGUI as sg
#
#
# def convert(feet, inches):
#     meters = feet * 0.3048 + inches * 0.0254
#     return meters
#
#
# sg.theme("Black")
#
# feet_label = sg.Text("Enter feet: ")
# feet_input = sg.Input(key="feet")
#
# inches_label = sg.Text("Enter inches: ")
# inches_input = sg.Input(key="inches")
#
# button = sg.Button("Convert")
# output_label = sg.Text("", key="output")
# exit_button = sg.Button("Exit")
#
# window = sg.Window("Convertor",
#                    layout=[[feet_label, feet_input],
#                            [inches_label, inches_input],
#                            [button, exit_button, output_label]])
#
# while True:
#     event, values = window.read()
#     try:
#         match event:
#             case "Exit":
#                 break
#             case sg.WIN_CLOSED:
#                 break
#         feet = float(values["feet"])
#         inches = float(values["inches"])
#
#         result = convert(feet, inches)
#         window["output"].update(value=f"{result} m", text_color="white")
#     except ValueError:
#         sg.popup("Please provide two numbers.", no_titlebar=True)
#
#
# window.close()

import PySimpleGUI as sg

from Modules.Functions_Day16_GUI import get_save, write_save

input_box = sg.InputText("Enter input here:", enable_events=True,
                         key="TODO")

buttontext = ("Garamond", 14)

add_button = sg.Button("Add a To-Do", key="add", font=buttontext)

list_box = sg.Listbox(values=get_save(), key="todos",
                      enable_events=True, size=[45, 10])

edit_button = sg.Button("Edit a To-Do", key="edit", font=buttontext)

complete_button = sg.Button("Complete a To-Do", key="complete", font=buttontext)

exit_button = sg.Button("Exit", key="exit", font=buttontext)



window = sg.Window("Bryan's Python To-Do App",
                   layout=[[input_box], [add_button, edit_button, complete_button],
                           [list_box],
                           [exit_button]],
                   font=("Garamond", 18))

while True:
    event, values = window.read()

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

                # Create a pop-up window for editing
                edit_layout = [
                    [sg.Text("Please select what you'd like to change this To-Do to be.")],
                    [sg.Input(key="edit_input")],
                    [sg.Button("Edit", key="edit_confirm")]
                ]
                edit_window = sg.Window("Edit To-Do", layout=edit_layout)

                while True:
                    edit_event, edit_values = edit_window.read()

                    if edit_event == "edit_confirm":
                        new_todo = edit_values["edit_input"] + "\n"
                        todos = get_save()
                        index = todos.index(todo_to_edit)
                        todos[index] = new_todo
                        write_save(todos)
                        window["todos"].update(values=todos)

                        edit_window.close()
                        break

                    elif edit_event == sg.WINDOW_CLOSED:
                        break

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
