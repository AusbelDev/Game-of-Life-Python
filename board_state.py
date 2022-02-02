import random

w = 5
h =5

cells = []

def dead_state(width, height):
    for i in range(0,height):
        row = [0 for j in range(0,width)]
        cells.append(row)

def random_state(width, height):
    for i in range(0,height):
         row = [random.randint(0,1) for j in range(0,width)]
         cells.append(row)
    print(cells)

random_state(w,h)