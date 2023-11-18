
import random

def item_swap(in_list: list, index_a: int, index_b: int):
    """Swaps positions of two items within a list."""
    in_list[index_a], in_list[index_b] = in_list[index_b], in_list[index_a]

def list_sort(in_list: list):
    """sorts list from smallest to largest value."""

    #Get candidate value
    for cand_index, cand_value in enumerate(in_list):

        #find smallest value to right of candidate
        swap_index = cand_index
        swap_value = cand_value
        for check_index, check_value in enumerate(in_list):

            if check_index > swap_index and check_value < swap_value:
                swap_index = check_index
                swap_value = check_value
            
        item_swap(in_list, cand_index, swap_index)
            


test_list  = []

for i in range(10):
    test_list.append(random.randint(1, 10))

print(test_list)
list_sort(test_list)
print(test_list)