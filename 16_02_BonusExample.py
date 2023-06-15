# See 16_01_Backend and Main_16.py
# https://www.udemy.com/course/the-python-mega-course/learn/lecture/34598404#learning-tools

import PySimpleGUI as sg

selectlabel = sg.Text("Selected file paths:")
selectinput = sg.Input()
selectbutton = sg.FilesBrowse("Select files to compress:")
selects = [selectlabel, selectinput,selectbutton]

destlabel = sg.Text("Destination directory for .zip file:")
destinput = sg.Input()
destbutton = sg.FolderBrowse("Choose destination directory:")
dests = [destlabel,destinput,destbutton]

compress_button = sg.Button("Compress!")

window = sg.Window("Bonus File Compressor",layout=[[selects], [dests], [compress_button]])
# aha that did work!

window.read()

window.close()