import random
import config

def spawn_food(snake,obstacles):
    while True:
        f = (random.randint(0, config.GRID_SIZE-1),
             random.randint(0, config.GRID_SIZE-1))
        if f not in snake and  f not in obstacles:
            return f