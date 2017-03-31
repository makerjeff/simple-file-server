import Tkinter
from Tkinter import *
from tkFileDialog import *


root = Tkinter.Tk()
file_loaded = None
file_data = None

# Open a file Dialog ---------------
def browse():
    global file_loaded
    global file_data
    print 'Browsing something. '
    file_loaded = askopenfilename(parent=root)

    with open(file_loaded, 'rb') as f:
        file_data = f.read()
    # print file_data

# Read the file ----------------
def read_binary():
    print file_data


# Main Loop ----------------
def Main():
    root.title('Video Viewer')

    label = Tkinter.Label(root, text='This program reads a text file.')
    label.pack()

    browse_button = Tkinter.Button(root, text='Browser', command=browse)
    browse_button.pack()

    something_else_button = Tkinter.Button(root, text='Print Data', command=read_binary)
    something_else_button.pack()

    root.mainloop()

# Module Gobbly Gook ---------------
if __name__ == '__main__':
    Main()