import random
import time


def displaycoord(board, size):
    print("Coordinates")
    for i in range(size*2 - 1):
        if (i % 2 == 0):
            for j in range(size):
                if (j == size-1):
                    print("+")
                else:
                    index = size + size - 1
                    index = (i//2)* index
                    index = index + j
                    if (board[index] == 0):
                        print("+ " + "{:02d}".format(index) + " ",end = "")
                    else:
                        print("+----",end = "")
        else:
            for j in range(size):
                if (j == size-1):
                    index = (i//2) * (size + size - 1)
                    index = index + size - 1
                    index = index + j
                    
                    if (board[index] == 0):
                        print("{:02d}".format(index))
                    else:
                        print("|")
                else:
                    index = (i//2) * (size + size - 1)
                    index = index + size - 1
                    index = index + j
                    
                    if (board[index] == 0):
                        print("{:02d}".format(index) + "   ",end = "")
                    else:
                        print("|    ",end = "") 
    return 0




def displayboard(board, point, size):
    for i in range(size*2 - 1):
        if (i % 2 == 0):
            for j in range(size):
                if (j == size-1):
                    print("+")
                else:
                    index = size + size - 1
                    index = (i//2)* index
                    index = index + j
                    if (board[index] == 0):
                        print("+   ",end = "")
                    else:
                        print("+---",end = "")
        else:
            for j in range(size):
                if (j == size-1):
                    index = (i//2) * (size + size - 1)
                    index = index + size - 1
                    index = index + j
                    if (board[index] == 0):
                        print(" ")
                    else:
                        print("|")
                else:
                    index = (i//2) * (size + size - 1)
                    index = index + size - 1
                    index = index + j
                    ptindex = index - size + 1 - size * (i // 2)
                    
                    if (board[index] == 0):
                        print("    ",end = "")
                    else:
                        print("|",end = "")
                        if (point[ptindex] == 1):
                            print(" a ", end = "")
                        elif (point[ptindex] == 2):
                            print(" b ", end = "")
                        else:
                            print("   ", end = "") 
    return 0




def getcmda(board, point, boardsize, size):
    print("Player A's turn")
    displaycoord(board, size)
    print("\n")
    displayboard(board, point, size)
    invalid = True
    while invalid == True:
        coord = input("Player A: ")
        if (int(coord) > boardsize):
            print("Invalid Move")
            invalid = True
        elif (int(coord) < 0):
            print("Invalid Move")
            invalid = True
        elif (board[int(coord)] == 1):
            print("Invalid Move")
            invalid = True
        else:
            invalid = False
    board[int(coord)] = 1
    q = int(coord) // (size + size - 1)
    r = int(coord) % (size + size - 1)
    '''
    print("remainder is " + str(r))
    print(int(coord)+1)
    print(int(coord)+size)
    print(int(coord)-size+1)
    '''
    return CheckScore(board, point, boardsize, size, coord, r, q, 1)


def getcmdb(board, point, boardsize, size):
    print("Player B's turn")
    displaycoord(board, size)
    print("\n")
    displayboard(board, point, size)
    invalid = True
    while invalid == True:
        coord = input("Player B: ")
        if (int(coord) > boardsize):
            print("Invalid Move")
            invalid = True
        elif (int(coord) < 0):
            print("Invalid Move")
            invalid = True
        elif (board[int(coord)] == 1):
            print("Invalid Move")
            invalid = True
        else:
            invalid = False
    board[int(coord)] = 1
    q = int(coord) // (size + size - 1)
    r = int(coord) % (size + size - 1)
    '''
    print("remainder is " + str(r))
    print(int(coord)+1)
    print(int(coord)+size)
    print(int(coord)-size+1)
    '''
    return CheckScore(board, point, boardsize, size, coord, r, q, 2)





def checkwin(board, point, pointsize, size, ispruning):
    player1 = 0
    player2 = 0
    gameend = True
    prune = (size-1)*(size-1) // 2
    for i in range(pointsize):
        if (point[i] == 0):
            gameend = False
        if (point[i] == 1):
            player1 += 1
        elif (point[i] == 2):
            player2 += 1
    #displayboard(board, point, size)
        if (ispruning == 0):
            if player1 > prune:
                return 1
            if player2 > prune:
                return 2
    if gameend:
        if player1 > player2:
            #print("Player1 win by " + str(player1-player2))
            return 1
        elif player2 > player1:
            #print("Player2 win by " + str(player2-player1))
            return 2
        elif player1 == player2:
            #print("Tie Game!")
            return 0 
    else:
        return -1

def GetAvailable(board, boardsize):
    L = []
    for i in range(boardsize):
        if (board[i] == 0):
            L.append(i)
    return L


def CheckMove(board, point, boardsize, size, coord, r, q, score):
    #print("Current Move: " + str(coord), end = "")
    rest = 0
    if (r == size - 1):
        #print("1 ", end = "")
        if (board[int(coord)+1] == 1 ):
            rest += 1
        if (board[int(coord)+size] == 1):
            rest += 1
        if (board[int(coord)-size+1] == 1):
            rest+= 1
        if (rest < score and point[int(coord) - size + 1 - size * q] == 0):
            #print("A|"+str(rest))
            return 1
                
    elif (r > size - 1 and r != (size + size - 2)):
        #print("2 ", end = "")
        if (board[int(coord)+1] == 1):
            rest += 1
        if (board[int(coord)+size] == 1):
            rest += 1 
        if (board[int(coord)-size+1] == 1):
            rest += 1
        #if (rest < score and point[int(coord) - size + 1 - size * q] == 0):
           # print("B|"+str(rest))
        
        nrest = 0
        #print("3 ", end = "")
        if (board[int(coord)-1] == 1):
            nrest += 1
        if (board[int(coord)+size-1] == 1):
            nrest += 1
        if (board[int(coord)-size] == 1):
            nrest += 1
        #if (nrest < score and point[int(coord)-1 - size + 1 - size * q] == 0):
            #print("C|"+str(nrest))

        if (rest < score and nrest < score):
            return 1
                
    elif (r == (size + size - 2)):
        #print("4 ", end = "")
        if (board[int(coord)-1] == 1):
            rest += 1
        if (board[int(coord)+size-1] == 1):
            rest += 1
        if (board[int(coord)-size] == 1):
            rest += 1
        if (rest < score and point[int(coord)-1 - size + 1 - size * q] == 0):
            #print("D|"+str(rest))
            return 1

    rest = 0
    if (q == 0 and r < size-1):
        #print("5 ", end = "")
        #print("|"+str(rest))
        if (board[int(coord)+2*size-1] == 1):
            rest += 1
        #print("|"+str(rest))
        if (board[int(coord)+size-1] == 1):
            rest += 1
        #print("|"+str(rest))
        if (board[int(coord)+size] == 1):
            rest += 1
        #print("|"+str(rest))
        if (rest < score and point[int(coord) - size * q] == 0):
            #print("E|"+str(rest))
            return 1

    elif (int(coord)+size > boardsize):
        #print("6 ", end = "")
        if (board[int(coord)-2*size+1] == 1):
            rest += 1
        if (board[int(coord)-size+1] == 1):
            rest += 1
        if (board[int(coord)-size] == 1):
            rest += 1
        if (rest < score and point[int(coord) -size - size + 1 - size * (q-1)] == 0):
            #print("F|"+str(rest))
            return 1

    elif (q != 0 and r < size-1):
        #print("7 ", end = "")
        if (board[int(coord)-2*size+1] == 1):
            rest += 1
        if (board[int(coord)-size+1] == 1):
            rest += 1
        if (board[int(coord)-size] == 1):
            rest += 1
        nq = (int(coord) - size) // (size + size - 1)
        #if (rest < score and point[int(coord) -size - size + 1 - size * nq] == 0):
            #print("G|"+str(rest))

        nrest = 0
        #print("8 ", end = "")
        if (board[int(coord)+2*size-1] == 1):
            nrest += 1
        if (board[int(coord)+size-1] == 1):
            nrest += 1
        if (board[int(coord)+size] == 1):
            nrest += 1
        nq1 = (int(coord) + size - 1) // (size + size - 1) 
        #if (nrest < score and point[int(coord) -size - size + 1 - size * nq] == 0):
            #print("H|"+str(nrest))

        if (rest < score and nrest < score and point[int(coord) -size - size + 1 - size * nq] == 0 and point[int(coord) -size - size + 1 - size * nq1] == 0):
            return 1
        
    return 0

def CheckOneMove(board, point, boardsize, size, coord, r, q):
    #print("Current Move: " + str(coord), end = "")
    rest = 0
    if (r == size - 1):
        #print("1 ", end = "")
        if (board[int(coord)+1] == 1 ):
            rest += 1
        if (board[int(coord)+size] == 1):
            rest += 1
        if (board[int(coord)-size+1] == 1):
            rest+= 1
        if (rest == 3 and point[int(coord) - size + 1 - size * q] == 0):
            #print("A|"+str(rest))
            return 1
                
    elif (r > size - 1 and r != (size + size - 2)):
        #print("2 ", end = "")
        if (board[int(coord)+1] == 1):
            rest += 1
        if (board[int(coord)+size] == 1):
            rest += 1 
        if (board[int(coord)-size+1] == 1):
            rest += 1
        if (rest == 3 and point[int(coord) - size + 1 - size * q] == 0):
            return 1
           # print("B|"+str(rest))
        
        nrest = 0
        #print("3 ", end = "")
        if (board[int(coord)-1] == 1):
            nrest += 1
        if (board[int(coord)+size-1] == 1):
            nrest += 1
        if (board[int(coord)-size] == 1):
            nrest += 1
        if (nrest == 3 and point[int(coord)-1 - size + 1 - size * q] == 0):
            return 1

                
    elif (r == (size + size - 2)):
        #print("4 ", end = "")
        if (board[int(coord)-1] == 1):
            rest += 1
        if (board[int(coord)+size-1] == 1):
            rest += 1
        if (board[int(coord)-size] == 1):
            rest += 1
        if (rest == 3 and point[int(coord)-1 - size + 1 - size * q] == 0):
            #print("D|"+str(rest))
            return 1

    rest = 0
    if (q == 0 and r < size-1):
        #print("5 ", end = "")
        #print("|"+str(rest))
        if (board[int(coord)+2*size-1] == 1):
            rest += 1
        #print("|"+str(rest))
        if (board[int(coord)+size-1] == 1):
            rest += 1
        #print("|"+str(rest))
        if (board[int(coord)+size] == 1):
            rest += 1
        #print("|"+str(rest))
        if (rest == 3 and point[int(coord) - size * q] == 0):
            #print("E|"+str(rest))
            return 1

    elif (int(coord)+size > boardsize):
        #print("6 ", end = "")
        if (board[int(coord)-2*size+1] == 1):
            rest += 1
        if (board[int(coord)-size+1] == 1):
            rest += 1
        if (board[int(coord)-size] == 1):
            rest += 1
        if (rest == 3 and point[int(coord) -size - size + 1 - size * (q-1)] == 0):
            #print("F|"+str(rest))
            return 1

    elif (q != 0 and r < size-1):
        #print("7 ", end = "")
        if (board[int(coord)-2*size+1] == 1):
            rest += 1
        if (board[int(coord)-size+1] == 1):
            rest += 1
        if (board[int(coord)-size] == 1):
            rest += 1
        nq = (int(coord) - size) // (size + size - 1)
        if (rest == 3 and point[int(coord) -size - size + 1 - size * nq] == 0):
            #print("G|"+str(rest))
            return 1

        nrest = 0
        #print("8 ", end = "")
        if (board[int(coord)+2*size-1] == 1):
            nrest += 1
        if (board[int(coord)+size-1] == 1):
            nrest += 1
        if (board[int(coord)+size] == 1):
            nrest += 1
        nq1 = (int(coord) + size - 1) // (size + size - 1) 
        if (nrest == 3 and point[int(coord) -size - size + 1 - size * nq] == 0):
            return 1
        
    return 0



def getwintimes(board, point, boardsize, size, pointsize, availablemove, move):
    
    mlist = availablemove.copy()
    mlist.remove(move)
    blist = board.copy()
    plist = point.copy()
    blist[move] = 1
    q = move // (size + size - 1)
    r = move % (size + size - 1)
    wintimes = 0
    gametimes = 0

    if CheckScore(blist, plist, boardsize, size, move, r, q, 1) == 0:
        backupboard = blist.copy()
        backuppoint = plist.copy()
        backupmove = mlist.copy()

        while gametimes < 1000:
            #print("[Game " + str(gametimes) + "]", end = "")
            blist = backupboard.copy()
            plist = backuppoint.copy()
            mlist = backupmove.copy()
            while True:
                while True:
                    #displayboard(blist, plist, size)
                    check = checkwin(blist, plist, pointsize, size, 0)
                    #print("Game Continue with check value: " + str(check))
                    if (check >= 0):
                        #print("Check = " + str(check))
                        if (check == 2):
                            wintimes += 1
                        break
                    #Player 1 Make moves
                    coord = random.choice(mlist)
                    #print("A: Choose coord " + str(coord))
                    mlist.remove(coord)
                    blist[coord] = 1
                    q = coord // (size + size - 1)
                    r = coord % (size + size - 1)
                    if CheckScore(blist, plist, boardsize, size, coord, r, q, 1) == 0:
                        check = checkwin(blist, plist, pointsize, size, 0)
                        #print("Game Continue with check value: " + str(check))
                        #if (check >= 0):
                        #    if (check == 2):
                        #        wintimes += 1
                        break
                if check != -1:
                    break
                while True:
                    #Player 2 Make moves
                    #displayboard(blist, plist, size)
                    check = checkwin(blist, plist, pointsize, size, 0)
                    #print("Game Continue with check value: " + str(check))
                    if (check >= 0):
                        #print("Check = " + str(check))
                        if (check == 2):
                            wintimes += 1
                        break
                    coord = random.choice(mlist)
                    #print("B: Choose coord " + str(coord))
                    mlist.remove(coord)
                    blist[coord] = 1
                    q = coord // (size + size - 1)
                    r = coord % (size + size - 1)
                    if CheckScore(blist, plist, boardsize, size, coord, r, q, 2) == 0:
                        #check = checkwin(blist, plist, pointsize, size)
                        #if (check >= 0):
                        #    if (check == 2):
                        #        wintimes += 1
                        break
                if check != -1:
                    break
            gametimes += 1

    else:
        backupboard = blist.copy()
        backuppoint = plist.copy()
        backupmove = mlist.copy()
        while gametimes < 1000:
            #print("[Game " + str(gametimes) + "]", end = "")
            blist = backupboard.copy()
            plist = backuppoint.copy()
            mlist = backupmove.copy()
            while True:
                while True:
                    #displayboard(blist, plist, size)
                    check = checkwin(blist, plist, pointsize, size, 0)
                    #print("a Game Continue with check value: " + str(check))
                    if (check >= 0):
                        #print("Check = " + str(check))
                        if (check == 2):
                            wintimes += 1
                        break
                    
                    #Player 1 Make moves
                    coord = random.choice(mlist)
                    #print("A: Choose coord " + str(coord))
                    mlist.remove(coord)
                    blist[coord] = 1
                    q = coord // (size + size - 1)
                    r = coord % (size + size - 1)
                    if CheckScore(blist, plist, boardsize, size, coord, r, q, 1) == 0:
                        check = checkwin(blist, plist, pointsize, size, 0)
                        #print("Game Continue with check value: " + str(check))
                        #if (check >= 0):
                        #    if (check == 2):
                        #        wintimes += 1
                        break
                if check != -1:
                    break
                while True:
                    #Player 2 Make moves
                    #displayboard(blist, plist, size)
                    check = checkwin(blist, plist, pointsize, size, 0)
                    #print("B Game Continue with check value: " + str(check))
                    if (check >= 0):
                        #print("Check = " + str(check))
                        if (check == 2):
                            wintimes += 1
                        break
                    coord = random.choice(mlist)
                    #print("B: Choose coord " + str(coord))
                    mlist.remove(coord)
                    blist[coord] = 1
                    q = coord // (size + size - 1)
                    r = coord % (size + size - 1)
                    if CheckScore(blist, plist, boardsize, size, coord, r, q, 2) == 0:
                        #check = checkwin(blist, plist, pointsize, size)
                        #if (check >= 0):
                        #    if (check == 2):
                        #        wintimes += 1
                        break
                if check != -1:
                    break
            gametimes += 1
    #print("Wintimes: " + str(wintimes))
    print("Thinking ...")
    return wintimes




def MCTS(board, point, boardsize, size, pointsize, availablemove):
    #print("===================MCTS===================")
    #displayboard(board, point, size)
    if not availablemove:
        exit()
    #print(*availablemove)
    maxmove = -1
    finalmove = -1
    nlist = GetAvailable(board, boardsize)
    for move in availablemove:
        #print("Move: " + str(move))
        current = getwintimes(board, point, boardsize, size, pointsize, nlist, move)
        #print("Current: " + str(current))
        if current >= maxmove:
            maxmove = current
            finalmove = move
    return finalmove




def randplayer(board, point, boardsize, size, pointsize):
    print("Player B's turn")
    displaycoord(board, size)
    availablemove = GetAvailable(board, boardsize)
    #print("All Move List: ", end = "")
    #print(*availablemove)
    nmove = []
    omove = []
    for move in availablemove:
        q = move // (size + size - 1)
        r = move % (size + size - 1)
        if (CheckMove(board, point, boardsize, size, move, r, q, 2) == 1):
            nmove.append(move)
        if (CheckOneMove(board, point, boardsize, size, move, r, q) == 1):
            omove.append(move)
    
    print("All two Move List: ", end = "")
    print(*nmove)
    print("All Three Move List: ", end = "")
    print(*omove)
    print("\n")
    
    displayboard(board, point, size)
    invalid = True
    while invalid == True:
        #coord = randint(0, boardsize - 1) 
        if omove:
            #coord = random.choice(omove)
            #print(*omove)
            coord = MCTS(board, point, boardsize, size, pointsize, omove)
            print("Computer Chose " + str(coord))      
        if nmove and (not omove):
            #print(*nmove)
            #coord = random.choice(nmove)
            coord = MCTS(board, point, boardsize, size, pointsize, nmove)
            print("Computer Chose " + str(coord))
        if (not nmove) and (not omove):
            coord = MCTS(board, point, boardsize, size, pointsize, availablemove)
            print("Computer Chose " + str(coord))
           
        if (int(coord) > boardsize):
            invalid = True
        elif (int(coord) < 0):
            invalid = True
        elif (board[int(coord)] == 1):
            invalid = True
        else:
            invalid = False
    board[int(coord)] = 1
    q = int(coord) // (size + size - 1)
    r = int(coord) % (size + size - 1)
    
    return CheckScore(board, point, boardsize, size, coord, r, q, 2)





def CheckScore(board, point, boardsize, size, coord, r, q, player):
    getpoint = 0
    if (r == size - 1):
        if (board[int(coord)+1] == 1 and board[int(coord)+size] == 1 and board[int(coord)-size+1] == 1):
            if (point[int(coord) - size + 1 - size * q] == 0):
                point[int(coord) - size + 1 - size * q] = player
                getpoint = 1
    elif (r > size - 1 and r != (size + size - 2)):
        if (board[int(coord)+1] == 1 and board[int(coord)+size] == 1 and board[int(coord)-size+1] == 1):
            if (point[int(coord) - size + 1 - size * q] == 0):
                point[int(coord) - size + 1 - size * q] = player
                getpoint = 1
        if (board[int(coord)-1] == 1 and board[int(coord)+size-1] == 1 and board[int(coord)-size] == 1):
            if (point[int(coord)-1 - size + 1 - size * q] == 0):
                point[int(coord)-1 - size + 1 - size * q] = player
                getpoint = 1
    elif (r == (size + size - 2)):
        if (board[int(coord)-1] == 1 and board[int(coord)+size-1] == 1 and board[int(coord)-size] == 1):
            if (point[int(coord)-1 - size + 1 - size * q] == 0):
                point[int(coord)-1 - size + 1 - size * q] = player
                getpoint = 1
    if (q == 0 and r < size-1):
        if (board[int(coord)+size-1] == 1 and board[int(coord)+size] == 1 and board[int(coord)+2*size-1] == 1):
            if (point[int(coord) - size * q] == 0):
                point[int(coord) - size * q] = player
                getpoint = 1
    elif (int(coord)+size > boardsize):
        if (board[int(coord)-size+1] == 1 and board[int(coord)-size] == 1 and board[int(coord)-2*size+1] == 1):
            if (point[int(coord) -size - size + 1 - size * (q-1)] == 0):
                point[int(coord) -size - size + 1 - size * (q-1)] = player
                getpoint = 1
    elif (q != 0 and r < size-1):
        if (board[int(coord)-size+1] == 1 and board[int(coord)-size] == 1 and board[int(coord)-2*size+1] == 1):
            nq = (int(coord) - size) // (size + size - 1)
            if (point[int(coord) -size - size + 1 - size * nq] == 0): 
                point[int(coord) -size - size + 1 - size * nq] = player
                getpoint = 1
        if (board[int(coord)+size-1] == 1 and board[int(coord)+size] == 1 and board[int(coord)+2*size-1] == 1):
            nq = (int(coord) + size - 1) // (size + size - 1) 
            if (point[int(coord) - size * nq] == 0):
                point[int(coord) - size * nq] = player
                getpoint = 1
    return getpoint


def main():
    size = input("Please input the size: ")
    if(int(size) > 5):
        print("Invalid size!")
        return 0
    print(size + "*" + size + " Dots and Boxes Games")
    board = []
    point = []
    boardsize = 2*(int(size)*(int(size)+1))
    for i in range(boardsize):
        board.append(0)
    pointsize = int(size) * int(size) 
    for i in range(pointsize):
        point.append(0)
    #displayboard(board, point, int(size)+1)
    pointA = 1
    pointB = 1
    while True:
        while pointA == 1:
            pointA = getcmda(board, point, boardsize, int(size)+1)
            if checkwin(board, point, pointsize, int(size)+1, 1) >= 0:
                displayboard(board, point, int(size)+1)
                return 0
        pointA = 1
        print("\n--------------------------------------\n")
        while pointB == 1:
            #pointB = getcmdb(board, point, boardsize, int(size)+1)
            pointB = randplayer(board, point, boardsize, int(size)+1, pointsize)
            if checkwin(board, point, pointsize, int(size)+1, 1) >= 0:
                displayboard(board, point, int(size)+1)
                return 0
        pointB = 1
        print("--------------------------------------")
    
    return 0




main()
