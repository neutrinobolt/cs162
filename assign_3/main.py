"""Main driver file for yet-to-be-named game."""

import gui_lib as gl

def main():

    #Opening window
    start = gl.Start()
    file_select = gl.FileList()
    file_select.file_window.root.withdraw()
    new_file = gl.NewFile()
    start.pair_class(file_select)
    start.start_window.mainloop()


if __name__ == "__main__":
    main()