import heapq

def astar(problem):
    start = problem.snake.head()
    goal = problem.food

    open_set = [(0, start)]
    came_from = {}
    g = {start: 0}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            return reconstruct(came_from, current)

        for action in problem.get_actions():
            neighbor = problem.result(current, action)
            if not problem.is_valid(neighbor, problem.snake.body):
                continue
            temp_g = g[current] + problem.step_cost()

            if neighbor not in g or temp_g < g[neighbor]:
                g[neighbor] = temp_g
                came_from[neighbor] = current

                f = temp_g + problem.heuristic(neighbor)
                heapq.heappush(open_set, (f, neighbor))

    return []
def reconstruct(came_from, current):
    path = []
    while current in came_from:
        path.append(current)
        current = came_from[current]
    return path[::-1]