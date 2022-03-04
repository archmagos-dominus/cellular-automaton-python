import pyglet  # pyglet is used to create the window and draw the shapes
from celular_automaton import cellular_automaton as ca


# preferred way to create a window according to the docs
# (create a class that inherits from the window class)
class Window(pyglet.window.Window):

    # create a constructor
    def __init__(self):
        super().__init__(600, 600)  # size of window
        self.ca = ca(600,   # "play" size x
                     600,   # "play" size y
                     10,    # size of cell
                     0.6)   # percent of play area filled with living cells
        pyglet.clock.schedule_interval(self.update, 1.0 / 5.0)  # update interval (fps controller)

    def on_draw(self):
        self.clear()    # clear the window
        self.ca.draw()  # draw the first generation

    def update(self, dt):
        self.ca.run_rules() # change the play are according to the rule book


# main function
if __name__ == '__main__':
    window = Window()  # create an instance of the Window class
    pyglet.app.run()  # run
