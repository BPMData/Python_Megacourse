FILEPATH = "Modules/Todos_Save.txt"
def get_save(filepath=FILEPATH): # everything after the = sign is the default argument/parameter.
    """Loads your To-Do Items from the specified Save.txt file.
    Reads the text file and returns the list of to-do items."""
    with open(filepath, "r") as savefile_local:
        todos_local = savefile_local.readlines()
    return todos_local

def write_save(todos_arg, filepath=FILEPATH): # Non-default parameters must always precede default parameters. IDK why.
    """Writes the current list saved in the variable todos to your specified Save.txt file.
    Thereby, when you run the program again, your To-Do Items will be saved."""
    with open(filepath,"w") as savefile_local:
        savefile_local.writelines(todos_arg)

# Example of a conditional block

if __name__ == "__main__":
    print("Hello")
    message = """I am a 
    Multi-Line
        Conditional 
            Code 
                Block"""

    print(message)

def ord(n):
    return str(n)+("th" if 4<=n%100<=20 else {1:"st",2:"nd",3:"rd"}.get(n%10, "th"))

def dtStylish(dt,f):
    return dt.strftime(f).replace("{th}", ord(dt.day))

import textwrap
import time

import PySimpleGUI as sg

# from multiprocessing import Process

'''
    Notification Window Demo Program
    Shamelessly stolen from PySimpleGUI user ncotrb

    Displays a small informational window with an Icon and a message in the lower right corner of the display
    Option to fade in/out or immediatealy display.
'''

# -------------------------------------------------------------------
# fade in/out info and default window alpha
USE_FADE_IN = True
WINDOW_ALPHA = 0.9
WIN_MARGIN = 60

# colors
WIN_COLOR = "#282828"
TEXT_COLOR = "#ffffff"

DEFAULT_DISPLAY_DURATION_IN_MILLISECONDS = 10000


# -------------------------------------------------------------------

def display_notification(title, message, icon, display_duration_in_ms=DEFAULT_DISPLAY_DURATION_IN_MILLISECONDS,
                         use_fade_in=True, location=None):
        # Compute location and size of the window
        message = textwrap.fill(message, 50)
        win_msg_lines = message.count("\n") + 1

        screen_res_x, screen_res_y = sg.Window.get_screen_size()
        win_margin = WIN_MARGIN  # distance from screen edges
        win_width, win_height = 364, 66 + (14.8 * win_msg_lines)

        layout = [[sg.Graph(canvas_size=(win_width, win_height), graph_bottom_left=(0, win_height),
                            graph_top_right=(win_width, 0), key="-GRAPH-", background_color=WIN_COLOR,
                            enable_events=True)]]

        win_location = location if location is not None else (
        screen_res_x - win_width - win_margin, screen_res_y - win_height - win_margin)
        window = sg.Window(title, layout, background_color=WIN_COLOR, no_titlebar=True,
                           location=win_location, keep_on_top=True, alpha_channel=0, margins=(0, 0),
                           element_padding=(0, 0),
                           finalize=True)

        window["-GRAPH-"].draw_rectangle((win_width, win_height), (-win_width, -win_height), fill_color=WIN_COLOR,
                                         line_color=WIN_COLOR)
        window["-GRAPH-"].draw_image(data=icon, location=(20, 20))
        window["-GRAPH-"].draw_text(title, location=(64, 20), color=TEXT_COLOR, font=("Arial", 12, "bold"),
                                    text_location=sg.TEXT_LOCATION_TOP_LEFT)
        window["-GRAPH-"].draw_text(message, location=(64, 44), color=TEXT_COLOR, font=("Arial", 9),
                                    text_location=sg.TEXT_LOCATION_TOP_LEFT)

        window["-GRAPH-"].Widget.config(cursor="hand2")

        if use_fade_in == True:
                for i in range(1, int(WINDOW_ALPHA * 100)):  # fade in
                        window.set_alpha(i / 100)
                        window.refresh()
                        time.sleep(.02)
                event, values = window(timeout=display_duration_in_ms)
                for i in range(int(WINDOW_ALPHA * 100), 1, -1):  # fade out
                        window.set_alpha(i / 100)
                        window.refresh()
                        time.sleep(.02)
        else:
                window.set_alpha(WINDOW_ALPHA)
                event, values = window(timeout=display_duration_in_ms)

        print(f'The event was {event}')


