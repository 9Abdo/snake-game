def is_collision(head, body, grid_size):
    return (
        head[0] < 0 or head[0] >= grid_size or
        head[1] < 0 or head[1] >= grid_size or
        head in body
    )