import streamlit as st
import functions

def add_todo():
    # get value the user inputs and adds it to the current list
    todo = st.session_state["new_todo"] + "\n"
    print(todo)
    # add new to do item to the todos dictionary
    my_todos.append(todo)
    # update the todo.txt file by calling the write function
    functions.write_todos(my_todos)
    # st.text_input(value='')


my_todos = functions.get_todos()

string_title = "My ToDo App"
string_subheader = "This is my web app. Thank you for using it."
string_text = "Use this to do app to increase your productivity. "
string_input = "enter to do item"


st.title(string_title)
st.subheader(string_subheader)
st.text(string_text)

for index, todo in enumerate(my_todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        print(todo.rstrip('\n'), " (", checkbox, ")")
        my_todos.pop(index)
        functions.write_todos(my_todos)
        del st.session_state[todo]
        st.rerun()

# st.checkbox("shop for groceries")

st.text_input(label="input", label_visibility="hidden", placeholder=string_input,
              on_change=add_todo, key='new_todo')

print("loaded")

st.session_state

