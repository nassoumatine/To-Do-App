import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key='todo entered')
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key='existing todos',
                      enable_events=True, size=[45, 10])

edit_button = sg.Button('Edit')
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")
window = sg.Window('My To-Do App',
                   layout=[[label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 20))
while True:
    event, values = window.read()  # This s a tupple of the event(button pressed), and a dict with jet
# index and value the text entered
    print(1, event)
    print(2, values)
    print(3, values['existing todos'])

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo entered'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['existing todos'].update(values=todos)
        case "Edit":
            todo_to_edit = values['existing todos'][0]
            new_todo = values['todo entered']

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)

            window['existing todos'].update(values=todos)
            # to have the edited version show in GUI automatically

        case "Complete":
            todo_to_complete = values["existing todos"][0]
            todos = functions.get_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window["existing todos"].update(values=todos)
            window["todo entered"].update(value="")

        case "Exit":
            break
        case 'existing todos':
            window['todo entered'].update(value=values['existing todos'][0])

        case sg.WIN_CLOSED:
            break


window.close()
