import random

# function to initialize game
def start_game():
    # initialize the grid
    mat = []
    for i in range(4):
        mat.append([0] * 4)
    
    # printing controls for user
    print("Commands are as follows : ")
    print("'W' or 'w' : Move Up")
    print("'S' or 's' : Move Down")
    print("'A' or 'a' : Move Left")
    print("'D' or 'd' : Move Right")
    
    # add a new 2 in grid after every step
    add_new_2(mat)
    
    return mat

# function to print the matrix line by line
def print_matrix(mat):
    for row in mat:
        print(" ".join(str(cell).rjust(4) for cell in row))
    print() 

# function to add a new 2 in grid at any random empty cell
def add_new_2(mat):
    # generate random indexes for row and column
    r = random.randint(0, 3)
    c = random.randint(0, 3)
    
    # use a while loop to make sure the randomly chosen cell is empty
    while(mat[r][c] != 0):
        r = random.randint(0, 3)
        c = random.randint(0, 3)
        
    mat[r][c] = 2
    
# function to get the current state of game
def get_current_state(mat):
    
    # if any cells is 2048, then print win
    for i in range(4):
        for j in range(4):
            if (mat[i][j] == 2048):
                return "You win!"
    
    # if there is still empty cell, game is not over
    for i in range(4):
        for j in range(4):
            if (mat[i][j] == 0):
                return "GAME NOT OVER"
    
    # if no cell is empty, but after any move left, right, up or down, 
    # any two cells get merged and create an empty cell,
    # then the game is not over
    for i in range(3):
        for j in range(3):
            if(mat[i][j]== mat[i + 1][j] or mat[i][j]== mat[i][j + 1]):
                return 'GAME NOT OVER'
    
    for j in range(3):
        if(mat[3][j]== mat[3][j + 1]):
            return 'GAME NOT OVER'

    for i in range(3):
        if(mat[i][3]== mat[i + 1][3]):
            return 'GAME NOT OVER'
        
    # else the game is over
    return 'GAME OVER'

# function to compress the grid after every step before and after merging cells
def compress(mat):
    changed = False
    
    # empty grid 
    new_mat = []
    
    # with all cells empty
    for i in range(4):
        new_mat.append([0] * 4)
    
    # we will shift entries of each cell to its extreme left row by row    
    for i in range(4):
        pos = 0
        
        for j in range(4):
            if(mat[i][j] != 0):
                new_mat[i][pos] = mat[i][j]
            
                if(j != pos):
                    changed = True
                pos += 1
    
    return new_mat, changed

# function to merge the cells in matrix after compression
def merge(mat):
    changed = False
    
    # merge the current cell with the next cell in the row 
    # if they have same value and are non empty
    for i in range(4):
        for j in range(3):
            if(mat[i][j] == mat[i][j+1] and mat[i][j] != 0):
                mat[i][j] = mat[i][j] * 2
                mat[i][j+1] = 0
                changed = True
    return mat, changed

# function to reverse the matrix
# reverse the content of each row
def reverse(mat):
    new_mat = []
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[i][3-j])
    return new_mat

# function to get the transpose of matrix
def transpose(mat):
    new_mat = []
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[j][i])
    return new_mat

# function to move left
def move_left(grid):
    # compress the grid
    new_grid, changed1 = compress(grid)
    
    # merge the cells.
    new_grid, changed2 = merge(new_grid)
    
    changed = changed1 or changed2
    
    # compress after merging.
    new_grid, temp = compress(new_grid)
    
    return new_grid, changed

# function to move right
def move_right(grid):
    # reverse the matrix
    new_grid = reverse(grid)
    
    # move left
    new_grid, changed = move_left(new_grid)
    
    # reverse the matrix again
    new_grid = reverse(new_grid)
    
    return new_grid, changed

# function to move up
def move_up(grid):
    # transpose the matrix
    new_grid = transpose(grid)
    
    # move left
    new_grid, changed = move_left(new_grid)
    
    # transpose the matrix again
    new_grid = transpose(new_grid)
    
    return new_grid, changed

# function to move down
def move_down(grid):
    # transpose the matrix
    new_grid = transpose(grid)
    
    # move right
    new_grid, changed = move_right(new_grid)
    
    # transpose the matrix again
    new_grid = transpose(new_grid)
    
    return new_grid, changed