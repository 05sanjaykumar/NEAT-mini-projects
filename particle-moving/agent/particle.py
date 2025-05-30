# agent/particle.py

import random

class CuriousParticle:
    def __init__(self, world):
        self.x = 0
        self.y = 0
        self.world = world
        self.world.mark_visited(self.x, self.y)


    def move(self):
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        dx, dy = random.choice(directions)
        new_x = self.x + dx
        new_y = self.y + dy

        if self.world.is_in_bounds(new_x, new_y):
            self.x = new_x
            self.y = new_y
            self.world.mark_visited(self.x, self.y)