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

def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo + "\n")
    write_save(todos)


st.title("My To-Do App")
st.subheader("A clean To-Do app")
st.write(datetimegreeting1)
st.write(datetimegreeting2)
st.write("Does this update in real-time?")
st.write("Woah, it does.")

st.checkbox("Checkbox 1")
st.checkbox("Checkbox 2")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="Enter a To-Do Item below:", placeholder="Walk the dog...", on_change=add_todo, key="new_todo")

st.write("Below is your session_state object.")
st.session_state