import random

w = 20
h = 30

cells = []

threshold = 0.9
def dead_state(width, height):
    for i in range(0,height):
        row = [0 for j in range(0,width)]
        cells.append(row)

def random_state(width, height):
    for i in range(0,height):
        row = []
         #row = [random.randint(0,1) for j in range(0,width)]
        for j in range(0,width):
            x = random.uniform(0,1)
            if x > threshold:
                row.append( "o")
            else:
                row.append("-")

        cells.append(row)
    return cells


def render(board_state):
    
    for row in board_state:
        print(*row)

state = random_state(w,h)

render(state)