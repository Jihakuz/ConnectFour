import time

def initBoard():
    #board is 7x5
    board = [["x","x","x","x","x","x","x"],\
             ["x","x","x","x","x","x","x"],\
             ["x","x","x","x","x","x","x"],\
             ["x","x","x","x","x","x","x"],\
             ["x","x","x","x","x","x","x"],\
             ["x","x","x","x","x","x","x"],\
             ["x","x","x","x","x","x","x"]]
    
    return board
    
def boardPrint(b):

    board = b

    print ("\n")
    
    for i in range (7): print (board[i])

    print ("\n")
    
def redGo(board):
    print ("\nRed's Go\n")
    flag = True
    
    while flag:
        
        x = int(input("X: "))
        y = int(input("Y: "))
       
        try:
            if "R" !=  board[y-1][x-1] or "Y" !=  board[y-1][x-1]:
                board[y-1][x-1] = "R"
                flag = False
            else: print ("\nSpace already taken, try again!\n")
                
        except IndexError or ValueError: print ("\nInvalid input, try again!\n")
        
    return board

def yellowGo(board):
    print ("\nYellow's Go\n")
    flag = True

    while flag:
        
        x = int(input("X: "))
        y = int(input("Y: "))
        
        try:
            if "R" !=  board[y-1][x-1] or "Y" !=  board[y-1][x-1]:
                board[y-1][x-1] = "Y"
                flag = False
            else: print ("\nSpace already taken, try again!\n")
                
        except IndexError or ValueError: print ("\nInvalid input, try again!\n")

    return board
        
def gravityCheck(board):
    for i in range(0,6):
        for j in range(0,7):           
            if board[i][j] == "R" or board[i][j] == "Y":
                change = board[i][j]
                if board[i+1][j] == "x":
                    board[i][j] = "x"
                    board[i+1][j] = change
        print ("\n" * 1000)
        print (boardPrint(board))
        time.sleep(0.5)

    print ("\n" * 1000)

def fourCheck(board):
            #check horizontal, vertical, right diagonal and left diagonal
    checks = [[[1,0],[2,0],[3,0]],\
              [[0,1],[0,2],[0,3]],\
              [[1,1],[2,2],[3,3]],\
              [[1,-1],[2,-2],[3,-3]]]

    Rpoints = 0
    Ypoints = 0

    for y in range(0,7):
        for x in range (0,7):
            if board[y][x] == "R":

                for i in range(len(checks)):
                    for j in range(len(checks[i])):
                        
                        try:
                            if board[y+checks[i][j][1]][x+checks[i][j][0]] == "R": Rpoints += 1
                            elif board[y+checks[i][j][1]][x+checks[i][j][0]] == "Y": Ypoints += 1
                                                       
                            if Rpoints == 4: return ("Red Wins")
                            elif Ypoints == 4: return ("Yelow Wins")
                        except IndexError: pass
                        
                    points = 0
    return None

def boardFull(board):
    for y in range(0,7):
            for x in range (0,7):
                if board[y][x] == "R" or board[y][x] == "Y":
                    return None

    return ("No one wins")
        

if __name__ == "__main__"
    #Setup
    b = initBoard()
    boardPrint(b)
    output = None

    #Gameloop
    while True:
        
        b = redGo(b)
        gravityCheck(b)
        boardPrint(b)

        output = fourCheck(b)
        if output != None:
            print (output)
            break

        output = boardFull(b)

        if output!= None:
            print (output)
            break        
        
        b = yellowGo(b)
        gravityCheck(b)
        boardPrint(b)
                                                                                                                                                                                                                                                                                                  
        fourCheck(b)


