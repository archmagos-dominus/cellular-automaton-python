import random as rnd
import pyglet


class cellular_automaton:

    # create a constructor
    # make sure that window_width and window_height are divisible with cell_size pls
    def __init__(self, window_width, window_height, cell_size, percent_fill):
        self.grid_width = int(window_width / cell_size)
        self.grid_height = int(window_height / cell_size)
        self.cell_size = cell_size
        self.percent_fill = percent_fill
        self.cells = []
        self.generate_cells()

    # create the "play grid" (as a list of lists)
    # also
    # create the first generation of cells at random (as close to percent_fill as practical)
    def generate_cells(self):
        for row in range(0, self.grid_height):
            self.cells.append([])
            for col in range(0, self.grid_width):
                if rnd.random() < self.percent_fill:
                    self.cells[row].append(1)   # creates living cell
                else:
                    self.cells[row].append(0)   # creates dead cell (empty space)

    def run_rules(self):
        # create a temp list of lists that will allow the program to change one cell state
        # without influencing the next cells
        temp = []
        for row in range(0, self.grid_height):
            temp.append([])
            for col in range(0, self.grid_width):
                # get the 'alive' and 'dead' values of all the neighbours
                cell_sum = sum([self.get_cell_value(row - 1, col),
                                self.get_cell_value(row - 1, col - 1),
                                self.get_cell_value(row, col - 1),
                                self.get_cell_value(row + 1, col - 1),
                                self.get_cell_value(row + 1, col),
                                self.get_cell_value(row + 1, col + 1),
                                self.get_cell_value(row, col + 1),
                                self.get_cell_value(row - 1, col + 1)])
                # if the cell is 'dead' and has 3 neighbours, it 'revives'
                if self.cells[row][col] == 0 and cell_sum == 3:
                    temp[row].append(1)
                # if the cell is alive and it has 2 or 3 neighbours it stays alive
                elif self.cells[row][col] == 1 and (cell_sum == 3 or cell_sum == 2):
                    temp[row].append(1)
                # if the cell has more than 3 neighbours it dies from over crowding
                # if it has less than 2 it dies from loneliness
                else:
                    temp[row].append(0)
        # update the real play area from the temp one
        self.cells = temp

    def get_cell_value(self, row, col):
        if 0 <= row < self.grid_height and 0 <= col < self.grid_width:
            return self.cells[row][col]
        return 0

    def draw(self):
        for row in range(0, self.grid_height):
            for col in range(0, self.grid_width):
                if self.cells[row][col] == 1:
                    # (0, 0) (0, 20) (20, 0) (20, 20)
                    square_coords = (row * self.cell_size, col * self.cell_size,
                                     row * self.cell_size, col * self.cell_size + self.cell_size,
                                     row * self.cell_size + self.cell_size, col * self.cell_size,
                                     row * self.cell_size + self.cell_size, col * self.cell_size + self.cell_size)
                    pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES,
                                                 [0, 1, 2, 1, 2, 3],
                                                 ('v2i', square_coords))
