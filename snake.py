class Snake:
    def __init__(self):
        self.body = [(10, 10)]
        self.direction = (1, 0)

    def move(self, next_cell):
        self.body.insert(0, next_cell)

    def shrink(self):
        """ shrink the head of the snake """
        self.body.pop()

    def head(self):
        return self.body[0]