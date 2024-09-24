# This app is a GUI that compresses files and puts them in a folder

import FreeSimpleGUI as sg
from bonus1617zip_creator import make_archive

label1 = sg.Text("Select files to compress:")
input1 = sg.Input()
choose_button1 = sg.FilesBrowse("Choose", key='files')

label2 = sg.Text("Select files to compress:")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key='folder')

compress_button = sg.Button("Compress")
output_label = sg.Text(key="output", text_color="red")

window = sg.Window("File Compressor", layout=[[label1, input1, choose_button1],
                                              [label2, input2, choose_button2],
                                              [compress_button, output_label]])
while True:
    event, values = window.read()
    print(event, values)
    filepaths = values["files"].split(';')
    folder = values['folder']
    make_archive(filepaths, folder)
    window["output"].update(value="Compression completed!")


window.close()
