print("Welcome to Sudoku!")

myBoard = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def main():
    draw_board(myBoard)
    solve(myBoard)
    print ("\n")
    draw_board(myBoard)

# prints out our sudoku board above
def draw_board(board):
    for row in range(len(board)):                              # len of our board will be 9 ∴ this iterates 9 times
        if row % 3 == 0 and row != 0:                          # for every third row, but not the first row, we print a seperating line
            print("— — — — — — — — — — — —")

        for coloumn in range(len(board[0])):                   # for every row, there is a coloumn with 9 numbers
            if coloumn % 3 == 0 and coloumn != 0:              # for every third coloumn, but not the first coloumn, we print a seperating line
                print (" ╵ ", end="")
            if coloumn == 8:
                print(board[row][coloumn])                     # for the final coloumn of each row, we must go to the next line (\n)
            else: 
                print(str(board[row][coloumn])+ " ", end="")   # for the rest, a simple " " will suffice

# backtracking algorithm
def solve(board):

    myPrint = draw_board(board)
    myPrint(board)
   
    print(board)
    myFind = find_empty(board)
    if not myFind:                                             # if there are no empty squares and myFind returns False: 
        return True                                            # board is solved
    else:
        row, coloumn = myFind                                  # empty square becomes the one we work on
    
    for number in range(1, len(board)+1):                      # we pass every possible value, in this case 1-9 to validate
        if valid(board, number, (row, coloumn)):
            board[row][coloumn] = number                       # assume this number does fit here, and continue 

            if solve(board):                                   # recursively calls the function
                return True
            
            board[row][coloumn] = 0                            # only falls to this if solution is invalid, resets value to 0 and tries again
    
    return False                                               # returning false here asks the for loop to run again with the next guess from the first square

# finds empty or '0' squares on the board and returns their position as a tuple
def find_empty(board):
    for row in range(len(board)):
        for coloumn in range(len(board[row])):
            if board[row][coloumn] == 0:
                return (row,coloumn)                           # this becomes the position tuple given to the "valid" function
    return None

# checks if number is valid at given position
def valid(board, number, position):                            
    for row in range(len(board)):                              # check row
        if board[position[0]][row] == number and position[1] != row: 
            return False                                       # if number exists in any other position in that row, there's a problem
    
    for row in range(len(board)):                              # check coloumn
        if board[row][position[1]] == number and position[0] != row:
            return False                                       # if number exists in any other position in that coloumn, there's a problem

    # checks 3x3 box
    box_Y_cord = position[0] // 3                              # we want the floor value for the box from the tuple given
    box_X_cord = position[1] // 3                              # (0,1,2) -> 0 | (3-5) -> 1 | (6-8) -> 2

    for row in range(box_Y_cord * 3, box_Y_cord * 3 + 3):      # given box number, now we need to search each row in that range
        for coloumn in range(box_X_cord * 3, box_X_cord * 3 + 3):   # each coloumn
            if board[row][coloumn] == number and (row,coloumn) != position:     # if the co-ordinate is equal to the number  
                return False                                                    # and NOT the number we just inserted, return false

    return True                                                # if number isn't found at all, return True! (we have a valid position)



main()

