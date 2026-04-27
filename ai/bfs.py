from collections import deque

def bfs(problem):
    start = problem.snake.head()
    goal = problem.food

    queue = deque([start])
    came_from = {}
    visited = {start}

    while queue:
        current = queue.popleft()

        if current == goal:
            return reconstruct(came_from, current)

        for action in problem.get_actions():
            neighbor = problem.result(current, action)

            if not problem.is_valid(neighbor, problem.snake.body):
                continue

            if neighbor in visited:
                continue

            visited.add(neighbor)
            came_from[neighbor] = current
            queue.append(neighbor)

    return []


def reconstruct(came_from, current):
    path = []
    while current in came_from:
        path.append(current)
        current = came_from[current]
    return path[::-1]