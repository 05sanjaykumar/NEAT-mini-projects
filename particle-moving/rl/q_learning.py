# rl/q_learning.py

import random
from collections import defaultdict

class QLearner:
    def __init__(self, actions, alpha=0.1, gamma=0.9, epsilon=0.2):
        self.q_table = defaultdict(lambda: defaultdict(float))
        self.actions = actions  # List of possible actions
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon

    def get_action(self, state):

        if random.random()<self.epsilon:
            return random.choice(self.actions)
        q_vals=self.q_table[state]
        return max(self.actions, key=lambda a:q_vals[a])
    
    def update(self, state, action, reward, next_state):
        max_future_q = max(self.q_table[next_state].values(), default=0.0)
        old_q = self.q_table[state][action]
        new_q = old_q + self.alpha * (reward + self.gamma * max_future_q - old_q)
        self.q_table[state][action] = new_q