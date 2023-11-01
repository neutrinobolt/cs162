"""Create window class to contain 1 label, 10 entries, and 1 button.

    Entries will only accept integer input.

    Button, when pressed, will first collect all entries and put them in a list.
    It will then display the lowest-number integer out of the list in the label.
    if that item is already being displayed, then the next lowest entry will be displayed, 
    and continue until all entries have been displayed.

    I came very close to getting this to work as intended. New values can be entered
    anywhere and the title will change to relfect that. However, if more than one
    instance of the same integer is present, it will only change to that number once,
    and not repeat that number for each instance of it. I've tried my darndest to 
    get it to work, but I'm already two weeks late in turning in this assignment. 
    """

import tkinter as tk

class NumDisplay:
    """Creates a window for displaying and manipulating numbers."""
    def __init__(self):

        self.root = tk.Tk()

        #Create display label
        self.num_title = tk.Label(self.root,
                                  text="Please enter integers into the boxes.")

        self.num_title.pack()

        #Create ten entry boxes
        self.entry_boxes = []
        self.entries = []
        self.current_index = 0

        for step in range(10):
            self.entry_box = tk.Entry(self.root, )
            self.entry_box.insert(0, f"{10 - step}")
            self.entry_box.pack()
            self.entry_boxes.append(self.entry_box)
            self.entries.append(self.entry_box.get())

        #debug
        #for value in self.entries:
         #   self.entry_value = value.get() #Intellisense doesn't highlight get, but it still works
          #  print(self.entry_value)

        #Create button
        def set_display ():
            """Function to be called upon pressing the setter button."""
            #task 2: display numbers in order

            #check if list has been changed
            test_list = []
            for value in self.entry_boxes:
                current_value = value.get()
                #print(current_value) #debug
                test_list.append(current_value)

            if test_list != self.entries:
                #if change has occurred, reset display loop
                self.entries = test_list
                self.num_title["text"] = "resetting..."
                print("Change occurred. resetting loop.")#debug
                print(f"self.entries = {self.entries}")

            try:
                int(self.num_title["text"])
            except ValueError:

                #Task 1: display smallest value in label
                #print(f"title {self.num_title} is not an integer.") #debug
                label_target = int(self.entries[0])
                for item, index in enumerate(self.entries):
                    item = int(index)
                    if item <= label_target:
                        label_target = item
                        self.current_index = index
                self.num_title["text"] = label_target
                print(self.current_index) #debug
            else:
                #replace displayed value with next highest value, includes repeated numbers
                #print(f"title {self.num_title} is an integer") #debug
                label_target = int(self.entries[0]) #starting check value
                current_label = int(self.num_title["text"]) #int of title for validation
                potential_index = 0
                for index, entry in enumerate(self.entries):

                    #debug, test values
                    print("New step") #debug
                    print(f"index {index}")
                    print(f"entry {entry}")
                    print(f"current label {current_label}")
                    print(f"label target {label_target}")
                    print(f"current index {self.current_index}")

                    entry_usable = int(entry)
                    #print(entry_usable) #debug
                    if entry_usable == int(current_label) and index > potential_index + 1:
                        label_target = entry
                        print(f" new label target {label_target}") #debug
                        potential_index = index
                    elif entry_usable > int(current_label) and  entry_usable <= label_target:
                        label_target = entry_usable
                        print(f"new label target {label_target}")
                        potential_index = index
                    else: #debug
                        print("No change made")
                    potential_index = index
                self.current_index = potential_index
                self.num_title["text"] = label_target
                print(self.current_index)

        self.disp_setter = tk.Button(self.root,
                                     text= "Press to update label.",
                                     command=set_display)
        self.disp_setter.pack()

    #Create button function


    def mainloop(self):

        self.root.mainloop()
