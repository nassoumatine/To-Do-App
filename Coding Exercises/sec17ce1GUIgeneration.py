import FreeSimpleGUI as sg

feet_label = sg.Text("Enter feet:")
feet_input = sg.Input()

inches_label = sg.Text("Enter inches:")
inches_input = sg.Input()

convertion_button = sg.Button("Convert")

window = sg.Window("Convertor", layout=[[feet_label, feet_input],
                                        [inches_label, inches_input],
                                        [convertion_button]])

window.read()
window.close()

# Another GUI
label = sg.Text("What are dolphins?")
option1 = sg.Radio("Amphibians", group_id="question1")  # .Radio helps to chose one option from many.
option2 = sg.Radio("Fish", group_id="question1")
option3 = sg.Radio("Mammals", group_id="question1")
option4 = sg.Radio("Birds", group_id="question1")

window = sg.Window("File Compressor",
                   layout=[[label],
                           [option1],
                           [option2],
                           [option3],
                           [option4],
                           ])

window.read()
window.close()
