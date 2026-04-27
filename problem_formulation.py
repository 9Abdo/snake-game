class SnakeProblem:
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

    def __init__(self, snake, food, grid_size, obstacles):
        self.snake = snake
        self.food = food
        self.grid_size = grid_size
        self.obstacles = obstacles

    def is_goal(self):
        return self.snake.head() == self.food

    def get_actions(self):
        return [self.UP, self.DOWN, self.LEFT, self.RIGHT]

    def result(self, state, action):
        x, y = state
        dx, dy = action
        return x + dx, y + dy

    def step_cost(self):
        return 1

    def is_valid(self, cell, body):
        x, y = cell
        if x < 0 or x >= self.grid_size or y < 0 or y >= self.grid_size:
            return False

        if cell in self.obstacles:
            return False

        if cell in body[:-1]:
            return False

        return True
    def heuristic(self, cell):
        return abs(cell[0] - self.food[0]) + abs(cell[1] - self.food[1])