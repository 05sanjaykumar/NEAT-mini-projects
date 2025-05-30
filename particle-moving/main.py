from env.tile_world import TileWorld
from agent.particle import CuriousParticle
from reward.novelty_reward import NoveltyReward
from rl.q_learning import QLearner

import time

ACTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # up, right, down, left

world = TileWorld(width=10, height=10)
reward_engine = NoveltyReward(world)
learner = QLearner(ACTIONS)
agent = CuriousParticle(world, reward_engine, learner)

for _ in range(100):
    agent.move()
    world.display()
    time.sleep(0.1)
    print("---")
