# env/tile_world.py

import numpy as np

class TileWorld:
    def __init__(self, width=10, height=10):
        self.width = width
        self.height = height
        self.grid = np.zeros((height, width), dtype=int)  # 0 = unexplored

    def is_in_bounds(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    def mark_visited(self, x, y):
        self.grid[y][x] = 1  # 1 = visited

    def display(self):
        print(self.grid)
