"""Main driver file for yet-to-be-named game."""

from class_lib import Window as cl

def main():

    #Opening window
    file_select = cl()
    file_select.file_win()
    file_select.mainloop()
    

if __name__ == "__main__":
    main()