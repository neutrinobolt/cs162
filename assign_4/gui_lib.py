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

        self.start_window.root.destroy()

    def window_connect(self, partner_window: GuiWindow):
        """Pair Start window to following window."""
        self.partner_class = partner_window

    def activate_partner (self):
        """close running window, open partner"""
        if self.partner_class is not None:
            self.partner_class.root.deiconify()
            self.start_window.root.withdraw()

class FileList:
    """Creates object class for file windows. """

    def __init__(self):

        self.file_window = GuiWindow()
        self.creator_window = None
        self.start_window = None
        self.file_window.root.protocol("WM_DELETE_WINDOW", self.window_cleaner)

        self.title = tk.Label(self.file_window.root, text = "Select a file:")
        self.title.grid(column= 0, row=0)

        self.file_one = tk.Label(self.file_window.root, text = "Empty file")
        self.file_one.grid (column= 1, row= 1)

        self.file_two = tk.Label(self.file_window.root, text = "Empty file")
        self.file_two.grid (column= 1, row= 2)

        self.file_three = tk.Label(self.file_window.root, text = "Empty file")
        self.file_three.grid (column= 1, row= 3)

        self.file_create = tk.Button(self.file_window.root,
                                text= "Create new file",
                                command= self.activate_creator)
        self.file_create.grid(column= 0, row= 4)

    def start_connect(self, partner_class: GuiWindow):
        """Connect the start window to this window"""
        self.start_window = partner_class

    def creator_connect(self, partner_class: GuiWindow):
        """Connect the file creator window to this window"""
        self.creator_window = partner_class

    def activate_creator (self):
        """close running window, open partner"""
        if self.creator_window is not None:
            self.creator_window.root.deiconify()
            self.file_window.root.withdraw()

    def window_cleaner(self):
        """Deletes this and paired windows"""
        print("cleaning windows...")
        if self.creator_window is not None:
            self.creator_window.root.destroy()
            print("creator window destroyed successfully")
        if self.start_window is not None:
            self.start_window.root.destroy()
            print("Start window destroyed successfully")

        self.file_window.root.destroy()
        print("File window destroyed successfully")

class NewFile:
     
    def __init__(self):
        self.creator_window = GuiWindow()
        self.file_window = None

        #Create name entry button
        self.name_entry = tk.Entry(self.creator_window.root, width= 20)
        self.name_entry.insert(0, "file name here...")
        self.name_entry.grid(column=0, row= 0)

        def file_rename_one (name: str):
            """rename the desired file to the input name"""
            self.file_window.file_one["text"] = name
            self.creator_window.root.withdraw()
            if self.file_window is not None:
                self.file_window.file_window.root.deiconify()

        def file_rename_two (name: str):
            """rename the desired file to the input name"""
            self.file_window.file_two["text"] = name
            self.creator_window.root.withdraw()
            if self.file_window is not None:
                self.file_window.file_window.root.deiconify()

        def file_rename_three (name: str):
            """rename the desired file to the input name"""
            self.file_window.file_three["text"] = name
            self.creator_window.root.withdraw()
            if self.file_window is not None:
                self.file_window.file_window.root.deiconify()

        #Create three file buttons
        self.file_one_button = tk.Button(self.creator_window.root,
                                         text = "Overwrite File 1",
                                         command= lambda: file_rename_one(self.name_entry.get()))
        self.file_one_button.grid(column= 0, row= 1)

        self.file_two_button = tk.Button(self.creator_window.root,
                                         text = "Overwrite File 2",
                                         command= lambda: file_rename_two(self.name_entry.get()))
        self.file_two_button.grid(column= 0, row= 2)

        self.file_three_button = tk.Button(self.creator_window.root,
                                         text = "Overwrite File 3",
                                         command= lambda: file_rename_three(self.name_entry.get()))
        self.file_three_button.grid(column= 0, row= 3)

        
    
    def filewin_connect (self, file_window: FileList):
        """Connect to the File window"""
        self.file_window = file_window
        
    


