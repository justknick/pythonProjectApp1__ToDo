import streamlit as st
import functions

my_todos = functions.get_todos()

string_title = "My ToDo App"
string_subheader = "This is my web app. Thank you for using it."
string_text = "Use this to do app to increase your productivity. "
string_input = "enter to do item"


st.title(string_title)
st.subheader(string_subheader)
st.text(string_text)

for todo in my_todos:
    st.checkbox(todo)

# st.checkbox("shop for groceries")

st.text_input(label="", placeholder=string_input)

print("loaded")

st.session_state