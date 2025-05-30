# agent/particle.py

import random

class CuriousParticle:
    def __init__(self, world, reward_engine, learner):
        self.x = 0
        self.y = 0
        self.world = world
        self.reward_engine = reward_engine
        self.learner = learner
        self.total_reward = 0

    def get_state(self):
        return (self.x, self.y)


    def move(self):
        state = self.get_state()
        action = self.learner.get_action(state)
        dx, dy = action
        new_x = self.x + dx
        new_y = self.y + dy

        if self.world.is_in_bounds(new_x, new_y):
            reward = self.reward_engine.get_reward(new_x,new_y)
            next_state = (new_x,new_y)

            self.learner.update(state, action, reward, next_state)
            self.x = new_x
            self.y = new_y
            self.total_reward += reward
            print(f"Moved to {next_state} | Reward: {reward:.2f} | Total: {self.total_reward:.2f}")