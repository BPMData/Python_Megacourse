import PySimpleGUI as sg

from Modules.Functions_Day16_GUI import get_save, write_save

input_box = sg.InputText("Enter input here:", enable_events=True, key="TODO")

buttontext = ("Garamond", 14)

add_button = sg.Button("Add a To-Do", key="add", font=buttontext)

list_box = sg.Listbox(values=get_save(), key="todos", enable_events=True, size=[45, 10])

edit_button = sg.Button("Edit a To-Do", key="edit", font=buttontext)

complete_button = sg.Button("Complete a To-Do", key="complete", font=buttontext)

exit_button = sg.Button("Exit", key="exit", font=buttontext)

window = sg.Window("Bryan's Python To-Do App",
                   layout=[[input_box], [add_button, edit_button, complete_button], [list_box], [exit_button]],
                   font=("Garamond", 18))

edit_popup_active = False
edit_window_active = False

while True:
    event, values = window.read()

    if event == "add":
        todos = get_save()
        new_todo = values["TODO"] + "\n"
        todos.append(new_todo)
        write_save(todos)
        window["todos"].update(values=todos)

    elif event == "edit" and not edit_popup_active and not edit_window_active:
        edit_popup_active = True

        # Create the first pop-up window
        popup_layout = [
            [sg.Text("Please double-click the To-Do Item which you would like to edit.")],
            [sg.Button("Nevermind", key="nevermind")]
        ]
        popup_window = sg.Window("Select To-Do", layout=popup_layout)
        popupevents, popupvalues = popup_window.read()



    elif event == "todos" and edit_popup_active and not edit_window_active:
        edit_popup_active = False

        if popupvalues["todos"]:
            selected_todo = popupvalues["todos"][0]

            # Close the first pop-up window
            popup_window.close()

            # Create the second pop-up window for editing
            edit_layout = [
                [sg.Text("Please enter what you'd like to change this To-Do to be.")],
                [sg.Input(key="edit_input")],
                [sg.Button("Finish editing", key="edit_confirm"), sg.Button("Nevermind", key="edit_nevermind")]
            ]
            edit_window = sg.Window("Edit To-Do", layout=edit_layout)
            edit_window_active = True

    elif event == "edit_confirm" and edit_window_active:
        new_todo = values["edit_input"] + "\n"

        todos = get_save()
        index = todos.index(selected_todo)
        todos[index] = new_todo
        write_save(todos)
        window["todos"].update(values=todos)

        edit_window.close()
        edit_window_active = False

    elif event == "nevermind" and edit_popup_active:
        edit_popup_active = False
        popup_window.close()

    elif event == "edit_nevermind" and edit_window_active:
        edit_window.close()
        edit_window_active = False

    elif event == "complete":
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

    elif event == "TODO":
        if window["TODO"].get() == "Enter input here:":
            window["TODO"].update(value="")

    elif event in (sg.WINDOW_CLOSED, "exit"):
        break

window.close()