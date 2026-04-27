def greedy(problem):
    start = problem.snake.head()
    goal = problem.food

    current = start
    came_from = {}
    visited = {current}

    while current != goal:
        best = None
        best_dist = float("inf")

        for action in problem.get_actions():
            neighbor = problem.result(current, action)

            if not problem.is_valid(neighbor, problem.snake.body):
                continue

            if neighbor in visited:
                continue

            dist = problem.heuristic(neighbor)

            if dist < best_dist:
                best_dist = dist
                best = neighbor
                came_from[neighbor] = current

        if best is None:
            return []

        current = best
        visited.add(current)

    return reconstruct(came_from, current)


def reconstruct(came_from, current):
    path = []
    while current in came_from:
        path.append(current)
        current = came_from[current]
    return path[::-1]