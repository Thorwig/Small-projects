class Node():
    def __init__(self, position_x: float, position_y: float, obs: bool):
        self.x = position_x
        self.y = position_y
        self.neighbors = []
        self.obs = obs

    def add_neighbors(self, position_x: float, position_y: float, obs: bool):
        self.neighbors.append((position_x, position_y, obs))
