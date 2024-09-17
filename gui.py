import functions
import FreeSimpleGUI as sg  # "as sg"helps avoid writing FreeSimpleGUI since its long to write.

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key='todo')
add_button = sg.Button('Add')
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button('Edit')

layout = [[label], [input_box, add_button], [list_box, edit_button]]

window = sg.Window('My To-Do App', layout=layout, font=("Helvetica", 20))
while True:
    event, values = window.read()
    print(values)
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)   # To change the to-do in the GUI display immediately

        case 'Edit':
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)   # To change the to-do in the GUI display immediately
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:  # to control the killing when we close the GUI
            break

print('Bye')
window.close()
