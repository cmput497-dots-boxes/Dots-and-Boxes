#!/usr/bin/env python
#-*- coding: utf-8 -*-

# 600 480
import tkinter
from tkinter import *
import math
from dots import DotsBoxesBoard,PLAYER1,PLAYER2,EMPTY
import numpy as np
import math
import Point
MAXSIZE = 20
B_SIZE= 30
PLAYER = 1
CMPUT = 2
LARGE_FONT = ("Verdana", 12)

class Chess_Board_Canvas(tkinter.Canvas):
    def __init__(self, master, height, width, board,use_ai=False):

        tkinter.Canvas.__init__(self, master, height=(height+1)*B_SIZE, width=(width+1)*B_SIZE+30)
        self.master = master
        self.height = height
        self.width = width
        self.board = board
        self.init_chess_board_points()    #画点
        self.init_chess_board_canvas()    #绘制棋盘
        self.ai_option = use_ai
        self.canvas = tkinter.Canvas

    def init_chess_board_points(self):
        self.chess_board_points = [[None for i in range(MAXSIZE)] for j in range(MAXSIZE)]
        #
        for i in range(self.width):
            for j in range(self.height):
                self.chess_board_points[i][j] = Point.Point(i, j)

    def init_chess_board_canvas(self):
        '''
        初始化棋盘
        :return:
        '''


        for i in range(self.width):
            for j in range(self.height):
                r = 2
                self.create_oval(self.chess_board_points[i][j].pixel_x-r, self.chess_board_points[i][j].pixel_y-r, self.chess_board_points[i][j].pixel_x+r, self.chess_board_points[i][j].pixel_y+r, fill='black')
    def draw_rect(self,x,y,player):
        if x != -1:
            if self.board.currentplayer == PLAYER1:
                self.create_rectangle(self.chess_board_points[x][y].pixel_x, self.chess_board_points[x][y].pixel_y,
                                      self.chess_board_points[x + 1][y + 1].pixel_x,
                                      self.chess_board_points[x + 1][y + 1].pixel_y, fill='red')
            elif self.board.currentplayer == PLAYER2:
                self.create_rectangle(self.chess_board_points[x][y].pixel_x, self.chess_board_points[x][y].pixel_y,
                                      self.chess_board_points[x + 1][y + 1].pixel_x,
                                      self.chess_board_points[x + 1][y + 1].pixel_y, fill='blue')
            x, y = self.board.findfill()
            if x != -1:
                self.draw_rect(x,y,PLAYER)
        else:
            self.board.switchplayer()

    def ai_move(self):
        if self.board.currentplayer == PLAYER2:
            x, y = self.board.aimove()
            if x == -1:
                return
            x, y = self.draw_line(x, y)
            self.draw_rect(x, y, CMPUT)
            self.ai_move()
        else:
            return

            # self.draw_rect(x, y)
    def draw_line(self,min1,min2):
        self.create_line(self.chess_board_points[int(min1[0])][int(min1[1])].pixel_x,
                         self.chess_board_points[int(min1[0])][int(min1[1])].pixel_y,
                         self.chess_board_points[int(min2[0])][int(min2[1])].pixel_x,
                         self.chess_board_points[int(min2[0])][int(min2[1])].pixel_y, width=2)
        self.board.drawline(min1, min2)
        x, y = self.board.findfill()
        return x,y
    def click1(self, event):
        '''
        侦听鼠标事件,根据鼠标的位置判断落点
        :param event:
        :return:
        '''
        distances = np.zeros((self.width,self.height))
        for i in range(self.width):
            for j in range(self.height):
                distances[i][j] = math.pow((event.x - self.chess_board_points[i][j].pixel_x), 2) + math.pow((event.y - self.chess_board_points[i][j].pixel_y), 2)
        min1 = np.unravel_index(distances.argmin(), distances.shape)
        dis = distances[min1[0],min1[1]]
        distances[min1[0],min1[1]] = math.inf
        min2 = np.unravel_index(distances.argmin(), distances.shape)
        dis = dis + distances[min2[0],min2[1]]
        # print(min1)
        if self.board.checkline(min1,min2) and  dis<= 600:
            x,y = self.draw_line(min1,min2)
            self.draw_rect(x,y,PLAYER)
            self.ai_move()
        if len(self.board.gen_legal_move()) == 0:
            root = tkinter.Tk()
            T = Text(root, height=5, width=30)
            T.pack()
            _,winner = self.board.check_winner()
            print(winner)
            if winner == PLAYER2:
                T.insert(END, "Computer wins")
            elif winner == PLAYER1:
                T.insert(END, "Congratulations, you win")
            elif winner == EMPTY:
                T.insert(END, "draw game")
            else:
                T.insert(END, "unknown result")



            # if self.board.currentplayer == PLAYER2:
        #     self.board.genmove()


    def clear_board(self):
        tkinter.Canvas.delete(self.b)



    # def __init__(self, parent, controller):
    #     tk.Frame.__init__(self, parent)
    #     label = tk.Label(self, text="Start Page", font=LARGE_FONT)
    #     label.pack(pady=10, padx=10)
    #
    #     button = tk.Button(self, text="player vs player",
    #                        command=lambda: controller.show_frame(GUI.Chess_Board_Frame))
    #     button.pack()
    #
    #     button2 = tk.Button(self, text="Visit Page 2",
    #                         command=lambda: controller.show_frame(PageTwo))
    #     button2.pack()