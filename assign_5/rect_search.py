"""Ben Snider, CS162, Assignment 5

This file contains a GUI class for use in creating, displaying,
and searching through a list of 20 randomly generated values."""

import tkinter as tk
from tkinter import messagebox
import random
import time

class SearchWindow:
    """Creates a window with three elements: 
    
    1. a canvas containing 20 rectangles of randomly generated lengths.
    2. an entry box for inputting a rectangle size to search for
    3. A button that runs a search function, highlighting all rectangles
    of input value, or raising an error window if an invalid entry is 
    given."""
    def __init__(self):

        #define highlight colors (constants)
        self.unchecked_color = "blue"
        self.matched_color = "green"
        self.unmatched_color = "red"

        #create window
        self.root = tk.Tk()

        #create canvas
        self.canvas = tk.Canvas(self.root, bg= "light grey", width= 450, height= 300)
        self.canvas.grid(column= 0, row= 0)

        #Create 20 rectangles of random length
        self.rectangles = []
        self.rect_lengths = []
        self.inital_x0 = 10
        self.y0 = 10
        self.check_index = 0

        for rectangle_num in range(20):
            x_step = rectangle_num * 20
            x0 = self.inital_x0 + x_step
            x1 = x0 + 10
            rect_length = random.randint(1, 20)
            rect_resize = rect_length  * 10
            y1 = self.y0 + rect_resize

            rectangle = self.canvas.create_rectangle(x0, self.y0, x1, y1,
                                         fill= self.unchecked_color)
            self.rect_lengths.append(rect_length)
            self.rectangles.append(rectangle)

        #print(self.rect_lengths) #debug
        #print(self.rectangles) #debug

        # Create entry box
        self.search_val = tk.Entry(self.root)
        self.search_val.grid(column= 0, row= 1)


        #define search function

        def rectangle_check():
            """Individually search and highlight each rectangle. 

            all rectangles start blue.
            If a non-int entry is given, raise a message box.
            If a rectangle matches the entry, it is highlighted green.
            Else it is highlighted red."""

            print("Searching...") #debug

            #Set all to blue
            for rectangle in self.rectangles:
                self.canvas.itemconfig(rectangle, fill= self.unchecked_color)

            # Check for valid input, clean

            try:
                target_val = int(self.search_val.get())
            except ValueError:
                messagebox.showerror("Invalid input",
                                     "ERROR! Invalid input. please enter a whole number.")
            else:
                # Find and higlight all rectangles of input length green, else red

                for index, rectangle in enumerate(self.rect_lengths):

                    time.sleep(.25)
                    self.root.update()

                    if rectangle == target_val:
                        self.canvas.itemconfig(self.rectangles[index],
                                            fill= self.matched_color)
                    else:
                        self.canvas.itemconfig(self.rectangles[index],
                                                fill= self.unmatched_color)

                print("Done") #debug

        #create search button
        self.search = tk.Button(self.root,
                                text= "Search:",
                                command=rectangle_check)
        self.search.grid(column= 0, row= 2)

    def mainloop(self):
        """Quick function for running generated windows."""
        self.root.mainloop()
        