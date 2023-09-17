import numpy as np

class Actions:
    def __init__(self, m):
        self.m = m
        self.mean = 0
        self.t = 0

    def choose(self):
        return np.random.randn() + self.m

    def update(self, x):
        self.t += 1
        self.mean = (1 - 1.0 / self.t) * self.mean + 1.0 / self.t * x
        return self.mean
