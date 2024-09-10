import functions
import FreeSimpleGUI as sg # "as sg"helps avoid writing FreeSimpleGUI since its long to write.

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")

window = sg.Window('My To-Do App', layout=[[label], [input_box], [add_button]])
window.read()
print("Hello")
window.close()