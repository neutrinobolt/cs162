"""Class library containing GUI materials."""

import tkinter as tk

class Window:
    """Window class generates a window and gives functionalities for basic
    tkinter options.
    """

    def __init__(self) -> None:
        self.root = tk.Tk()
    
    def label (self, label, column, row):
        label = tk.Label(self.root, text = label)
        label.grid(column= column, row= row)

    def entry (self, width, def_text, col, row):
        entry = tk.Entry(self.root, width = width)
        entry.insert(0, def_text)
        entry.grid(column= col, row= row)

    def button (self, but_text, com_func, col, row):
        button = tk.Button(self.root, text = but_text, command = com_func)
        button.grid(column= col, row= row)

    def mainloop(self):
        self.root.mainloop()

    

        
    
