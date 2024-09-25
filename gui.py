import functions
import FreeSimpleGUI as sg


label = sg.Text("Type in a To-Do Item: ")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")

window = sg.Window('My Todo App', layout=[[label], "", [input_box, add_button]])
window.read()
window.close()

