import functions
import FreeSimpleGUI as sg


label = sg.Text("Type in a To-Do Item: ")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add", key="add")

button_quit = sg.Button("Close", key="quit")

window = sg.Window('My Todo App',
                   layout=[[label], "",
                           [input_box, add_button],
                           [button_quit]
                           ],
                   font=('Helvetica', 20)
                   )
while True:
    event, values = window.read()
    print(event, " ", values)
    match event:
        case "add":
            todos = functions.get_todos()
            new_todos = values['todo'] + "\n"
            todos.append(new_todos)
            functions.write_todos(todos)
        case "close":
            break
        case sg.WIN_CLOSED:
            break

window.close()