# Base64 Images to use as icons in the window
img_error = b'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAA3NCSVQICAjb4U/gAAAACXBIWXMAAADlAAAA5QGP5Zs8AAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAIpQTFRF////20lt30Bg30pg4FJc409g4FBe4E9f4U9f4U9g4U9f4E9g31Bf4E9f4E9f4E9f4E9f4E9f4FFh4Vdm4lhn42Bv5GNx5W575nJ/6HqH6HyI6YCM6YGM6YGN6oaR8Kev9MPI9cbM9snO9s3R+Nfb+dzg+d/i++vt/O7v/fb3/vj5//z8//7+////KofnuQAAABF0Uk5TAAcIGBktSYSXmMHI2uPy8/XVqDFbAAAA8UlEQVQ4y4VT15LCMBBTQkgPYem9d9D//x4P2I7vILN68kj2WtsAhyDO8rKuyzyLA3wjSnvi0Eujf3KY9OUP+kno651CvlB0Gr1byQ9UXff+py5SmRhhIS0oPj4SaUUCAJHxP9+tLb/ezU0uEYDUsCc+l5/T8smTIVMgsPXZkvepiMj0Tm5txQLENu7gSF7HIuMreRxYNkbmHI0u5Hk4PJOXkSMz5I3nyY08HMjbpOFylF5WswdJPmYeVaL28968yNfGZ2r9gvqFalJNUy2UWmq1Wa7di/3Kxl3tF1671YHRR04dWn3s9cXRV09f3vb1fwPD7z9j1WgeRgAAAABJRU5ErkJggg=='
img_success = b'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAA3NCSVQICAjb4U/gAAAACXBIWXMAAAEKAAABCgEWpLzLAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAHJQTFRF////ZsxmbbZJYL9gZrtVar9VZsJcbMRYaMZVasFYaL9XbMFbasRZaMFZacRXa8NYasFaasJaasFZasJaasNZasNYasJYasJZasJZasJZasJZasJZasJYasJZasJZasJZasJZasJaasJZasJZasJZasJZ2IAizQAAACV0Uk5TAAUHCA8YGRobHSwtPEJJUVtghJeYrbDByNjZ2tvj6vLz9fb3/CyrN0oAAADnSURBVDjLjZPbWoUgFIQnbNPBIgNKiwwo5v1fsQvMvUXI5oqPf4DFOgCrhLKjC8GNVgnsJY3nKm9kgTsduVHU3SU/TdxpOp15P7OiuV/PVzk5L3d0ExuachyaTWkAkLFtiBKAqZHPh/yuAYSv8R7XE0l6AVXnwBNJUsE2+GMOzWL8k3OEW7a/q5wOIS9e7t5qnGExvF5Bvlc4w/LEM4Abt+d0S5BpAHD7seMcf7+ZHfclp10TlYZc2y2nOqc6OwruxUWx0rDjNJtyp6HkUW4bJn0VWdf/a7nDpj1u++PBOR694+Ftj/8PKNdnDLn/V8YAAAAASUVORK5CYII='


def process(location=None):
        title = "Action completed successfully"
        message = "This message is intended to inform you that the action you have performed has been successful. There is no need for further action."
        display_notification(title, message, img_success, 4000, True, location=location)


todo1 = "Walk the dog"
todo2 = 'Have the dog put down for rabies'

def todosuccessfuledit(location=None):
        title = "To-Do Item Edited Successfully"
        message = f"''{todo1}'' was successfully changed to ''{todo2}''. There is no need for further action."
        display_notification(title, message, img_success, 400, True, location=location)

def compressdone(location=None):
    title = "Files compressed succesfully!"
    message = "compressed.zip created. There is no need for further action."
    display_notification(title, message, img_success, 400, True, location=location)

if __name__ == '__main__':
        todosuccessfuledit(location=(WIN_MARGIN, WIN_MARGIN))

        # was experimenting with using multiprocessing with these windows.  Couldn't get it to work
        # p = Process(target=process)
        # p1 = Process(target=process, args=((WIN_MARGIN, WIN_MARGIN),))
        # p1.start()
        # p.start()
        # p.join()
        # p1.join()
