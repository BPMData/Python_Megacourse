import pathlib
import zipfile

filepaths=[1,2,3]

def zipit(filepaths, dest_dir): # You have to add the code to edit the default directory to the main.py file, not here.
    dest_path = pathlib.Path(dest_dir, "compressed.zip")
    with zipfile.ZipFile(dest_path, "w") as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)

if __name__ == "__main__":
    zipit(["Todos_Save.txt", "Bonus_14_day.py"], dest_dir="") # dest_dir="" makes the zip appear in the folder of the files, which IMO is the preferred outcome.
