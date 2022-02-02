import random

w = 5
h = 5


rules = [
    ["rule", "state", "alive neighbours", "next state"],
    ["First", 1, "1 or 0", 0],
    ["Second", 1, "2 or 3", 1],
    ["Third", 1, "4", 0],
    ["Fourth", 0, "3", 1]
]



cells = []
board_vals = []

threshold = 0.9

def dead_state(width, height):
    for i in range(0,height):
        row = [0 for j in range(0,width)]
        cells.append(row)

def random_state(width, height):
    for i in range(0,height):
        row = []
        row_vals = []
        for j in range(0,width):
            x = random.uniform(0,1)
            if x > threshold:
                row.append( "o")
                row_vals.append( 1 )
            else:
                row.append("-")
                row_vals.append( 0 )

        cells.append(row)
        board_vals.append(row_vals)
        
    
    return cells, board_vals


def render(board_state):
    
    for row in board_state[1]:
        print(*row)
    #for row in board_state[0]:
     #   print(*row)


def check_alive_neighbors(board_state):
    alive_neighbours_matrix = []
    for row in range(0,len(board_state[0])):
        row_alive = []
        for column in range(0,len(board_state[0][0])):
            cell_state = board_state[1][row][column]
            
            if row == 0 and column == 0:
                alive_neighbours = sum([board_state[1][row][column+1], board_state[1][row+1][column], board_state[1][row+1][column+1]])
                row_alive.append(alive_neighbours)
            
            elif row == 0 and column <  len(board_state[0][0])-1:
                alive_neighbours = sum([board_state[1][row][column+1], board_state[1][row+1][column], board_state[1][row+1][column+1],board_state[1][row][column-1],board_state[1][row+1][column-1]])
                row_alive.append(alive_neighbours)

            elif row == 0 and column == len(board_state[0][0])-1:
                alive_neighbours = sum([board_state[1][row+1][column], board_state[1][row][column-1],board_state[1][row+1][column-1]])
                row_alive.append(alive_neighbours)

            elif row <  len(board_state[0])-1 and column == 0:
                alive_neighbours = sum([board_state[1][row][column+1], board_state[1][row+1][column], board_state[1][row+1][column+1],board_state[1][row-1][column],board_state[1][row-1][column+1]])
                row_alive.append(alive_neighbours)
            
            elif row <  len(board_state[0])-1 and column <  len(board_state[0][0])-1:
                alive_neighbours = sum([board_state[1][row-1][column-1], board_state[1][row-1][column], board_state[1][row-1][column+1], board_state[1][row][column-1], board_state[1][row][column+1], board_state[1][row+1][column-1],board_state[1][row+1][column],board_state[1][row+1][column+1]])
                row_alive.append(alive_neighbours)

            elif row <  len(board_state[0])-1 and column == len(board_state[0][0])-1:
                alive_neighbours = sum([board_state[1][row-1][column-1], board_state[1][row-1][column], board_state[1][row][column-1],board_state[1][row+1][column-1],board_state[1][row+1][column]])
                row_alive.append(alive_neighbours)

            elif row ==  len(board_state[0])-1 and column == 0:
                alive_neighbours = sum([board_state[1][row][column+1],board_state[1][row-1][column],board_state[1][row-1][column+1]])
                row_alive.append(alive_neighbours)
            
            elif row ==  len(board_state[0])-1 and column <  len(board_state[0][0])-1:
                alive_neighbours = sum([board_state[1][row-1][column-1], board_state[1][row-1][column], board_state[1][row-1][column+1], board_state[1][row][column-1], board_state[1][row][column+1]])
                row_alive.append(alive_neighbours)

            elif row ==  len(board_state[0])-1 and column == len(board_state[0][0])-1:
                alive_neighbours = sum([board_state[1][row-1][column-1], board_state[1][row-1][column], board_state[1][row][column-1]])
                row_alive.append(alive_neighbours)
        
        alive_neighbours_matrix.append(row_alive)
    
    print("*"*10)
    for r in alive_neighbours_matrix:
        print(*r)            
    print("*"*10)
    return alive_neighbours_matrix



#def next_board_state():

state = random_state(w,h)

check_alive_neighbors(state)

render(state)