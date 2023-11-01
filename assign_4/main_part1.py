"""Main driver file for yet-to-be-named game."""

import gui_lib as gl

def main():

    #iterate windows
    start = gl.Start()
    file_select = gl.FileList()
    file_select.file_window.root.withdraw()
    new_file = gl.NewFile()
    new_file.creator_window.root.withdraw()

    #pair windows
    start.window_connect(file_select.file_window)
    file_select.start_connect(start.start_window)
    file_select.creator_connect(new_file.creator_window)
    new_file.filewin_connect(file_select)

    #Start mainloop
    start.start_window.mainloop()


if __name__ == "__main__":
    main()