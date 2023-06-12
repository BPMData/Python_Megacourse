def get_save(filepath="15_Save.txt"): # everything after the = sign is the default argument/parameter.
    """Loads your To-Do Items from the specified Save.txt file.
    Reads the text file and returns the list of to-do items."""
    with open(filepath, "r") as savefile_local:
        todos_local = savefile_local.readlines()
    return todos_local

def write_save(todos_arg, filepath="15_Save.txt"): # Non-default parameters must always precede default parameters. IDK why.
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

