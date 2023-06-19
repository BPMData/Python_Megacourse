import streamlit as st

from Modules.Functions_Day16_GUI import get_save

todos = get_save()

st.title("My To-Do App")
st.subheader("A clean To-Do app")
st.write("Lorem ipsum")

st.checkbox("Checkbox 1")
st.checkbox("Checkbox 2")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="Enter a To-Do Item below:", placeholder="Walk the dog...")
