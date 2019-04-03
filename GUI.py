#!/usr/bin/env python
#-*- coding: utf-8 -*-

# 600 480
import tkinter
import math
from dots import DotsBoxesBoard,PLAYER1,PLAYER2
import numpy as np
import math
import Point
MAXSIZE = 20
B_SIZE= 30

class Chess_Board_Canvas(tkinter.Canvas):
    def __init__(self, master, height, width, board):

        tkinter.Canvas.__init__(self, master, height=(height+1)*B_SIZE, width=(width+1)*B_SIZE+30)
        self.height = height
        self.width = width
        self.board = board
        self.init_chess_board_points()    #画点
        self.init_chess_board_canvas()    #绘制棋盘

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

        if self.board.checkline(min1,min2) and  dis<= 600:
            self.create_line(self.chess_board_points[int(min1[0])][int(min1[1])].pixel_x, self.chess_board_points[int(min1[0])][int(min1[1])].pixel_y,
                         self.chess_board_points[int(min2[0])][int(min2[1])].pixel_x, self.chess_board_points[int(min2[0])][int(min2[1])].pixel_y,width = 2)
            self.board.drawline(min1,min2)
            x,y = self.board.findfill()
            if x != -1:
                if self.board.currentplayer == PLAYER1:
                    self.create_rectangle(self.chess_board_points[x][y].pixel_x, self.chess_board_points[x][y].pixel_y,
                                      self.chess_board_points[x+1][y+1].pixel_x,
                                      self.chess_board_points[x+1][y+1].pixel_y,fill='red')
                elif self.board.currentplayer == PLAYER2:
                    self.create_rectangle(self.chess_board_points[x][y].pixel_x, self.chess_board_points[x][y].pixel_y,
                                          self.chess_board_points[x + 1][y + 1].pixel_x,
                                          self.chess_board_points[x + 1][y + 1].pixel_y, fill='blue')
            else:
                self.board.switchplayer()
        # if self.board.currentplayer == PLAYER2:
        #     self.board.genmove()

class Chess_Board_Frame(tkinter.Frame):
    def __init__(self, master=None):
        tkinter.Frame.__init__(self, master)
        # self.create_widgets()

    def create_widgets(self,height,width):
        board = DotsBoxesBoard(width,height)
        self.chess_board_label_frame = tkinter.LabelFrame(self, text="Chess Board", padx=5, pady=5)
        self.chess_board_canvas = Chess_Board_Canvas(self.chess_board_label_frame, height, width, board)

        self.chess_board_canvas.bind('<Button-1>', self.chess_board_canvas.click1)

        self.chess_board_label_frame.pack()
        self.chess_board_canvas.pack()
