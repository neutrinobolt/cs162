import tkinter
import rect_search as rs


def test_random_min():
    """Checks that lower bound of shapes is indeed 1."""

    #create lists to hold max and min lengths for 20 individual windows
    
    total_min_vals = []

    #Set expected max and min
    expected_min_length = 1

    for window in range(20):
        #create 20 windows, get smallest and largest lengths from each
        test_min_window = rs.SearchWindow()

        min_rect = 10

        for rect_length in test_min_window.rect_lengths:
            #find smallest and largest values
            if rect_length < min_rect:
                min_rect = rect_length
            
            #add them to big lists
            
            total_min_vals.append(min_rect)
    
    #find overall min and max lengths
    overall_min_val = 10
    

    for min_val in total_min_vals:
        if min_val < overall_min_val:
            overall_min_val = min_val

    #assert correct lengths

    assert overall_min_val == expected_min_length

def test_random_max():
    
    total_max_vals = []

    expected_max_length = 20
    
    for window in range(20):

        test_max_window = rs.SearchWindow()
        max_rect = 10

        for rect_length in test_max_window.rect_lengths:

            if rect_length > max_rect:
                max_rect = rect_length
            
            total_max_vals.append(max_rect)
    
    overall_max_val = 10

    for max_val in total_max_vals:
        if max_val > overall_max_val:
            overall_max_val = max_val
    
    assert overall_max_val == expected_max_length