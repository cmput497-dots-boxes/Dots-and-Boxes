MAXSIZE = 8
PLAYER1 = 1
PLAYER2 = 2
EMPTY = 0
import numpy as np



class DotsBoxesBoard(object):
    def __init__(self, width,length):

        # Creates a Dots Boxes Board of given size

        assert 2 <= width <= MAXSIZE

        assert 2 <= length <= MAXSIZE
        self.reset(width,length)

    def reset(self, width, length):

        self.width = width
        self.length = length
        self.currentplayer = PLAYER1
        self.maxpoint = width*(length+1)+(width+1)*length

        self.rows = np.full(width*(length+1), EMPTY, dtype = np.int32)
        self.columns = np.full((width+1)*length, EMPTY, dtype = np.int32)
        self.blocks = np.full(width*length, EMPTY, dtype = np.int32)



