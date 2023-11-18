"""This is a pytest testing module for the rectangle sorter module."""

import random
import sort_gui as sg
import main
import tkinter as tk

def test_sorter():
    """Tests that selection_sort function from main """

    length_list: list[int] = []
    for step in range(20):
        length = random.randint(1, 20)
        length_list.append(length)

    test_window = sg.SortGui(rect_lengths=length_list,
                             sort_func= lambda: main.selection_sort(test_window.rect_lengths,
                                                                    canv_window= test_window))
    main.DELAY= 0
    main.selection_sort(test_window.rect_lengths,
                        canv_window= test_window)
    test_list = test_window.rect_lengths
    test_debug = 0

    for cand_index, cand_length in enumerate(test_list):
        for check_index, check_length in enumerate(test_list):
            if check_index > cand_index and check_length < cand_length:
                test_debug += 1

    assert test_debug == 0
