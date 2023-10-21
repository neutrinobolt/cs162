"""Class library containing GUI materials."""

import tkinter as tk

class GuiWindow:
    """Base window class containing methods and attributes all guis will need."""

    def __init__(self):
        """initialize window"""
        self.root = tk.Tk()
        self.root.geometry("800x600")
        self.partner_class = None

    def mainloop (self):
        self.root.mainloop()

class Start:
    """Window class generates a Start screen.
    """

    def __init__(self):
        
        self.start_window = GuiWindow()
        self.start_window.root.protocol("WM_DELETE_WINDOW", self.window_cleaner)

        self.partner_class = None


        self.title = tk.Label(self.start_window.root, text = "Insert game here...")
        self.title.pack()
        self.start = tk.Button(self.start_window.root,
                            text = "Click here to start!",
                            command = self.activate_partner)
        self.start.pack()

    def window_cleaner(self):
        """Deletes this and paired windows"""
        if self.partner_class is not None:
            self.partner_class.root.destroy()

        self.start_window.root.destroy()

    def window_connect(self, partner_window: GuiWindow):
        """Pair Start window to following window."""
        self.partner_class = partner_window

    def activate_partner (self):
        """close running window, open partner"""
        if self.partner_class is not None:
            self.partner_class.root.deiconify()
            self.start_window.root.withdraw()

    def __del__(self):
        del self.partner_class
        del self

class FileList:
    """Creates object class for file windows. """

    def __init__(self):

        self.file_window = GuiWindow()
        self.partner_class = None
        self.file_window.root.protocol("WM_DELETE_WINDOW", self.window_cleaner)

        self.title = tk.Label(self.file_window.root, text = "Select a file:")
        self.title.grid(column= 0, row=1)

        self.file_list = [0,0,0]
        self.file_row = 0

        for file in self.file_list:
            self.file_row +=1
            if file is True:
                pass
            else:
                file_name = tk.Label(self.file_window.root, text = "Empty File")
                file_name.grid(column= 1, row= self.file_row + 1)

        file_create = tk.Button(self.file_window.root,
                                text= "Create new file",
                                command= self.activate_partner)
        file_create.grid(column= 0, row= 5)

    def window_connect(self, partner_class: GuiWindow):
        """Connect a secondary gui_window to this window"""
        self.partner_class = partner_class

    def activate_partner (self):
        """close running window, open partner"""
        if self.partner_class is not None:
            self.partner_class.root.deiconify()
            self.file_window.root.withdraw()

    def window_cleaner(self):
        """Deletes this and paired windows"""
        print("cleaning windows...")
        if self.partner_class is not None:
            self.partner_class.root.destroy()
            print("Partner class destroyed successfully")

        self.file_window.root.destroy()
        print("File window destroyed successfully")

class NewFile:
     
    pass
