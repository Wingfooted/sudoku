

grid  = [
    ["", "", "", 6, 7, 8, 9, 1, 2],
    ["", "", "", 1, 9, 5, 3, 4, 8],
    ["", "", "", 3, 4, 2, 5, 6, 7],
    [8, 5, 9, "", "", "", 4, 2, 3],
    [4, 2, 6, "", "", "", 7, 9, 1],
    [7, 1, 3, "", "", "", 8, 5, 6],
    [9, 6, 1, 5, 3, 7, "", "", ""],
    [2, 8, 7, 4, 1, 9, "", "", ""],
    [3, 4, 5, 2, 8, 6, "", "", ""]
] #grid can be edited for custom solutions. 

def display(board):
    for row in board:
        print(row)

def valid(board):
    valid = True

    #checking rows
    for row in board:
        row_elements = []
        for i in row:
            if i=="":
                pass
            elif i not in row_elements:
                row_elements.append(i) 
            else:
                #meaning that 
                valid = False
                #print("failed rows")

    #getting columns
    cols = []
    for x in range(9):
        col=[]
        for y in range(9):
            col.append(board[y][x])
        cols.append(col)

    #checking columns
    for col in cols:
        col_elements = []
        for i in col:
            if i=="":
                pass
            elif i not in col_elements:
                col_elements.append(i)
            else:
                valid= False
                #print("failed cols")


    #getting cubes
    cubes = []
    a,b,c = 1,2,3
    for y in range(3):
        for x in range(3):
            values = [

                board[0+3*y][0+3*x], board[0+3*y][1+3*x], board[0+3*y][2+3*x], #row 1
                board[1+3*y][0+3*x], board[1+3*y][1+3*x], board[1+3*y][2+3*x],#row 2
                board[2+3*y][0+3*x], board[2+3*y][1+3*x], board[2+3*y][2+3*x] #row 3

            ] #indexes in the form of y,x
            cubes.append(values)
    
    #checking cubes
    for cube in cubes:
        cube_elements = []
        for i in cube:
            if i=="":
                pass
            elif i not in cube_elements:
                cube_elements.append(i)
            else:
                valid= False
                #print("failed cubes")

    return valid

def full(board):
    complete = True
    for row in board:
        for number in row:
            if number:
                complete = False
    return complete

def solve(board, x=0, y=0, n=1):
    #print(n)
    #display(board)
    #print("new reccursion", "x:", x, "y:", y)

    #game complete
    if full(board) and valid(board):

        #program complete
        print('.')
        display(board)
        next = input(". ")
    
    #finding a unique cell
    #cell is full
    elif board[y][x] != "":
        if x == 8:
            solve(board, x=0, y=y+1,n=n+1)
        else:
            solve(board, x=x+1, y=y,n=n+1)

    #unique cell
    elif board[y][x] == "":
        nums = [i+1 for i in range(9)] #no's 1-9

        temp_board = board
        for number in nums:
            temp_board[y][x] = number
            #print("number", number)

            if valid(temp_board):
                #can continue
                if x==8:
                    solve(temp_board, x=0, y=y+1, n=n+1)
                else:
                    solve(temp_board, x=x+1, y=y, n=n+1)

            else:
                #print("backtrack")
                temp_board[y][x] = ""
                pass #this kills the solve. 


if __name__ == '__main__':
    solve(grid)