import heapq

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(problem):
    start = problem.snake.head()
    goal = problem.food
    snake_body = problem.snake.body
    obstacles=problem.obstacles

    open_set = []
    heapq.heappush(open_set, (0, start))

    came_from = {}
    g_score = {start: 0}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path

        for action in problem.get_actions():
            neighbor = (current[0] + action[0], current[1] + action[1])

            body = snake_body[:-1]

            if problem.is_valid(neighbor, body):

                temp_g = g_score[current] + problem.step_cost()

                if neighbor not in g_score or temp_g < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = temp_g
                    f = temp_g + heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f, neighbor))

    return []