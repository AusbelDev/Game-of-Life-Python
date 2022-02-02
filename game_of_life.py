import random
import time
w = 30
h = 30

cells = []
board_vals = []

threshold = 0.9

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
    for row in board_state[0]:
        print(*row)
    print("*"*20)
    


def check_alive_neighbours(board_state):
    alive_neighbours_matrix = []
    for row in range(0,len(board_state)):
        row_alive = []
        for column in range(0,len(board_state[0])):
            
            
            if row == 0 and column == 0:
                alive_neighbours = sum([board_state[row][column+1], board_state[row+1][column], board_state[row+1][column+1]])
                row_alive.append(alive_neighbours)
            
            elif row == 0 and column <  len(board_state[0])-1:
                alive_neighbours = sum([board_state[row][column+1], board_state[row+1][column], board_state[row+1][column+1],board_state[row][column-1],board_state[row+1][column-1]])
                row_alive.append(alive_neighbours)

            elif row == 0 and column == len(board_state[0])-1:
                alive_neighbours = sum([board_state[row+1][column], board_state[row][column-1],board_state[row+1][column-1]])
                row_alive.append(alive_neighbours)

            elif row <  len(board_state)-1 and column == 0:
                alive_neighbours = sum([board_state[row][column+1], board_state[row+1][column], board_state[row+1][column+1],board_state[row-1][column],board_state[row-1][column+1]])
                row_alive.append(alive_neighbours)
            
            elif row <  len(board_state)-1 and column <  len(board_state[0])-1:
                alive_neighbours = sum([board_state[row-1][column-1], board_state[row-1][column], board_state[row-1][column+1], board_state[row][column-1], board_state[row][column+1], board_state[row+1][column-1],board_state[row+1][column],board_state[row+1][column+1]])
                row_alive.append(alive_neighbours)

            elif row <  len(board_state)-1 and column == len(board_state[0])-1:
                alive_neighbours = sum([board_state[row-1][column-1], board_state[row-1][column], board_state[row][column-1],board_state[row+1][column-1],board_state[row+1][column]])
                row_alive.append(alive_neighbours)

            elif row ==  len(board_state)-1 and column == 0:
                alive_neighbours = sum([board_state[row][column+1],board_state[row-1][column],board_state[row-1][column+1]])
                row_alive.append(alive_neighbours)
            
            elif row ==  len(board_state)-1 and column <  len(board_state[0])-1:
                alive_neighbours = sum([board_state[row-1][column-1], board_state[row-1][column], board_state[row-1][column+1], board_state[row][column-1], board_state[row][column+1]])
                row_alive.append(alive_neighbours)

            elif row ==  len(board_state)-1 and column == len(board_state[0])-1:
                alive_neighbours = sum([board_state[row-1][column-1], board_state[row-1][column], board_state[row][column-1]])
                row_alive.append(alive_neighbours)
        
        alive_neighbours_matrix.append(row_alive)
    
    return alive_neighbours_matrix



def next_board_state(board_state):
    new_board_state = []
    cells = []
    state_matrix = board_state[1]
    alive_neighbours_matrix = check_alive_neighbours(state_matrix)

    for row in range(0,len(state_matrix)):
        new_row_state = []
        row_toappend = []
        for column in range(0,len(state_matrix[0])):
            cell_state =  state_matrix[row][column]
            alive_neighbours = alive_neighbours_matrix[row][column]
            #print(cell_state, alive_neighbours)
            if cell_state == 1 and alive_neighbours <= 1:
                new_row_state.append( 0 )
                row_toappend.append("-")
            elif cell_state == 1 and alive_neighbours == 3:
                new_row_state.append( 1 )
                row_toappend.append("o")
            elif cell_state == 1 and alive_neighbours == 2:
                new_row_state.append( 1 )
                row_toappend.append("o")
            elif cell_state == 1 and alive_neighbours > 3:
                new_row_state.append( 0 )
                row_toappend.append("-")
            elif cell_state == 0 and alive_neighbours == 3:
                new_row_state.append( 1 )
                row_toappend.append("o")
            else:
                new_row_state.append( 0 )
                row_toappend.append("-")
        
        new_board_state.append(new_row_state)
        cells.append(row_toappend)

    return cells, new_board_state

board_state = random_state(w,h)

render(board_state)



for i in  range(0,100):
    
    new_board = next_board_state(board_state)
    
    time.sleep( 0.5 )
    render(new_board)
    board_state = new_board
