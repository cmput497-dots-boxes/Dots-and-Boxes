import numpy as np


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


class DotsBoxesBoard(object):
    def __init__(self, width,height):

        # Creates a Dots Boxes Board of given size

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
        self.blocks = np.zeros((width-1,height-1,5))
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
        if np.sum(self.blocks[x][y] == 0) == 1:

            self.blocks[x][y][COLORED] = FILL

    def switchplayer(self):
        self.currentplayer = 5 - self.currentplayer


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
