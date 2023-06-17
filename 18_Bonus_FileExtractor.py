import pathlib

import PySimpleGUI as sg

from Modules.Functions_Day16_GUI import fadepopup
from Modules.ZipExtractor_Bonus_Day18 import extractit

sg.theme("Topanga")

selectlabel = sg.Text("Select the archive you wish to extract:")
selectinput = sg.Input(size=64)
selectbutton = sg.FileBrowse("Choose archive",
                             key="archive")  # not FILESbrowse cuz we want them only to be able to pick one

selectrow = [selectlabel, selectinput, selectbutton]

destlabel = sg.Text("Select the destination to which you wish to extract the archive:")
destinput = sg.Input()
destbutton = sg.FolderBrowse("Choose destination",
                             key="dest")  # not FILESbrowse cuz we want them only to be able to pick one

destrow = [destlabel, destinput, destbutton]

extractbutton = sg.Button("Extract!", key="eiaeo")
output_text = sg.Text(key="output", text_color="yellow")

exitbutton = sg.Button(image_source="exit.png", key="exit", tooltip="Exit the program.")

window = sg.Window("Bonus: File Extractor",
                   layout=[
                       [selectrow],
                       [destrow],
                       [extractbutton, output_text],
                       [exitbutton]
                   ], font=16)
while True:
    event, values = window.read()

    # if event == "exit":
    #     break
    # okay their way is better

    match event:
        case "exit":
            break
        case sg.WINDOW_CLOSED:
            break

    filepath = values["archive"]
    dest_path = values["dest"]

    if dest_path == "":
        dest_path = pathlib.Path(filepath).parent
    else:
        dest_path == dest_path
    extractit(filepath, dest_path)
    window["output"].update(value='Extraction completed successfully.')
    fadepopup("Extraction complete!",
              "Files were successfully extracted. There is no need for further action.")

window.close()
