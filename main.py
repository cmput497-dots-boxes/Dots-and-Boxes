import GUI
import tkinter

if __name__ == '__main__':
    window = tkinter.Tk()
    gui_chess_board = GUI.Chess_Board_Frame(window)
    gui_chess_board.create_widgets(3,4)

    gui_chess_board.pack()
    window.mainloop()