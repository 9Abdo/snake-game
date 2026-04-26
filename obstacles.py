import random
import config

def spawn_obstacles(snake, food, num=15):
    obstacles = []

    while len(obstacles) < num:
        o = (random.randint(0, config.GRID_SIZE-1),
             random.randint(0, config.GRID_SIZE-1))

        if o not in snake and o != food and o not in obstacles:
            obstacles.append(o)

    return obstacles