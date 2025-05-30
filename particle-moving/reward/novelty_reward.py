# reward/novelty_reward.py
class NoveltyReward:
    def __init__(self, world):
        self.world = world
        self.visited = set()

    def get_reward(self, x, y):
        pos = (x, y)
        if pos not in self.visited:
            self.visited.add(pos)
            self.world.grid[y][x] = 1
            return 1.0  # reward for new tile
        else:
            return -0.1  # penalty for repeat visit