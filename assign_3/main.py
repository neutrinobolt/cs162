"""Main driver file for yet-to-be-named game."""

from class_lib import Window as cl

def open_win():
    """Display start window"""
    start_win = cl()
    start_win.label("Insert game here...", 0, 0)
    start_win.button("Click here to start!", file_win, 0, 1)
    start_win.mainloop()


def file_win():
    """Display file window"""
    pass

def main():

    #Opening window
    open_win()
    

if __name__ == "__main__":
    main()