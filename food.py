import random
import config

def spawn_food(snake):
    while True:
        f = (random.randint(0, config.GRID_SIZE-1),
             random.randint(0, config.GRID_SIZE-1))
        if f not in snake:
            return f