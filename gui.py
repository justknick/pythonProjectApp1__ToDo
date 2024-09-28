import functions
import FreeSimpleGUI as sg


label_add = sg.Text("Type in a To-Do Item: ")
input_box = sg.InputText(tooltip="Enter todo", key='todo')
button_add = sg.Button("Add", key='add')

label_list_box = sg.Text("My To-Do List: ")
list_box = sg.Listbox(values=functions.get_todos(), key='selected',
                      enable_events=True, size=[45, 10])
button_edit = sg.Button("Edit", key='edit')


button_quit = sg.Button("Close", key='quit')

# window instance
window = sg.Window('My Todo App',
                   layout=[[label_add], "",
                           [input_box, button_add],
                           [label_list_box],
                           [list_box, button_edit],
                           [button_quit]
                           ],
                   font=('Helvetica', 14)
                   )
while True:
    event, values = window.read()
    print(1, " events ", event)
    print(2, " values ", values)
    match event:
        case "add":
            todos_list = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos_list.append(new_todo)
            functions.write_todos(todos_list)
            window['selected'].update(values=todos_list)

        case "edit":
            todo_to_edit = values['selected'][0]
            new_todo = values['todo']
            todos_list = functions.get_todos()
            index_of_edit = todos_list.index(todo_to_edit)
            todos_list[index_of_edit] = new_todo + "\n"
            functions.write_todos(todos_list)
            window['selected'].update(values=todos_list)
        case 'selected':
            window['todo'].update(value=values['selected'][0])
        case "close":
            break
        case sg.WIN_CLOSED:
            break

window.close()
