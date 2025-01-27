import functions
import FreeSimpleGUI as sg
import time
import os

if not os.path.exists('todos.txt'):
    with open('todos.txt', "w") as file:
        pass

sg.theme("DarkTeal2")

label_timestamp = sg.Text('', key='timestamp')
label_add = sg.Text("Type in a To-Do Item: ")
input_box = sg.InputText(tooltip="Enter todo", key='input_box')
button_add = sg.Button("Add", key='add', size=10, mouseover_colors="LightBlue2",
                       tooltip="Adds To-Do item to the list")

label_list_box = sg.Text("My To-Do List: ")
list_box = sg.Listbox(values=functions.get_todos(), key='selected',
                      enable_events=True, size=[45, 10])
button_edit = sg.Button("Edit", key='edit',
                       tooltip="Updates To-Do item in the list")

button_quit = sg.Button("Quit", key='quit')

button_complete = sg.Button("Done", key='complete', mouseover_colors="LightBlue2",
                       tooltip="Removes To-Do item from the list")


# window instance
window = sg.Window('My Todo App',
                   layout=[[label_timestamp],
                           [label_add], "",
                           [input_box, button_add],
                           [label_list_box],
                           [list_box, button_edit, button_complete],
                           [button_quit]
                           ],
                   font=('Helvetica', 14)
                   )
while True:
    event, values = window.read(timeout=200)
    window["timestamp"].update(value=time.strftime("%b, %d,  %Y  %H:%M:%S"))
    # print(1, " events ", event)
    # print(2, " values ", values)
    match event:
        case "add":
            todos_list = functions.get_todos()
            new_todo = values['input_box'] + "\n"
            todos_list.append(new_todo)
            functions.write_todos(todos_list)
            window['selected'].update(values=todos_list)
            window['input_box'].update(value='')

        case "edit":
            try:
                todo_to_edit = values['selected'][0]
                new_todo = values['input_box']
                todos_list = functions.get_todos()
                index_of_edit = todos_list.index(todo_to_edit)
                todos_list[index_of_edit] = new_todo + "\n"
                functions.write_todos(todos_list)
                window['selected'].update(values=todos_list)
                window['input_box'].update(value='')
            except IndexError:
                sg.popup("Please select an item first.", font=('Helvetica', 14))

        case "complete":
            try:
                todo_to_complete = values['selected'][0]
                # print("You selected : ", todo_to_complete.rstrip('\n'))
                todos_list = functions.get_todos()
                todos_list.remove(todo_to_complete)
                functions.write_todos(todos_list)
                window['selected'].update(values=todos_list)
                window['input_box'].update(value='')
            except IndexError:
                sg.popup("Please select an item first.", font=('Helvetica', 14))

        case 'selected':
            window['input_box'].update(value=values['selected'][0].rstrip('\n'))

        case "quit":
            break
        case sg.WIN_CLOSED:
            break

window.close()
