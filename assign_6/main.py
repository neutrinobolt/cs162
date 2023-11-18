"""Main driver for assignment."""

import random
import sort_gui as sg
import time

DELAY = .25

def item_swap(in_list: list, index_a: int, index_b: int):
    """Swaps positions of two items within a list."""
    in_list[index_a], in_list[index_b] = in_list[index_b], in_list[index_a]

def selection_sort(rect_lengths: list,
                    canv_window: sg.SortGui):
    """Performs a selection sort on the given rectangle list, 
    then displays properly."""

    #Identify index to sort

    for cand_index, cand_length in enumerate(rect_lengths):

        canv_window.rect_box.itemconfig(cand_index + 1, fill= canv_window.checking)
        canv_window.rect_box.update()
        time.sleep(DELAY)

        swap_index = cand_index
        swap_length = cand_length
        
        for check_index, check_length in enumerate(rect_lengths):
            #find smallest value in remaining list, swap locations, update
            if check_index > swap_index and check_length < swap_length:
                swap_index = check_index
                swap_length = check_length
        #print(swap_length) #debug
        canv_window.rect_box.itemconfig(swap_index + 1,
                                        fill = canv_window.checking)
        canv_window.rect_box.update()

        
        time.sleep(DELAY)

        
        

        item_swap(rect_lengths, cand_index, swap_index)
        canv_window.update_rectangle(cand_index + 1,
                                     swap_length,
                                     canv_window.matched)
        if cand_index != swap_index:
            canv_window.update_rectangle(swap_index + 1,
                                        cand_length,
                                        canv_window.unchecked)
        #canv_window.root[swap_index], canv_window.root[cand_index] = canv_window.root[cand_index], canv_window.root[swap_index]
        #canv_window.update_box(rect_lengths)
        #canv_window.rect_box.itemconfig(cand_index + 1, fill= canv_window.matched)
        canv_window.rect_box.update()
        time.sleep(DELAY)
    
    canv_window.success.grid(column=0, row=2)
    
    #print(rect_lengths) #debug


def main():
    """run main program. Generate random values for rect lengths, 
    generate gui."""

    #Generate and save info for random rects
    length_list: list[int] = []
    for step in range(20):
        length = random.randint(1, 20)
        length_list.append(length)
    
    #Create window
    rect_sorter = sg.SortGui(rect_lengths=length_list,
                             sort_func= lambda: selection_sort(rect_sorter.rect_lengths,
                                                               canv_window= rect_sorter))
    rect_sorter.mainloop()

if __name__ == "__main__":
    main() 