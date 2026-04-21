class SnakeProblem:
    def __init__(self, snake, food, grid_size):
        self.snake = snake
        self.food = food
        self.grid_size = grid_size

    def get_state(self):
        return (tuple(self.snake.body), self.food)

    def is_goal(self):
        return self.snake.head() == self.food


    def get_actions(self):
        return [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def result(self, action):
        head = self.snake.head()
        new_head = (head[0] + action[0], head[1] + action[1])
        return new_head

    def step_cost(self):
        return 1