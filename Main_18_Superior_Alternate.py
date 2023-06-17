import time

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
                         key="TODO")

buttontext = ("Garamond", 14)

add_button = sg.Button(image_source="add.png", key="add", mouseover_colors="dark orange", tooltip="Add a To-Do Item")

list_box = sg.Listbox(values=get_save(), enable_events=True, size=[45, 10],
                      key = "todos")

edit_button = sg.Button(image_source="edit.png",tooltip="Edit a To-Do Item",
                            key="edit", mouseover_colors="dark orange")

complete_button = sg.Button(image_source="completebw.png",tooltip="Complete a To-Do Item",
                            key="complete", mouseover_colors="dark orange")

exit_button = sg.Button(image_source="exit.png",tooltip="Exit program",
                            key="exit", mouseover_colors="dark orange")

buttoncol = [[edit_button], [complete_button]]

window = sg.Window("Bryan's Python To-Do App",
                   layout=[[datetimegreeting], [clock], [hello],
                           [input_box, add_button],
                           [list_box, sg.Column(buttoncol)],
                           [exit_button]],
                   font=("Garamond", 18))

edit_popup_active = False
edit_window_active = False

while True:
    event, values = window.read()

    print(f"Event is {event}")  # Gets the label of the button that was pressed
    print(f"values is {values}")  # Gets the actual input to the field associated with that button.
    print(f"values['todos'] is {values['todos']}")

    # window["clock"].update(value=f"The current time is: {strftime('%b %d, %Y %I:%M:%S %p')}.", text_color="sienna3")

    match event:

        case "add":
            todos = get_save()
            new_todo = values["TODO"] + "\n"
            todos.append(new_todo)
            write_save(todos)
            window["todos"].update(values=todos)

        case "edit":
            if not edit_popup_active and not edit_window_active:
                edit_popup_active = True

                # Create the pop-up window to ask user to select what to edit.
                popup_layout = [
                    [sg.Text("Please double-click the To-Do Item which you would like to edit.")],
                    [sg.Button("Nevermind", key="nevermind")]
                ]
                popup_window = sg.Window("Select To-Do", layout=popup_layout)
                popup_window.read()
                popup_window.close()

            elif event == "todos" and edit_popup_active and not edit_window_active:

                if values["todos"]:
                    selected_todo = values["todos"][0]

                    # Close first pop-up
                    popup_window.close()

                    # Create second pop-up
                    edit_layout = [
                        [sg.Text("Please what you'd like to edit this To-Do Item to be.")],
                        [sg.Input(key="edit_input")],
                        [sg.Button("Finish editing", key="edit_confirm"),
                         sg.Button("Nevermind", key="edit_nevermind")]
                    ]
                    edit_window = sg.Window("Edit To-Do", layout=edit_layout)
                    edit_window.read()
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

            #
            # while True:
            #     edit_event, edit_values = edit_window.read()
            #
            #     if edit_event == "edit_confirm":
            #         new_todo = edit_values["edit_input"] + "\n"
            #         todos = get_save()
            #         index = todos.index(todo_to_edit)
            #         todos[index] = new_todo
            #         write_save(todos)
            #         window["todos"].update(values=todos)
            #
            #         edit_window.close()
            #         break
            #
            #     elif edit_event == sg.WINDOW_CLOSED:
            #         break
            #
            # # except IndexError:
            # #     sg.popup("Please select an item to edit before clicking the Edit button.", no_titlebar=True,
            # #              font=("Garamond", 14))

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

