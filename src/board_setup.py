import numpy as np



def setup_board():
    grid = np.zeros((3,3,3,3,10))
    for OY in grid:
        for IY in OY:
            for OX in IY:
                for IX in OX:
                    for num in range(0,10):
                        IX[num] = num
    return grid

def input_board(grid):
    for OY in range(0,3):
        for OX in range(0,3):
            boxcode = input()
            counter = 0
            for IY in range(0,3):
                for IX in range(0,3):
                    grid[OX,OY,IX,IY] = [boxcode[counter], 0,0,0,0,0,0,0,0,0]
                    counter = counter + 1
    return grid

def print_board(grid):
    for OY in range(0,3):
        for IY in range(0,3):
            for OX in range(0,3):
                for IX in range(0,3):
                    print(int(grid[OX,OY,IX,IY,0]), end = "|")
                print(end="  ")
            print()
        print("---------------------")