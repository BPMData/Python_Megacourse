# https://www.udemy.com/course/the-python-mega-course/learn/lecture/34598594#learning-tools
import pathlib

import PySimpleGUI as sg

from Modules.Functions_Day16_GUI import compressdone
from Modules.ZipCreator_Bonus_Day17 import zipit

sg.theme("DarkAmber")

selectlabel = sg.Text("Selected file paths:")
selectinput = sg.Input()
selectbutton = sg.FilesBrowse("Select files to compress:", key="selected")
selects = [selectlabel, selectinput, selectbutton]

destlabel = sg.Text("Destination directory for .zip file:")
destinput = sg.Input()
destbutton = sg.FolderBrowse("Choose destination directory:", key="dest")
dests = [destlabel, destinput, destbutton]

compress_button = sg.Button("Compress!")

output = sg.Text(key="output",text_color="green")

window = sg.Window("Bonus File Compressor",
                   layout=[[selects], [dests], [compress_button, output]])
# aha that did work!

while True:
    event, values = window.read()
    print(f"Event is {event}.")
    print()
    print()
    print(f"Values is {values}")
    filepaths = values["selected"].split(";")
    destpath = values["dest"]
    # The following four lines of code make it so the default directory is the directory of the files if nothing is selected. Optimal functionality imo.
    if destpath == "":
        destpath = pathlib.Path(filepaths[0]).parent
    else:
        destpath = destpath
    zipit(filepaths, destpath)
    window["output"].update(value="Compression completed!")
    compressdone() # that's cool as hell, yeah!

window.close()