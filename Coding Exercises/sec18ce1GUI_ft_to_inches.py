"""
This file is a GUI that converts a height in ft to meters.
"""

import FreeSimpleGUI as sg
from bonus.bonus14converters14 import convert

feet_label = sg.Text("Enter feet: ")
feet = sg.Input(key="feet value")

inches_label = sg.Text("Enter inches: ")
inches = sg.Input(key="inches value")

convert_button = sg.Button("Convert ", key="Convert")

# meters_value =
output_in_meters = sg.Text("", key="output")

window = sg.Window("Convertor", layout=[[[feet_label, feet]],
                                        [[inches_label, inches]],
                                        [convert_button, output_in_meters]],
                   font=("Helvetica", 20))

while True:
    event, values = window.read()

    match event:
        case "Convert":
            feet = float(values["feet value"])
            inches = float(values["inches value"])
            meters = convert(feet, inches)
            window["output"].update(value=f"{meters: .4f} m")

        case sg.WIN_CLOSED:
            break

window.close()
