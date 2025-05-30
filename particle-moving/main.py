# main.py

from env.tile_world import TileWorld
from agent.particle import CuriousParticle
from reward.novelty_reward import NoveltyReward
import time

world = TileWorld(width=10, height=10)
reward_engine = NoveltyReward(world)
agent = CuriousParticle(world)

for _ in range(50):  # simulate 50 steps
    agent.move()
    world.display()
    time.sleep(0.2)
    print("---")
