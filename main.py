import GUI
import tkinter as tk
from dots import PLAYER1,PLAYER2

class quitButton(tk.Button):
    def __init__(self, parent):
        tk.Button.__init__(self, parent)
        self['text'] = 'Good Bye'
        # Command to close the window (the destory method)
        self['command'] = parent.destroy
        self.pack()


LARGE_FONT = ("Verdana", 12)

class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage,Chess_Board_Frame):
            if F == Chess_Board_Frame:
                frame = F(container, self,4,3)
            else:
                frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class Chess_Board_Frame(tk.Frame):
    def __init__(self,parent, controller,height=5,width=6):
        tk.Frame.__init__(self, parent)
        board = GUI.DotsBoxesBoard(width,height)
        self.chess_board_label_frame = tk.Label(self, text="Chess Board")
        self.chess_board_label_frame.pack(pady=10, padx=10)

        self.chess_board_canvas = GUI.Chess_Board_Canvas(self.chess_board_label_frame, height, width, board)
        self.chess_board_canvas.bind('<Button-1>', self.chess_board_canvas.click1)
        self.chess_board_label_frame.pack()
        self.chess_board_canvas.pack()
        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Dots and boxes", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        # button = tk.Button(self, text="player vs player",
        #                    command=lambda: controller.show_frame(Chess_Board_Frame))
        # button.pack()

        button2 = tk.Button(self, text="player vs computer",
                            command=lambda: controller.show_frame(Chess_Board_Frame))
        button2.pack()


# class PageOne(tk.Frame):
#
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
#         label.pack(pady=10, padx=10)
#
#         button1 = tk.Button(self, text="Back to Home",
#                             command=lambda: controller.show_frame(StartPage))
#         button1.pack()
#
#         button2 = tk.Button(self, text="Page Two",
#                             command=lambda: controller.show_frame(PageTwo))
#         button2.pack()
#
#
# class PageTwo(tk.Frame):
#
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         label = tk.Label(self, text="Page Two!!!", font=LARGE_FONT)
#         label.pack(pady=10, padx=10)
#
#         button1 = tk.Button(self, text="Back to Home",
#                             command=lambda: controller.show_frame(StartPage))
#         button1.pack()
#
#         button2 = tk.Button(self, text="Page One",
#                             command=lambda: controller.show_frame(PageOne))
#         button2.pack()



if __name__ == '__main__':
    app = SeaofBTCapp()
    quitButton(app)
    app.mainloop()
    #
    # gui_chess_board = GUI.Chess_Board_Frame(window)
    # # gui_chess_board.create_widgets(7,10)
    # # tkinter.Canvas.delete(gui_chess_board.chess_board_canvas)
    # gui_chess_board.create_widgets(5,6)
    #
    # gui_chess_board.pack()
    #
    # window.mainloop()