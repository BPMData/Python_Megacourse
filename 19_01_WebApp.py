import time

import streamlit as st

from Modules.Functions_Day16_GUI import get_save, write_save, ord

daymonth = time.strftime("%A, %B ")
date = ord(int(time.strftime("%d")))
dayofyear = ord(int(time.strftime("%j")))
time = time.strftime("%I:%M:%S %p")

datetimegreeting1 = f"Hello! The current date is {daymonth}{date}.\nThe time at which you opened this program was {time}."
datetimegreeting2 = f"It is the {dayofyear} day of the year."

todos = get_save()

# def add_todo():
#     new_todo = st.session_state["text"]
#     todos.append(new_todo + "\n")
#     write_save(todos)



st.title("My To-Do App")
st.subheader("A clean To-Do app")
st.write(datetimegreeting1)
st.write(datetimegreeting2)
st.write("Does this update in real-time?")
st.write("Woah, it does.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        write_save(todos)
        del st.session_state[todo]
        st.experimental_rerun()

if "temp" not in st.session_state:
    st.session_state["temp"]=""

def add_todo():
    new_todo = st.session_state["text"]
    todos.append(new_todo + "\n")
    write_save(todos)
    st.session_state["temp"] = st.session_state["text"]
    st.session_state["text"] = ""

input = st.text_input(label="Enter a To-Do Item below:", placeholder="Walk the dog...", on_change=add_todo, key="text")

st.button("Add To-Do", key="add")


st.write("Below is your session_state object.")
st.session_state

# I'll try to fix that glitch some other time lol. Maybe the instructor will show me how to fix it.

