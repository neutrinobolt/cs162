"""Class file to hold class initializarion for sorting function"""

import tkinter as tk

class SortGui:
    """Create a tkinter window containing a canvas containing random rectangles
    and a button that will sort the rectangles."""

    def __init__(self,
                 rect_lengths: list[int],
                 sort_func,
                 unchecked = "white",
                 checking = "blue",
                 unmatched = "red",
                 matched = "green"):

            #initialize given variables
        self.rect_lengths = rect_lengths
        self.unchecked = unchecked
        self.checking = checking
        self.unmatched = unmatched
        self.matched = matched

        #define sorting algorithm
        #def rect_sort():
          #  """Sort rectangles, with pauses at each step."""
            

        #setup window
        self.root = tk.Tk()

        self.rect_box = tk.Canvas(self.root, height=400, width= 600)
        self.rect_box.grid(column= 0, row= 0)

        #test
        #self.rect_box.create_rectangle(x0=10,y0=10,x1=20,y1=20, fill="red")

        #put rectangles in rectbox

        self.rect_indices = []

        self.roof_buffer = 10
        self.left_buffer = 10
        self.width = 10

        for index, length in enumerate(self.rect_lengths):
            x0 = index * 15 + self.left_buffer
            disp_length = length * 5
            rectangle = self.rect_box.create_rectangle(x0,
                                           self.roof_buffer,
                                           x0 + self.width,
                                           self.roof_buffer + disp_length,
                                           fill=self.unchecked)
            self.rect_indices.append(rectangle)
        #print(self.rect_lengths) #debug

        self.sort_button = tk.Button(self.root,
                                        text="sort rectangles",
                                        command= sort_func)
        
        self.sort_button.grid(column=0,
                                row=1)
        
        #Create a success label that will not be shown until after the sort is done

        self.success = tk.Label(self.root, 
                                text="Great job... *burp*... I'm proud, or something...")

    def update_rectangle(self, rect_ind, new_length = None, new_color = None):
        """Changes size and color of given rectangle in canvas"""
        #Get desired coords. Only y1 should change, the rest 
        rect_coords = self.rect_box.coords(rect_ind)
        x0 = rect_coords[0]
        y0 = rect_coords[1]
        x1 = rect_coords[2]
        y1 = self.roof_buffer + new_length * 5

        if new_length is not None:
            self.rect_box.coords(rect_ind, x0, y0, x1, y1)
        if new_color is not None:
            self.rect_box.itemconfig(rect_ind, fill= new_color)


    def mainloop(self):
        self.root.mainloop()
