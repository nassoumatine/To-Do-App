# This app is a GUI that compresses files and puts them in a folder

import FreeSimpleGUI as sq

label1 = sq.Text("Select files to compress:")
input1 = sq.Input()
choose_button1 = sq.FilesBrowse("Choose")

label2 = sq.Text("Select destination folder:")
input2 = sq.Input()
choose_button2 = sq.FolderBrowse("Choose")

compress_button = sq.Button("Compress")

window = sq.Window("File Compressor", layout=[[label1, input1, choose_button1],
                                              [label2, input2, choose_button2],
                                              [compress_button]])

while True:
    event, values = window.read()
    pass

window.read()
window.close()
