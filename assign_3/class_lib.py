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

    def open_win(self):
        """Display start window"""
    
        self.label("Insert game here...", 0, 0)
        self.button("Click here to start!", self.file_win, 0, 1)
        self.mainloop()

    
    def file_win(self):
        """Display file window"""
        self.file_list = [0,0,0]
        self.label("Select a file!", 0, 0)
        self.file_col = 0
        for file in self.file_list:
            self.file_col += 1
            if file is True:
                pass
            else:
                self.label("Empty File", 1, self.file_col)
                self.button("Create new file", self.create_win, 0, self.file_col)

    def create_win():
        pass

    

        
    
