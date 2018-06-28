def initBoard():
    #board is 7x5
    board = [["x","x","x","x","x","x","x"],["x","x","x","x","x","x","x"],\
             ["x","x","x","x","x","x","x"],["x","x","x","x","x","x","x"],\
             ["x","x","x","x","x","x","x"],["x","x","x","x","x","x","x"],\
             ["x","x","x","x","x","x","x"]]
    return board
    
def boardPrint(b):

    board = b

    print ("\n")
    
    for i in range (7):
        print (board[i])

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
            else:
                print ("\nSpace already taken, try again!\n")
        except IndexError:
            print ("\nInvalid input, try again!\n")
        
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
            else:
                print ("\nSpace already taken, try again!\n")
        except IndexError:
            print ("\nInvalid input, try again!\n")

    return board
        
def gravityCheck(board):
    for i in range(0,6):
        for j in range(0,7):           
            if board[i][j] == "R" or board[i][j] == "Y":
                change = board[i][j]
                if board[i+1][j] == "x":
                    board[i][j] = "x"
                    board[i+1][j] = change

def fourCheck(board):
    #check horizontal for Red
    for y in range(0,7):
        for x in range (0,7):
            if board[y][x] == "R":
                try:
                    
                    if board[y+1][x] == "R" and board[y+2][x] == "R" \
                       and board[y+3][x] == "R":
                        return ("Red Wins")

                except IndexError:
                    pass
                
    #check horzontal for Yellow      
    for y in range(0,7):
        for x in range (0,7):
            if board[y][x] == "Y":
                try:
                    
                    if board[y+1][x] == "Y" and board[y+2][x] == "Y" \
                       and board[y+3][x] == "Y":
                        return ("Yellow Wins!")

                except IndexError:
                    pass
    

    #check vertical for Red
    for y in range(0,7):
        for x in range (0,7):
            if board[y][x] == "R":
                try:
                    
                    if board[y][x+1] == "R" and board[y][x+2] == "R" \
                       and board[y][x+3] == "R":
                        return ("Red Wins!")

                except IndexError:
                    pass

    
    #check vertical for Yellow
    for y in range(0,7):
        for x in range (0,7):
            if board[y][x] == "Y":
                try:
                    
                    if board[y][x+1] == "Y" and board[y][x+2] == "Y" \
                       and board[y][x+3] == "Y":
                        return ("Yellow Wins!")

                except IndexError:
                    pass

    
    #check vertical for Yellow
    for y in range(0,7):
        for x in range (0,7):
            if board[y][x] == "R":
                try:
                    
                    if board[y+1][x+1] == "R" and board[y+2][x+2] == "R" \
                       and board[y+3][x+3] == "R":
                        return ("Yellow Wins!")

                except IndexError:
                    pass
    
    #check vertical for Yellow
    for y in range(0,7):
        for x in range (0,7):
            if board[y][x] == "Y":
                try:
                    
                    if board[y+1][x+1] == "Y" and board[y+2][x+2] == "Y" \
                       and board[y+3][x+3] == "Y":
                        return ("Yellow Wins!")

                except IndexError:
                    pass

            
               
def main():
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
        
        b = yellowGo(b)
        gravityCheck(b)
        boardPrint(b)
                                                                                                                                                                                                                                                                                                  
        fourCheck(b)


main()




