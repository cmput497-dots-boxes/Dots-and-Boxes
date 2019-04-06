import numpy as np
import random

MAXSIZE = 20
PLAYER1 = 2
PLAYER2 = 3
EMPTY = 0
LINE = 1
LEFT = 0
BOTTOM = 1
RIGHT = 2
TOP = 3
COLORED = 4
FILL = 5
UNFILL = 6


class DotsBoxesBoard(object):
    def __init__(self, width,height):

        # Creates a Dots Boxes Board of given size
        print(width)
        assert 2 <= width <= MAXSIZE

        assert 2 <= height <= MAXSIZE
        self.reset(width,height)
        self.fmodel = np.zeros(5)
        self.fmodel[4] = 1

    def reset(self, width, height):

        self.width = width
        self.height = height
        self.currentplayer = PLAYER1
        self.maxpoint = width*(height+1)+(width+1)*height
        #
        # self.rows = np.full(width*(length+1), EMPTY, dtype = np.int32)
        # self.columns = np.full((width+1)*length, EMPTY, dtype = np.int32)
        # self.rows = np.zeros((width-1,height))
        # self.columns = np.zeros(())
        self.init_blocks(width-1,height-1)

    def init_blocks(self,x,y):
        self.blocks = np.zeros((x,y,5))
        for i in range (x):
            for j in range (y):
                self.blocks[i][j][4] = UNFILL
        self.currentplayer = PLAYER1

    def checkline(self,point1,point2):
        if point1[0] == point2[0]:
            if point1[0]>0:
                if self.blocks[point1[0]-1][min(point1[1],point2[1])][RIGHT] == 0:
                    return True
            else:
                if self.blocks[0][min(point1[1],point2[1])][LEFT] == 0:
                    return True
        elif point1[1] == point2[1]:
            if point1[1]>0:
                if self.blocks[min(point1[0],point2[0])][point1[1]-1][BOTTOM] == 0:
                    return True
            else:
                if self.blocks[min(point1[0],point2[0])][0][TOP] == 0:
                    return True
        return False
    def checkfill(self,x,y):
        if np.sum(self.blocks[x][y] == 0) == 0:
            self.blocks[x][y][COLORED] = FILL

    def switchplayer(self):
        self.currentplayer = 5 - self.currentplayer

    def gen_legal_move(self):
        indexes = np.where(self.blocks == EMPTY)
        moves = []
        for i in range(len(indexes[0])):
            temp = [indexes[0][i],indexes[1][i],indexes[2][i]]
            moves.append(temp)
        return moves

    def gen_legal_boxes(self):
        indexes = np.where(self.blocks == EMPTY)
        moves = []
        for i in range(len(indexes[0])):
            temp = [indexes[0][i],indexes[1][i]]
            moves.append(temp)
        return moves

    def move_to_point(self,move):
        if move[2] == 0:
            x = [move[0],move[1]]
            y = [move[0],move[1]+1]
        elif move[2] == 1:
            x = [move[0],move[1]+1]
            y = [move[0]+1,move[1]+1]
        elif move[2] == 2:
            x = [move[0]+1,move[1]+1]
            y = [move[0]+1,move[1]]
        elif move[2] == 3:
            x = [move[0]+1,move[1]]
            y = [move[0],move[1]]
        return x,y


    def aviodtwo(self):
        boxes = self.gen_legal_boxes()
        t_boxes = []
        moves = []

        for i in range(len(boxes)):
            num = boxes.count(boxes[i])
            if num >=3:
                t_boxes.append((boxes[i][0],boxes[i][1]))
        t_boxes = list(dict.fromkeys(t_boxes))
        for i in range(len(t_boxes)):
            indexes = np.where(self.blocks[t_boxes[i][0]][t_boxes[i][1]] == EMPTY)
            for j in range(len(indexes[0])):
                temp = [t_boxes[i][0], t_boxes[i][1], indexes[0][j]]
                moves.append(temp)
            return moves

    def aimove(self):
        moves = self.gen_legal_move()
        if len(moves) == 0:
            return (-1,-1)
        avtmoves = self.aviodtwo()
        move = random.choice(moves)
        if avtmoves:
            move = random.choice(avtmoves)
        x,y = self.move_to_point(move)
        return(x,y)

    def drawline(self,point1,point2):
        if point1[0] == point2[0]:
            if point1[0]>0:
                self.blocks[point1[0] - 1][min(point1[1], point2[1])][RIGHT] = LINE
                self.checkfill(point1[0] - 1,min(point1[1], point2[1]))
            if point1[0]<self.width-1:
                self.blocks[point1[0]][min(point1[1], point2[1])][LEFT] = LINE
                self.checkfill(point1[0],min(point1[1], point2[1]))
        elif point1[1] == point2[1]:
            if point1[1]>0:
                self.blocks[min(point1[0], point2[0])][point1[1] - 1][BOTTOM] =  LINE
                self.checkfill(min(point1[0], point2[0]),point1[1] - 1)
            if point1[1]<self.height-1:
                self.blocks[min(point1[0], point2[0])][point1[1]][TOP] = LINE
                self.checkfill(min(point1[0], point2[0]),point1[1])

    def findfill(self):
        indexes = np.where(self.blocks == FILL)
        if len(indexes[0]) == 0 :
            return -1,-1
        x = indexes[0][0]
        y = indexes[1][0]
        self.blocks[x][y][COLORED] = self.currentplayer
        return x,y
        # print(np.sum(self.blocks == 1))
        # np.where(self.blocks == )

    def genmove(self):
        return
