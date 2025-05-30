# env/tile_world.py

import numpy as np

class TileWorld:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = np.zeros((height, width), dtype=int)  # Note: [y][x] order!

    def is_in_bounds(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    def display(self, agent_x=None, agent_y=None):
        display_grid = self.grid.copy()

        if agent_x is not None and agent_y is not None:
            display_grid[agent_y][agent_x] = 8  # Show agent with an 8

        print(display_grid)
