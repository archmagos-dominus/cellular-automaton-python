from tkinter import *
import tkinter as tk
from random import random


# create the grid array
def create_grid(size):
    # global variables that can be used in the other functions
    global grid, cell_size
    # dictate the cell size as screen_width/number_of_cells
    cell_size = int(500 / size.get())
    # initialize grid
    grid = list()
    # iterate through the grid array
    for i in range(size.get()):
        # array becomes 2d by inserting another array as an element to the first
        grid.append(list())
        # iterate through the added array
        for j in range(size.get()):
            # initialize x as a random value from 0 to 1
            x = random()
            # if x is more than 0.5, the cell is considered "Alive"
            if x >= 0.5:
                grid[-1].append(1)
            # otherwise it is considered "Dead"
            else:
                grid[-1].append(0)


# update canvas
def update_field(f: tk.Canvas) -> None:
    # global variables that can be used in the other functions
    global grid, cell_size
    # call to update grid
    update_grid()
    # display updated grid on the canvas
    for i in range(len(grid)):
        for j in range(len(grid)):
            # create green cell if the cell is 'alive' or red if it's 'dead'
            if grid[i][j] == 1:
                field.create_rectangle(i * cell_size, j * cell_size, i * cell_size + cell_size,
                                       j * cell_size + cell_size, fill='green')
            else:
                field.create_rectangle(i * cell_size, j * cell_size, i * cell_size + cell_size,
                                       j * cell_size + cell_size, fill='gray')


def update_grid():
    # global grid variable
    global grid
    # tempgrid variable holding the temporary updated grid values
    tempgrid = grid
    # iterate through the grid
    for i in range(len(grid)):
        for j in range(len(grid)):
            # define next and previous rows and columns
            # special cases for first and last rows and columns
            # in order for the 'play area' to become faux infinite
            # by looping around all edges
            if i == 0:
                prev_row = len(grid) - 1
            else:
                prev_row = i - 1

            if i == len(grid) - 1:
                next_row = 0
            else:
                next_row = i + 1

            if j == 0:
                prev_col = len(grid[i]) - 1
            else:
                prev_col = j - 1

            if j == len(grid[i]) - 1:
                next_col = 0
            else:
                next_col = j + 1
            # calculate the sum of the cells neighbour
            cell_sum = sum([grid[prev_row][prev_col],
                            grid[prev_row][j],
                            grid[prev_row][next_col],
                            grid[i][prev_col],
                            grid[i][next_col],
                            grid[next_row][prev_col],
                            grid[next_row][j],
                            grid[next_row][next_col]
                            ])
            # check the rules in order to decide the fate of the cell
            # if it's dead and has 3 neighbours it becomes alive
            # if it is alive and it has less than 2 neighbours it dies of loneliness
            # if it is alive and it has more than 3 neighbours it dies of overcrowding
            if cell_sum == 3 and grid[i][j] == 0:
                tempgrid[i][j] = 1
            elif grid[i][j] == 1 and (cell_sum == 2 or cell_sum == 3):
                tempgrid[i][j] = 1
            else:
                tempgrid[i][j] = 0
    # old grid becomes the new grid
    grid = tempgrid


# define the root window of the tkinter GUI
root = tk.Tk()
# initialize the size_var as an IntVar
size_var = tk.IntVar()
# create canvas 500x500
field = tk.Canvas(root, width=500, height=500)
field.pack()
# create input for the size of the grid
size_sbox = Spinbox(root, from_=3, to=50, textvariable=size_var)
size_sbox.pack()
next_button = tk.Button(root, text="Next Iteration", command=lambda: update_field(field))
next_button.pack()
init_button = tk.Button(root, text="New Initialization", command=lambda: create_grid(size_var))
init_button.pack()
tk.mainloop()
