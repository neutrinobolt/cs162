"""Main driver file for yet-to-be-named game."""

from class_lib import Window as cl

def open_win(op_root: cl):
    """Display start window"""
    
    op_root.label("Insert game here...", 0, 0)
    op_root.button("Click here to start!", lambda: file_win(op_root), 0, 1)
    op_root.mainloop()


def file_win(root: cl):
    """Display file window"""
    file_list = [0,0,0]
    root.label("Select a file!", 0, 0)
    file_col = 0
    for file in file_list:
        file_col += 1
        if file is True:
            pass
        else:
            root.label("Empty File", 1, file_col)
            root.button("Create new file", create_win, 0, file_col)

def create_win():
    pass

def main():

    #Opening window
    file_select = cl()
    open_win(file_select)
    

if __name__ == "__main__":
    main()