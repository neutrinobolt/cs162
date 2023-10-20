"""Class library containing GUI materials."""

import tkinter as tk

class Gui_Window:
    """Base window class containing methods and attributes all guis will need."""

    def __init__(self):
        """initialize window"""
        self.root = tk.Tk()
        self.root.geometry("800x600")

    

    def mainloop (self):
        self.root.mainloop()

class Start:
    """Window class generates a Start screen.
    """

    def __init__(self):
        
        self.start_window = Gui_Window()


        self.title = tk.Label(self.start_window.root, text = "Insert game here...")
        self.title.grid(column= 0, row= 0)
        self.start = tk.Button(self.start_window.root,
                            text = "Click here to start!",
                            command = self.activate_partner)
        self.start.grid(column= 0, row =0)

    def pair_class(self, partner_class: Gui_Window):
        self.partner_class = partner_class

    def activate_partner (self):
        """close running window, open partner"""

        self.partner_class.root.deiconify()
        self.start_window.root.withdraw()

    #def activate_partner (self):
     #   """close running window, open partner"""
#
 #      self.partner.deiconify()
  #      self.root.withdraw()
        
    #def mainloop(self):
     #   self.root.mainloop()

    #def label (self, label, column, row):
     #   label = tk.Label(self.root, text = label)
      #  label.grid(column= column, row= row)
#
 #   def entry (self, width, def_text, col, row):
  #      entry = tk.Entry(self.root, width = width)
   #     entry.insert(0, def_text)
    #    entry.grid(column= col, row= row)
#
 #   def button (self, but_text, com_func, col, row):
  #      button = tk.Button(self.root, text = but_text, command = com_func)
   #     button.grid(column= col, row= row)
#
    
    
    #def file_win(self):
     #   """Display file window"""
      #  self.file_list = [0,0,0]
       # self.label("Select a file!", 0, 0)
        #self.file_col = 0
        #for file in self.file_list:
         #   self.file_col += 1
          #  if file is True:
           #     pass
            #else:
             #   self.label("Empty File", 1, self.file_col)
              #  self.button("Create new file", self.create_win, 0, self.file_col)
#
 #   def create_win():
  #      pass

class FileList:
    """Creates object class for file windows. """

    def __init__(self):
         
        self.file_window = Gui_Window()

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
                file_name.grid(column= 0, row= self.file_row)
                

        file_create = tk.Button(self.file_window.root,
                                text= "Create new file",
                                command= self.activate_partner)
        file_create.grid(column=1, row= 4)

    def pair_class(self, partner_class: Gui_Window):
        """Connect a secondary gui_window to this window"""
        self.partner_class = partner_class

    def activate_partner (self):
        """close running window, open partner"""

        self.partner_class.root.deiconify()
        self.file_window.root.withdraw()

class NewFile:
     
    pass
